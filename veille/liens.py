#!/usr/bin/env python3
"""Vérifie que chaque source citée dans content/breves répond (hors blocages anti-robots 403/429)."""
import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

bad = []
for f in sorted(Path(__file__).parent.parent.glob("content/breves/*.json")):
    for s in json.loads(f.read_text(encoding="utf8"))["sources"]:
        req = urllib.request.Request(s["url"], headers={"User-Agent": "Mozilla/5.0 PoidsEtMesuresBot"})
        err = None
        for essai in range(3):  # erreurs passagères (504...) : on réessaie
            try:
                urllib.request.urlopen(req, timeout=20)
                err = None
                break
            except urllib.error.HTTPError as e:
                err = None if e.code in (403, 429) else e.code
                if err is None or e.code < 500:
                    break
            except Exception as e:
                err = e
            time.sleep(3)
        if err is not None:
            bad.append(f"{f.name}: {s['url']} -> {err}")
print("\n".join(bad) or "liens ok")
sys.exit(1 if bad else 0)
