#!/usr/bin/env python3
"""Vérifie que chaque source citée dans content/breves répond (hors blocages anti-robots 403/429)."""
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

bad = []
for f in sorted(Path(__file__).parent.parent.glob("content/breves/*.json")):
    for s in json.loads(f.read_text(encoding="utf8"))["sources"]:
        req = urllib.request.Request(s["url"], headers={"User-Agent": "Mozilla/5.0 PoidsEtMesuresBot"})
        try:
            urllib.request.urlopen(req, timeout=20)
        except urllib.error.HTTPError as e:
            if e.code not in (403, 429):
                bad.append(f"{f.name}: {s['url']} -> {e.code}")
        except Exception as e:
            bad.append(f"{f.name}: {s['url']} -> {e}")
print("\n".join(bad) or "liens ok")
sys.exit(1 if bad else 0)
