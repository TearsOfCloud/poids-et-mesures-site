#!/usr/bin/env python3
"""Ajoute à radio/bibliotheque.json les segments d'un fichier de scripts dont le mp3 existe
dans src/assets/radio/audio/ (durée lue avec ffprobe), puis relancer make_grille.py.
Usage : python3 radio/ajouter_segments.py radio/scripts/AAAA-MM-JJ.json"""
import json, pathlib, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
lib_path = ROOT / "radio/bibliotheque.json"
lib = json.loads(lib_path.read_text(encoding="utf8"))
have = {s["id"]: s for s in lib["segments"]}
for s in json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf8"))["segments"]:
    f = ROOT / "src/assets/radio/audio" / (s["id"] + ".mp3")
    if not f.exists():
        print("pas d'audio, ignoré :", s["id"]); continue
    d = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)]))
    have[s["id"]] = {"id": s["id"], "format": s["format"], "titre": s["titre"], "fichier": f.name,
                     "duree": round(d, 1), "texte": s["texte"], "date": json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf8"))["date"]}
lib["segments"] = list(have.values())
lib_path.write_text(json.dumps(lib, ensure_ascii=False, indent=1), encoding="utf8")
print(len(lib["segments"]), "segments")
