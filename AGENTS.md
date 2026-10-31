# Site Poids & Mesures

Site statique en français, généré par `python3 build.py` (bibliothèque standard seulement) vers `dist/`, publié sur GitHub Pages par `.github/workflows/deploy.yml` à chaque fusion dans `Main`.

- `src/` : gabarits (`templates/`), CSS/JS, polices, images. `content/` : articles (`articles/<slug>/{meta.json,page.html}`), brèves (`breves/*.json`), correctifs. `site.json` : éditeur, hébergeur, réseaux, URL.
- Brèves et veille : lire `veille/GUIDE-BREVES.md` avant toute rédaction.
- Polices auto-hébergées, aucun traceur, aucun CDN externe. Fond papier fixe, pas de mode sombre.
- Tears est l'éditeur. Ne jamais stocker de clé ni de mot de passe dans le dépôt. Tears n'est pas technique : pas de procédure Terminal pour lui.
- Un correctif d'erreur factuelle passe avant toute autre tâche.
