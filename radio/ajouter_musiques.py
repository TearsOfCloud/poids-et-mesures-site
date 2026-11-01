#!/usr/bin/env python3
"""Range les pistes produites par musique_lofi.py dans le site et la bibliothèque.
Usage : python3 radio/ajouter_musiques.py <dossier_des_mp3>   (remplace les musiques de démonstration)"""
import json, pathlib, shutil, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
src = pathlib.Path(sys.argv[1])
dst = ROOT / "src/assets/radio/audio"
lib_path = ROOT / "radio/bibliotheque.json"
lib = json.loads(lib_path.read_text(encoding="utf8"))
lib["segments"] = [s for s in lib["segments"] if not s["id"].startswith(("musique", "jingle"))]
for f in sorted(src.glob("*.mp3")):
    shutil.copy(f, dst / f.name)
    d = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)]))
    jing = f.stem.startswith("jingle")
    lib["segments"].append({"id": f.stem, "format": "musique", "titre": "Jingle P&M" if jing else "Musique lo-fi",
                            "fichier": f.name, "duree": round(d, 1), "texte": ""})
for old in dst.glob("musique-demo-*.mp3"):
    old.unlink()
lib_path.write_text(json.dumps(lib, ensure_ascii=False, indent=1), encoding="utf8")
print(len(lib["segments"]), "segments dans la bibliothèque")
