# Guide des scripts radio (consignes de la tâche quotidienne)

La radio ne lit que du contenu **déjà publié** sur le site (brève ou article de fond). Rien de nouveau n'entre à l'antenne sans passer d'abord par le site.

## Chaque jour, après la tâche de veille
1. Lire les brèves et articles publiés ou fusionnés depuis la veille.
2. Écrire `radio/scripts/AAAA-MM-JJ.json` (modèle : `radio/scripts/2026-10-31.json`) avec :
   - **1 journal** (3 à 4 minutes, 3 à 5 sujets, un par brève du jour) ;
   - **1 « mot pesé »** (format `bases`, 1 minute) tiré d'un terme du jour ;
   - **1 anecdote ou dossier** (2 à 6 minutes) tiré d'un article de fond (rediffusable, hors actualité périssable).
3. `python3 radio/valider_scripts.py` doit afficher « scripts ok ».
4. Ouvrir une pull request « Scripts radio du JJ/MM » vers `Main`. Tears valide en fusionnant (semaine de validation).

## Écrire pour l'oreille
- Français oral, phrases courtes, « tu ». Pas de traduction mot à mot de l'anglais.
- **Aucun chiffre** : tout s'écrit comme on le dit (« vingt-neuf octobre », « quatre-vingt-huit virgule deux pour cent »). Le validateur bloque les chiffres.
- Jamais de lien, d'adresse ni de commande à lire : dire « va lire la brève sur le site, la vérification y est écrite ».
- Expliquer chaque terme technique la première fois. Dire « Google dit », « selon Mistral » pour tout chiffre d'éditeur ; séparer annoncé et mesuré.
- Aucun fait qui n'est pas dans la brève ou l'article cité (liste `sources` obligatoire).
- Pas de sujets sensibles en automatique (santé, justice, élections, personnes nommées, violences) : mêmes règles que `veille/GUIDE-BREVES.md`.
- Une brève ne passe qu'une fois au journal ; elle peut être rappelée le lendemain si elle est encore vraie.

## Ensuite (étape voix)
Les textes validés vont à Kore (recette HANDOFF-S4-S5, lexique `lexicon.json` pour les noms propres), qui produit un mp3 par segment ; on les ajoute à `radio/bibliotheque.json`, puis `python3 radio/make_grille.py`.
