# Radio P&M

Tout l'audio est fabriqué à l'avance ; le site ne génère jamais de voix en direct.

- `bibliotheque.json` : les segments prêts (voix Kore, musique) avec durée, format, titre, texte.
- `make_grille.py` : transforme la bibliothèque en programme de 24 h (`src/assets/radio/grille.json`). Lancer `python3 radio/make_grille.py` après tout ajout de segment.
- `src/assets/radio.js` : lecteur ; avec l'heure de Paris, il calcule le segment en cours et la seconde de lecture.
- Phase de test : segments = extraits des vidéos longues + musique de synthèse simple. À remplacer par les vrais segments radio (scripts → Kore par lots sur le Mac). Au-delà de ~1 Go d'audio, passer `base` de la grille sur une URL externe (Cloudflare R2).
