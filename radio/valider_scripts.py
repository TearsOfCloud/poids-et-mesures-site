#!/usr/bin/env python3
"""Contrôle les scripts radio avant la voix. Sortie non nulle = on ne génère pas.

- chaque segment cite au moins une source qui existe dans content/ (brève ou article) ;
- pas de chiffre dans le texte : tout est écrit comme on le dit (Kore lit mal les chiffres) ;
- pas de lien ni de commande à lire à voix haute ;
- affiche une durée estimée (~150 mots/minute).
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
FORMATS = {"journal", "breve", "titres", "bases", "anecdote", "outil", "dossier"}


def check(path):
    errs, d = [], json.loads(path.read_text(encoding="utf8"))
    ids = set()
    for s in d["segments"]:
        sid = s.get("id", "?")
        if sid in ids:
            errs.append(f"{sid}: id en double")
        ids.add(sid)
        if s.get("format") not in FORMATS:
            errs.append(f"{sid}: format inconnu")
        if not s.get("sources"):
            errs.append(f"{sid}: aucune source")
        for src in s.get("sources", []):
            p = ROOT / "content" / ("breves" if src["type"] == "breve" else "articles") / (src["slug"] + (".json" if src["type"] == "breve" else ""))
            if not p.exists():
                errs.append(f"{sid}: source introuvable {src['slug']}")
        t = s["texte"]
        if re.search(r"\d", t):
            errs.append(f"{sid}: chiffre dans le texte (écrire en lettres) : {re.findall(r'.{12}\d+.{6}', t)[:2]}")
        if re.search(r"https?://|www\.|~/|\$ ", t):
            errs.append(f"{sid}: lien ou commande à lire à voix haute")
        mots = len(t.split())
        print(f"  {sid}: {mots} mots, ~{mots / 150:.1f} min")
    return errs


if __name__ == "__main__":
    allerrs = []
    for f in sorted((ROOT / "radio/scripts").glob("*.json")):
        print(f.name)
        allerrs += check(f)
    if allerrs:
        print("ERREURS :", *allerrs, sep="\n - ")
        sys.exit(1)
    print("scripts ok")
