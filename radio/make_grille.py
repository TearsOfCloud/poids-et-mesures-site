#!/usr/bin/env python3
"""Fabrique la grille de la radio (programme de 24 h, répété chaque jour).

Lit radio/bibliotheque.json (segments audio déjà prêts) et écrit
src/assets/radio/grille.json. Le lecteur du site calcule, avec l'heure de Paris,
quel segment passe et à quelle seconde : tout le monde entend la même chose.

Règle : jamais deux segments de voix de suite, de la musique entre les deux ;
on tourne dans la bibliothèque sans rejouer deux fois de suite le même segment.
"""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DAY = 86400


def build(lib):
    segs = {s["id"]: s for s in lib["segments"]}
    voix = [s["id"] for s in lib["segments"] if s["format"] != "musique"]
    music = [s["id"] for s in lib["segments"] if s["format"] == "musique"]
    if not voix or not music:
        raise SystemExit("il faut au moins un segment de voix et une musique")
    plan, t, i, m = [], 0.0, 0, 0
    while t < DAY:
        for sid in (music[m % len(music)], voix[i % len(voix)]):
            plan.append([sid, round(t, 1)])
            t += segs[sid]["duree"]
            if t >= DAY:
                break
        i += 1
        m += 1
    return {"base": "audio/", "duree_cycle": DAY, "segments": segs, "plan": plan}


if __name__ == "__main__":
    lib = json.loads((ROOT / "radio/bibliotheque.json").read_text(encoding="utf8"))
    g = build(lib)
    out = ROOT / "src/assets/radio/grille.json"
    out.write_text(json.dumps(g, ensure_ascii=False, separators=(",", ":")), encoding="utf8")
    print(f"grille : {len(g['plan'])} entrées, {out.stat().st_size // 1024} Ko")
