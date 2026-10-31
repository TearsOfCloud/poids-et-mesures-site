#!/usr/bin/env python3
"""Génère le site statique dans ./dist à partir de src/ et content/. Bibliothèque standard seulement.

    python3 build.py            # valide le contenu puis construit
    python3 build.py --check    # valide seulement
"""
import html
import json
import re
import shutil
import sys
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "src"
DIST = ROOT / "dist"
SITE = json.loads((ROOT / "site.json").read_text(encoding="utf8"))

RUBRIQUES_BREVES = {
    "outils": ("Outils", "c-vert"),
    "entreprises": ("Entreprises", "c-corail"),
    "regles": ("Règles", "c-bleu"),
    "recherche": ("Recherche", "c-gris"),
}
RUBRIQUES_ARTICLES = {
    "bases": ("Les bases", "c-bleu", "v-bleu"),
    "anecdote": ("Anecdote", "c-corail", "v-corail"),
    "benchmark": ("Benchmark", "c-vert", "v-vert"),
    "actu": ("L'actu pesée", "c-gris", "v-bleu"),
    "outil": ("Outil testé", "c-vert", "v-vert"),
}
# sujets qui exigent une relecture humaine (garde-fou du cadrage : pas d'automatique)
SENSIBLE = re.compile(
    r"\b(santé|médic|cancer|suicide|procès|tribunal|plainte|condamn|arrêté|mort|décès|"
    r"attentat|guerre|élection|candidat|député|ministre|président)\w*",
    re.I,
)

esc = html.escape


def load_json(path):
    return json.loads(path.read_text(encoding="utf8"))


def fr_date(iso):
    y, m, d = iso.split("-")
    return f"{d}/{m}/{y}"


# ---------- contenu ----------

def load_articles():
    out = []
    for d in sorted((ROOT / "content/articles").glob("*/")):
        meta = load_json(d / "meta.json")
        meta["slug"] = d.name
        meta["page"] = (d / "page.html").read_text(encoding="utf8")
        out.append(meta)
    return sorted(out, key=lambda a: a["date"], reverse=True)


def load_breves():
    out = []
    for f in sorted((ROOT / "content/breves").glob("*.json")):
        b = load_json(f)
        b["slug"] = f.stem
        out.append(b)
    return sorted(out, key=lambda b: (b["date"], b.get("heure", "00:00")), reverse=True)


def load_correctifs():
    d = ROOT / "content/correctifs"
    return sorted((load_json(f) for f in d.glob("*.json")), key=lambda c: c["date"], reverse=True) if d.exists() else []


def validate(articles, breves):
    errs = []
    seen = set()
    for b in breves:
        n = b["slug"]
        for k in ("date", "heure", "rubrique", "titre", "resume", "en_clair", "pour_toi", "sources", "revue"):
            if not b.get(k):
                errs.append(f"{n}: champ manquant « {k} »")
        if n in seen:
            errs.append(f"{n}: doublon")
        seen.add(n)
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}-[a-z0-9-]+", n):
            errs.append(f"{n}: le nom du fichier doit être AAAA-MM-JJ-mots-cles")
        if b.get("date") and not n.startswith(b["date"]):
            errs.append(f"{n}: le nom doit commencer par la date ({b['date']})")
        if b.get("rubrique") not in RUBRIQUES_BREVES:
            errs.append(f"{n}: rubrique inconnue « {b.get('rubrique')} »")
        if b.get("revue") not in ("humaine", "auto"):
            errs.append(f"{n}: revue doit valoir « humaine » ou « auto »")
        if len(b.get("titre", "")) > 110:
            errs.append(f"{n}: titre trop long ({len(b['titre'])} > 110)")
        if len(b.get("resume", "")) > 300:
            errs.append(f"{n}: résumé trop long ({len(b['resume'])} > 300)")
        texte = " ".join([b.get("titre", ""), b.get("resume", ""), *b.get("en_clair", []), b.get("pour_toi", "")])
        if re.search(r"exemple\s*:|lorem|à compléter|\btodo\b", texte, re.I):
            errs.append(f"{n}: texte provisoire détecté")
        if not b.get("sources"):
            errs.append(f"{n}: au moins une source est obligatoire")
        for s in b.get("sources", []):
            if not str(s.get("url", "")).startswith("https://") or not s.get("nom") or not s.get("date"):
                errs.append(f"{n}: source incomplète (nom, url https, date) : {s}")
            elif s["date"] > b.get("date", "9999"):
                errs.append(f"{n}: la source est datée après la brève")
        if not any(s.get("type") == "primaire" for s in b.get("sources", [])):
            errs.append(f"{n}: aucune source primaire (type « primaire »)")
        if b.get("revue") == "auto" and SENSIBLE.search(texte):
            errs.append(f"{n}: sujet sensible, publication automatique interdite (revue doit être « humaine »)")
    for a in articles:
        for k in ("titre", "titre_html", "description", "rubrique", "date", "minutes", "image"):
            if not a.get(k):
                errs.append(f"article {a['slug']}: champ manquant « {k} »")
        if a.get("rubrique") not in RUBRIQUES_ARTICLES:
            errs.append(f"article {a['slug']}: rubrique inconnue")
    return errs


