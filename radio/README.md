# Radio P&M

Tout l'audio est fabriqué à l'avance ; le site ne génère jamais de voix en direct.

- `bibliotheque.json` : les segments prêts (voix Kore, musique) avec durée, format, titre, texte.
- `make_grille.py` : transforme la bibliothèque en programme de 24 h (`src/assets/radio/grille.json`). Lancer `python3 radio/make_grille.py` après tout ajout de segment.
- `src/assets/radio.js` : lecteur ; avec l'heure de Paris, il calcule le segment en cours et la seconde de lecture.
- `musique_lofi.py` : compositeur maison (4 styles : lo-fi, boom-bap, ambiant, house douce), aucun droit tiers ; `ajouter_musiques.py` range les pistes. `kore_segments.py` : voix.
- La grille couvre 24 h : jingle à chaque heure, journal à 7 h/12 h/18 h/22 h, deux rendez-vous de voix par heure, rediffusions marquées. Au-delà de ~1 Go d'audio, passer `base` sur une URL externe (Cloudflare R2).
- Chaîne du jour : scripts (PR) → `kore_segments.py` → `ajouter_segments.py` → `make_grille.py AAAA-MM-JJ`.
