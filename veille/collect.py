#!/usr/bin/env python3
"""Lit les flux RSS de veille/sources.json et écrit veille/candidats.json (sujets des dernières heures
pas encore traités). Bibliothèque standard seulement.

    python3 veille/collect.py              # collecte
    python3 veille/collect.py --vus URL…   # marque des liens comme traités (publiés OU écartés)
"""
import gzip
import html
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

D = Path(__file__).parent
VUS = D / "vus.json"
IA = re.compile(r"\b(ia|ai|intelligence artificielle|llm|gpt|claude|gemini|mistral|chatbot|agents?|robots?|machine learning|copilot|deepfake|openai|anthropic|nvidia|modèles?|models?)\b", re.I)
NS = {"a": "http://www.w3.org/2005/Atom", "c": "http://purl.org/rss/1.0/modules/content/", "d": "http://purl.org/dc/elements/1.1/"}


def clean(s, n=500):
    s = html.unescape(re.sub(r"<[^>]+>", " ", s or ""))
    return re.sub(r"\s+", " ", s).strip()[:n]


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 PoidsEtMesuresBot", "Accept-Encoding": "gzip"})
    with urllib.request.urlopen(req, timeout=20) as r:
        data = r.read()
        if r.headers.get("Content-Encoding") == "gzip" or data[:2] == b"\x1f\x8b":
            data = gzip.decompress(data)
    return ET.fromstring(data)


def parse_date(s):
    if not s:
        return None
    try:
        d = parsedate_to_datetime(s)
    except (TypeError, ValueError):
        try:
            d = datetime.fromisoformat(s.replace("Z", "+00:00"))
        except ValueError:
            return None
    return d if d.tzinfo else d.replace(tzinfo=timezone.utc)


def items(root):
    for it in root.iter("item"):
        yield (it.findtext("title"), it.findtext("link"), it.findtext("pubDate") or it.findtext("d:date", namespaces=NS), it.findtext("description") or it.findtext("c:encoded", namespaces=NS))
    for e in root.iter("{%s}entry" % NS["a"]):
        l = e.find("a:link[@rel='alternate']", NS)
        if l is None:
            l = e.find("a:link", NS)
        yield (e.findtext("a:title", namespaces=NS), l.get("href") if l is not None else None,
               e.findtext("a:published", namespaces=NS) or e.findtext("a:updated", namespaces=NS), e.findtext("a:summary", namespaces=NS) or e.findtext("a:content", namespaces=NS))


def main():
    vus = set(json.loads(VUS.read_text()) if VUS.exists() else [])
    if "--vus" in sys.argv:
        vus |= set(sys.argv[sys.argv.index("--vus") + 1:])
        VUS.write_text(json.dumps(sorted(vus), indent=1, ensure_ascii=False) + "\n")
        print(len(vus), "liens marqués comme traités")
        return
    cfg = json.loads((D / "sources.json").read_text(encoding="utf8"))
    depuis = datetime.now(timezone.utc) - timedelta(hours=cfg["fenetre_heures"])
    out, pannes = [], []
    for s in cfg["sources"]:
        try:
            root = fetch(s["url"])
        except Exception as e:  # une source en panne ne bloque pas les autres
            pannes.append({"source": s["nom"], "erreur": str(e)[:120]})
            continue
        for titre, lien, date, resume in items(root):
            d = parse_date(date)
            if not (titre and lien and d and d >= depuis) or lien in vus:
                continue
            if s["filtre_ia"] and not IA.search(f"{titre} {clean(resume)}"):
                continue
            out.append({"source": s["nom"], "type": s["type"], "titre": clean(titre, 200), "url": lien.strip(),
                        "date": d.isoformat(), "resume": clean(resume, 400)})
    out.sort(key=lambda x: (x["type"] != "primaire", x["date"]), reverse=False)
    out.sort(key=lambda x: x["date"], reverse=True)
    (D / "candidats.json").write_text(json.dumps({"collecte": datetime.now(timezone.utc).isoformat(), "pannes": pannes, "candidats": out}, indent=1, ensure_ascii=False) + "\n", encoding="utf8")
    print(f"{len(out)} candidats, {len(pannes)} source(s) en panne")
    for p in pannes:
        print("  panne :", p["source"], p["erreur"])


if __name__ == "__main__":
    main()