# ---------- gabarits ----------

def tpl(name):
    return (SRC / "templates" / name).read_text(encoding="utf8")


def fill(t, **kw):
    for k, v in kw.items():
        t = t.replace("{{" + k + "}}", v)
    return t


def social_html(root):
    items = [f'<li><a href="{esc(u)}" rel="noopener" target="_blank">{esc(n)}</a></li>' for n, u in SITE["reseaux"].items() if u]
    return "".join(items) or '<li>@poidsetmesuresia</li>'


def breve_html(b, root):
    nom, cls = RUBRIQUES_BREVES[b["rubrique"]]
    s = b["sources"][0]
    return (
        f'<article class="breve" data-cat="{b["rubrique"]}"><time class="mono" datetime="{b["date"]}">{b["date"][8:]}/{b["date"][5:7]} · {esc(b["heure"])}</time>'
        f'<h3><a href="{root}breves/{b["slug"]}/">{esc(b["titre"])}</a></h3>'
        f'<div class="row"><span class="mono tag {cls}">{nom}</span>'
        f'<a class="mono src" href="{esc(s["url"])}" rel="noopener" target="_blank">Source : {esc(s["nom"])} ↗</a></div></article>'
    )


def card_html(a, root):
    nom, cls, vis = RUBRIQUES_ARTICLES[a["rubrique"]]
    q = re.sub(r"[̀-ͯ]", "", __import__("unicodedata").normalize("NFD", f'{a["titre"]} {a["description"]} {a.get("mots_cles","")}'.lower()))
    badge = '<span class="vbadge">▶ Vidéo</span>' if a.get("video") else ""
    return (
        f'<a class="card piece dossier" href="{root}articles/{a["slug"]}/" data-r="{a["rubrique"]}" data-v="{1 if a.get("video") else 0}" data-q="{esc(q)}">{badge}'
        f'<div class="vis {vis}"><img class="sticker" src="{root}assets/img/{a["image"]}.png" alt=""></div>'
        f'<span class="mono tag {cls}">{nom}</span><h3>{esc(a["titre"])}</h3><p>{esc(a["description"].split(". Source")[0])}</p>'
        f'<div class="meta mono">{fr_date(a["date"])[:5]} · {a["minutes"]} min · Source primaire</div></a>'
    )


