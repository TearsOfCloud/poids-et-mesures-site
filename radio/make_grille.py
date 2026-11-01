#!/usr/bin/env python3
"""Fabrique la grille de la radio : le programme d'une journée complète (24 h).

Lit radio/bibliotheque.json (segments audio prêts : voix Kore + musiques + jingles) et écrit
src/assets/radio/grille.json. Le lecteur du site calcule, avec l'heure de Paris, quel segment
passe et à quelle seconde : tout le monde entend la même chose au même moment.

Cadence (modifiable ci-dessous) :
- chaque heure commence par un jingle de 8 s ; journal complet à 7 h, 12 h, 18 h et 22 h ;
- deux rendez-vous de voix par heure en journée (:10 et :40), un toutes les deux heures la nuit ;
- entre deux, de la musique, sans jamais rejouer deux fois la même de suite ;
- tout passage d'un segment déjà diffusé plus tôt est marqué « rediffusion » (le lecteur l'affiche).
Une entrée du plan = [id, début en secondes depuis minuit, durée jouée, rediffusion 0/1].
Le lecteur coupe en fondu la dernière musique d'un trou pour tomber pile sur le rendez-vous suivant.
Usage : python3 radio/make_grille.py [AAAA-MM-JJ]   (la date sert de graine à l'ordre des musiques)
"""
import json, pathlib, random, sys, datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
DAY = 86400
JOURNAL_HEURES = (7, 12, 18, 22)
VOIX_JOUR = (10, 40)            # minutes de chaque heure (7 h à 23 h)
NUIT = (1, 3, 5)                # heures avec un rendez-vous de voix la nuit (rediffusions)
RESTE_MIN = 25                  # on évite un morceau final plus court que ça


def ordre_voix(segs):
    """Rotation des segments de voix (hors journal), en alternant les formats."""
    par = {}
    for s in segs:
        if s["format"] != "journal":
            par.setdefault(s["format"], []).append(s["id"])
    out, formats = [], sorted(par, key=lambda f: -len(par[f]))
    while any(par.values()):
        for f in formats:
            if par[f]:
                out.append(par[f].pop(0))
    return out


def build(lib, jour=None):
    segs = {s["id"]: s for s in lib["segments"]}
    voix = [s for s in lib["segments"] if s["format"] != "musique"]
    musiques = [s["id"] for s in lib["segments"] if s["format"] == "musique" and not s["id"].startswith("jingle")]
    jingles = [s["id"] for s in lib["segments"] if s["id"].startswith("jingle")]
    journaux = sorted((s for s in voix if s["format"] == "journal"), key=lambda s: s.get("date", ""))
    if not voix or not musiques:
        raise SystemExit("il faut au moins un segment de voix et une musique")
    rng = random.Random(jour or "defaut")
    cycle = ordre_voix(voix) or [voix[0]["id"]]

    # 1) rendez-vous de voix : (secondes, id)
    rdv, k = [], 0
    for h in range(24):
        if 7 <= h <= 23:
            for m in VOIX_JOUR:
                t = h * 3600 + m * 60
                if m == VOIX_JOUR[0] and h in JOURNAL_HEURES and journaux:
                    rdv.append((h * 3600 + 8, journaux[-1]["id"]))
                else:
                    rdv.append((t, cycle[k % len(cycle)])); k += 1
        elif h in NUIT:
            rdv.append((h * 3600 + 20 * 60, cycle[k % len(cycle)])); k += 1
    rdv.sort()
    # 2) événements fixes : jingle à chaque heure pile, puis les rendez-vous de voix
    ev = []
    for h in range(24):
        if jingles:
            ev.append((h * 3600, jingles[h % len(jingles)]))
    for t, sid in rdv:
        ev.append((t, sid))
    ev.sort(key=lambda e: (e[0], e[1].startswith("jingle") is False))
    # 3) on déroule la journée en remplissant les trous de musique
    plan, deja, pool, last = [], set(), [], None
    def tirer():
        nonlocal pool, last
        if not pool:
            pool = musiques[:]; rng.shuffle(pool)
            if pool[0] == last and len(pool) > 1: pool.append(pool.pop(0))
        last = pool.pop(0)
        return last
    t = 0.0
    nuit_fin = 7 * 3600
    for i, (st, sid) in enumerate(ev):
        # trou de musique avant cet événement
        while st - t > 1.0:
            m = tirer(); d = segs[m]["duree"]; reste = st - t
            jouee = reste if (d >= reste or reste - d < RESTE_MIN) else d
            plan.append([m, round(t, 1), round(min(jouee, d), 1), 0]); t += min(jouee, d)
            if jouee > d: pass
        t = max(t, st) if st - t > 0 else t
        d = segs[sid]["duree"]
        is_j = sid.startswith("jingle")
        redif = 0 if (is_j or (sid not in deja and st >= nuit_fin)) else 1
        if not is_j: deja.add(sid)
        suivant = ev[i + 1][0] if i + 1 < len(ev) else DAY
        plan.append([sid, round(t, 1), round(min(d, max(1.0, suivant - t)), 1), redif]); t += min(d, max(1.0, suivant - t))
    while DAY - t > 1.0:
        m = tirer(); d = segs[m]["duree"]; reste = DAY - t
        jouee = min(d, reste)
        plan.append([m, round(t, 1), round(jouee, 1), 0]); t += jouee
    used = {p[0] for p in plan}
    return {"base": "audio/", "duree_cycle": DAY, "date": jour, "segments": {i: segs[i] for i in segs if i in used}, "plan": plan}


if __name__ == "__main__":
    jour = sys.argv[1] if len(sys.argv) > 1 else datetime.date.today().isoformat()
    lib = json.loads((ROOT / "radio/bibliotheque.json").read_text(encoding="utf8"))
    g = build(lib, jour)
    out = ROOT / "src/assets/radio/grille.json"
    out.write_text(json.dumps(g, ensure_ascii=False, separators=(",", ":")), encoding="utf8")
    voix = sum(p[2] for p in g["plan"] if not g["segments"][p[0]]["format"] == "musique")
    print(f"grille {jour} : {len(g['plan'])} entrées, voix {voix/60:.0f} min sur 24 h, {out.stat().st_size // 1024} Ko")
