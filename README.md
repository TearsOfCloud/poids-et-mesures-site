# Poids & Mesures · site d'actu

Site statique : `python3 build.py` puis ouvrir `dist/index.html`. Voir `AGENTS.md` et `veille/GUIDE-BREVES.md`.

## Hébergement Cloudflare Pages
- Commande de build : `python3 build.py` · Dossier de sortie : `dist` · Variable `SITE_URL` = adresse finale (ex. `https://poids-et-mesures-site.pages.dev`) · `PYTHON_VERSION` = `3.12`.
- GitHub Pages reste actif (`.github/workflows/deploy.yml`) tant que Cloudflare n'est pas vérifié.