def head(title, desc, root, path, extra=""):
    url = SITE["url"].rstrip("/") + "/" + path
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{esc(url)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Poids &amp; Mesures">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="{esc(SITE['url'].rstrip('/'))}/assets/og.png">
<meta property="og:url" content="{esc(url)}">
<meta property="og:locale" content="fr_FR">
<meta name="twitter:card" content="summary_large_image">
<link rel="alternate" type="application/rss+xml" title="Poids &amp; Mesures" href="{root}rss.xml">
<link rel="icon" href="{root}assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{root}assets/site.css">
{extra}</head>
"""


def page(path, title, desc, view_id, view_html, ctx, nav="", extra=""):
    root = "../" * path.count("/") if path.endswith("/") else "../" * path.count("/")
    root = root or ""
    fil = ctx["fil"]
    body = fill(
        tpl("top.html") + "\n<main>\n<section class=\"view on\" id=\"" + view_id + "\">" + view_html + "\n</section>\n</main>\n" + tpl("footer.html") + tpl("mini.html"),
        fil_html=fil, social_html=social_html(root), editeur=esc(SITE["editeur"]),
    )
    body = body.replace("{{root}}", root)
    out = head(title, desc, root, path, extra) + f'<body data-page="{nav}">\n' + body + f'\n<script src="{root}assets/site.js"></script>\n<script src="{root}assets/radio.js"></script>\n</body>\n</html>\n'
    dest = DIST / path / "index.html" if path else DIST / "index.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(out, encoding="utf8")


def jsonld(d):
    return '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False) + "</script>\n"


# ---------- pages ----------

def build():
    articles, breves, correctifs = load_articles(), load_breves(), load_correctifs()
    errs = validate(articles, breves)
    if errs:
        print("ERREURS DE CONTENU :", *errs, sep="\n - ")
        sys.exit(1)
    print(f"contenu ok : {len(articles)} article(s), {len(breves)} brève(s)")
    if "--check" in sys.argv:
        return

    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    shutil.copytree(SRC / "assets", DIST / "assets")
    (DIST / ".nojekyll").write_text("")
    # radio : chaque segment de la grille doit avoir son fichier audio
    gj = SRC / "assets/radio/grille.json"
    if gj.exists():
        g = json.loads(gj.read_text(encoding="utf8"))
        manque = [x["fichier"] for x in g["segments"].values() if g["base"].startswith("http") is False and not (SRC / "assets/radio" / g["base"] / x["fichier"]).exists()]
        if manque:
            print("RADIO : fichiers audio manquants :", *manque, sep="\n - "); sys.exit(1)

    last = breves[:8]
    fil_items = "".join(f'<a href="{{{{root}}}}breves/{b["slug"]}/">{esc(b["titre"])}</a>' for b in last) or '<a href="{{root}}methode/">Les premières brèves arrivent bientôt</a>'
    ctx = {"fil": fil_items * 2}
    une = next((a for a in articles if a.get("une")), articles[0] if articles else None)
    base_desc = "L'actu de l'IA expliquée pour tout le monde, sources à l'appui. Et une radio à venir."

    # accueil
    others = [a for a in articles if a is not une][:2]
    side = "".join(
        (lambda nom, cls, vis: (
            f'<a class="card piece torn pose" href="{{{{root}}}}articles/{a["slug"]}/" style="--r:{2 if i == 0 else -1.5}deg">'
            f'<img class="obj sticker" src="{{{{root}}}}assets/img/{a["image"]}.png" alt=""><span class="mono tag {cls}">{nom}</span>'
            f'<h3>{esc(a["titre"])}</h3><p>{esc(a["description"].split(". Source")[0])}</p><div class="meta mono">{a["minutes"]} min</div></a>'
        ))(*RUBRIQUES_ARTICLES[a["rubrique"]][:2])
        for i, a in enumerate(others)
    )
    if len(others) < 2:
        side += (
            '<a class="card piece torn pose" href="{{root}}methode/" style="--r:-1.5deg"><img class="obj sticker" src="{{root}}assets/img/balance.png" alt="">'
            '<span class="mono tag c-vert">Transparence</span><h3>Comment on <mark>travaille</mark></h3>'
            "<p>De la veille à ton oreille : sources, vérification, correctifs.</p><div class=\"meta mono\">2 min</div></a>"
        )
    brv = "".join(breve_html(b, "{{root}}") for b in last) or (
        '<p class="empty">Les premières brèves arrivent bientôt. Chacune sera liée à sa source officielle.</p>'
    )
    dossiers = ""
    if len(articles) > 1:
        dossiers = (
            '  <div class="sec-h"><h2>Les <em>dossiers</em></h2><a class="mono" href="{{root}}articles/" style="text-decoration:underline">Tous les articles →</a></div>\n  <div class="dossiers">'
            + "".join(card_html(a, "{{root}}").replace("card piece dossier", "card piece dossier pose") for a in articles[:3])
            + "</div>\n"
        )
    home = fill(tpl("home.html"), side_cards=side, breves_html=brv, dossiers_section=dossiers, une_url="{{root}}articles/" + (une["slug"] + "/" if une else ""))
    home = home.replace('<div class="sec-h"><h2>Les <em>brèves</em></h2>', '<div class="sec-h"><h2>Les <em>brèves</em></h2>', 1)
    if len(breves) > len(last):
        home = home.replace('<aside class="mot', '<p style="margin:0 0 18px"><a class="mono" href="{{root}}breves/" style="text-decoration:underline">Toutes les brèves →</a></p>\n   <aside class="mot', 1) if False else home
    page("", "Poids & Mesures · On pèse ce que l'IA fait vraiment", base_desc, "v-home", home, ctx, "home")

    # articles
    page("articles/", "Les articles · Poids & Mesures", "Tout ce qu'on a pesé : les bases, les anecdotes, les tests.", "v-articles",
         fill(tpl("articles.html"), grid_html="".join(card_html(a, "{{root}}") for a in articles)), ctx, "articles")
    for a in articles:
        others = [x for x in articles if x is not a][:2]
        if others:
            nxt = '<div class="piece"><span class="mono">À lire ensuite</span>' + "".join(
                f'<a href="{{{{root}}}}articles/{x["slug"]}/" style="display:block;margin-top:10px;font-weight:900;font-size:19px;letter-spacing:-.02em;line-height:1.2">{esc(x["titre"])}</a>' for x in others) + "</div>"
        else:
            nxt = '<div class="piece"><span class="mono">À lire ensuite</span><a href="{{root}}breves/" style="display:block;margin-top:10px;font-weight:900;font-size:19px;letter-spacing:-.02em;line-height:1.2">Les dernières brèves, sourcées</a></div>'
        vid = ""
        if a.get("video"):
            vid = (f'<a class="piece video" href="{esc(a["video"])}" rel="noopener" target="_blank" aria-label="Voir la vidéo" style="padding:16px;display:grid;margin-bottom:24px">'
                   f'<span class="phone"><span class="t">{esc(a["titre"])}</span><img src="{{{{root}}}}assets/img/laptop.png" alt=""><span class="pl">▶</span><span class="ru"></span></span>'
                   '<span><span class="mono c-corail">Voir en vidéo</span><b style="display:block;font-size:19px;letter-spacing:-.02em;line-height:1.15;margin:6px 0">L\'histoire en 80 secondes</b><span class="mono c-gris">Reel · @poidsetmesuresia</span></span></a>')
        ld = jsonld({"@context": "https://schema.org", "@type": "Article", "headline": a["titre"], "datePublished": a["date"], "inLanguage": "fr",
                     "description": a["description"], "publisher": {"@type": "Organization", "name": "Poids & Mesures"}})
        page(f"articles/{a['slug']}/", a["titre"] + " · Poids & Mesures", a["description"], "v-article",
             fill(a["page"], video_html=vid, next_html=nxt), ctx, "articles", ld)

    # brèves
    lst = "".join(breve_html(b, "{{root}}") for b in breves) or '<p class="empty">Les premières brèves arrivent bientôt.</p>'
    page("breves/", "Les brèves · Poids & Mesures", "L'actu de l'IA en quelques lignes, chaque brève liée à sa source.", "v-breves",
         '<div class="wrap"><div class="page"><span class="mono c-corail">Le fil</span><h1>Toutes les <em>brèves</em></h1>'
         '<p class="chapo">Chaque brève tient en quelques lignes, explique les mots difficiles et renvoie à sa source.</p>'
         f'<div class="breves" style="display:block"><div id="breves">{lst}</div></div></div></div>', ctx, "home")
    for b in breves:
        nom, cls = RUBRIQUES_BREVES[b["rubrique"]]
        paras = "".join(f"<p>{esc(p)}</p>" for p in b["en_clair"])
        termes = ""
        if b.get("termes"):
            termes = '<div class="piece torn" style="margin:22px 0"><span class="mono">Les mots expliqués</span><dl style="margin-top:10px">' + "".join(
                f'<dt style="font-weight:900;margin-top:8px">{esc(t["mot"])}</dt><dd>{esc(t["def"])}</dd>' for t in b["termes"]) + "</dl></div>"
        srcs = "".join(
            f'<li>{i}. <a href="{esc(s["url"])}" rel="noopener" target="_blank" style="text-decoration:underline">{esc(s["nom"])}</a>'
            f'{" (source primaire)" if s.get("type") == "primaire" else ""}, publié le {fr_date(s["date"])}. Consultée le {fr_date(s.get("consulte", b["date"]))}.</li>'
            for i, s in enumerate(b["sources"], 1))
        relu = ("Relue par l'éditeur avant publication." if b["revue"] == "humaine"
                else "Publiée automatiquement, relue par l'éditeur après coup. Une erreur ? Signale-la.")
        view = f"""
 <div class="wrap"><article class="page">
  <div class="crumb"><a class="mono" href="{{{{root}}}}">Accueil</a><span class="mono">/</span><span class="mono tag {cls}">{nom}</span><span class="mono c-gris">· {fr_date(b['date'])} · {esc(b['heure'])}</span></div>
  <h1 style="margin-top:18px">{esc(b['titre'])}</h1>
  <p class="chapo">{esc(b['resume'])}</p>
  <div class="prose" style="margin-top:26px"><h2>En clair</h2>{paras}
   <div class="tldr piece torn" style="margin:24px 0"><span class="mono">Ce que tu peux en faire</span><p style="margin-top:8px">{esc(b['pour_toi'])}</p></div>
   {termes}
   <div class="sources"><span class="mono">Sources</span><ol style="list-style:none">{srcs}</ol></div>
   <div class="transp"><b>Comment cette brève a été faite.</b> Rédigée avec l'aide de l'IA à partir des sources ci-dessus. {relu} <a href="{{{{root}}}}correctifs/" style="text-decoration:underline">Voir les correctifs</a>.</div>
  </div>
 </article></div>"""
        ld = jsonld({"@context": "https://schema.org", "@type": "NewsArticle", "headline": b["titre"], "datePublished": b["date"], "inLanguage": "fr",
                     "description": b["resume"], "publisher": {"@type": "Organization", "name": "Poids & Mesures"}})
        page(f"breves/{b['slug']}/", b["titre"] + " · Poids & Mesures", b["resume"], "v-breve", view, ctx, "home", ld)

    # radio, méthode, correctifs, mentions
    page("radio/", "La radio · Poids & Mesures", "La webradio de Poids & Mesures, en test : journal, bases, anecdotes, outils testés, à écouter en continu.", "v-radio", tpl("radio.html"), ctx, "radio")
    page("methode/", "Comment on travaille · Poids & Mesures", "De la veille à ton oreille : sources, vérification, correctifs.", "v-methode", tpl("methode.html"), ctx, "")
    corr = "".join(
        f'<div class="piece corr torn" style="margin-top:20px"><span class="mono c-gris">{fr_date(c["date"])} · <a href="{esc(c["url"])}" style="text-decoration:underline">{esc(c["titre"])}</a></span>'
        f'<p style="margin-top:8px" class="avant">« {esc(c["avant"])} »</p><p style="margin-top:6px"><b>Corrigé :</b> {esc(c["apres"])}</p></div>' for c in correctifs
    ) or '<p style="margin-top:26px"><b>Aucun correctif publié pour l\'instant.</b> Le jour où on se trompe, ça apparaît ici.</p>'
    page("correctifs/", "Correctifs · Poids & Mesures", "Quand on se trompe, on le corrige ici, en clair.", "v-correctifs", fill(tpl("correctifs.html"), correctifs_html=corr), ctx, "")
    contact = esc(SITE["contact"]) or "à compléter"
    page("mentions-legales/", "Mentions légales · Poids & Mesures", "Éditeur, hébergeur et contact.", "v-mentions",
         f'<div class="wrap"><div class="page"><span class="mono c-gris">Transparence</span><h1>Mentions <em>légales</em></h1>'
         f'<div class="prose" style="margin-top:20px"><h2>Éditeur et directeur de la publication</h2><p>{esc(SITE["editeur"])}</p><h2>Contact</h2><p>{contact}</p>'
         f'<h2>Hébergeur</h2><p>{esc(SITE["hebergeur"])}</p><h2>Contenus</h2><p>Les articles et brèves sont rédigés avec l\'aide de l\'IA, à partir de sources citées, puis relus par l\'éditeur. '
         'La voix de la radio est une voix de synthèse et la musique est générée par IA. Les marques citées appartiennent à leurs propriétaires. Aucun cookie de suivi n\'est déposé ; les polices sont hébergées sur ce site.</p></div></div></div>',
         ctx, "")
    (DIST / "404.html").write_text(
        head("Page introuvable · Poids & Mesures", "Cette page n'existe pas.", "/" + SITE["url"].split("/", 3)[-1].strip("/") + "/" if "github.io" in SITE["url"] else "/", "404.html")
        + '<body><main style="max-width:640px;margin:20vh auto;padding:0 20px"><h1 style="font-size:56px">Page <em>introuvable</em></h1><p style="margin-top:16px"><a href="./" style="text-decoration:underline">Retour à l\'accueil</a></p></main></body></html>', encoding="utf8")

    # RSS + sitemap
    base = SITE["url"].rstrip("/")
    items = [(a["date"], "00:00", a["titre"], f"{base}/articles/{a['slug']}/", a["description"]) for a in articles]
    items += [(b["date"], b["heure"], b["titre"], f"{base}/breves/{b['slug']}/", b["resume"]) for b in breves]
    items.sort(reverse=True)
    rss = "".join(
        f"<item><title>{esc(t)}</title><link>{u}</link><guid>{u}</guid><pubDate>{format_datetime(datetime.fromisoformat(d + 'T' + h + ':00+00:00'))}</pubDate><description>{esc(desc)}</description></item>"
        for d, h, t, u, desc in items[:40])
    (DIST / "rss.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>Poids &amp; Mesures</title>'
        f"<link>{base}/</link><description>{esc(SITE['accroche'])}. L'actu de l'IA expliquée pour tout le monde, sources à l'appui.</description><language>fr-fr</language>{rss}</channel></rss>", encoding="utf8")
    urls = [""] + ["articles/", "breves/", "radio/", "methode/", "correctifs/", "mentions-legales/"] + [f"articles/{a['slug']}/" for a in articles] + [f"breves/{b['slug']}/" for b in breves]
    (DIST / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(f"<url><loc>{base}/{u}</loc></url>" for u in urls) + "</urlset>", encoding="utf8")
    (DIST / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {base}/sitemap.xml\n")
    print(f"site construit dans {DIST} ({len(urls)} pages)")


if __name__ == "__main__":
    build()
