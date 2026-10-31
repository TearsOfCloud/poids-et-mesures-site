# Guide de rédaction des brèves (consignes de la tâche quotidienne)

Média : Poids & Mesures, vulgarisation de l'IA et de la tech, en français, pour des curieux non experts. Éditeur : Tears.

## Déroulé de la tâche quotidienne
1. `git checkout -B breves/AAAA-MM-JJ origin/Main`, puis `python3 veille/collect.py` (écrit `veille/candidats.json`).
2. Choisir 2 à 4 sujets (jamais plus de 5) parmi les candidats : nouveauté qui change quelque chose pour un utilisateur, un développeur, ou une règle de droit. Écarter : communiqués d'investissement, résultats de bourse, événements, pubs, études de cas clients, rumeurs.
3. Pour chaque sujet retenu, **lire la page source primaire en entier** (WebFetch ou curl). Si seule la presse est lisible, retrouver la source primaire (annonce de l'éditeur, texte de loi, décision, dépôt, article de recherche). Pas de source primaire lue = pas de brève.
4. Écrire `content/breves/AAAA-MM-JJ-mots-cles.json` (modèle ci-dessous).
5. `python3 build.py` (doit afficher « contenu ok ») et `python3 veille/liens.py`.
6. Marquer tous les liens traités, retenus ou écartés : `python3 veille/collect.py --vus URL1 URL2 …` (et committer `veille/vus.json`).
7. Pousser la branche et ouvrir **une pull request** « Brèves du JJ/MM » vers `Main`. Description : un bullet par brève avec sa source, les points incertains, et ce qui a été écarté et pourquoi. Tears valide en fusionnant (semaine de validation). Ne jamais fusionner soi-même.
8. Si aucun sujet ne passe le filtre : ne rien publier, ne pas ouvrir de PR, le dire en une ligne.

## Modèle de brève (JSON)
```json
{
  "date": "AAAA-MM-JJ", "heure": "HH:MM",
  "rubrique": "outils | entreprises | regles | recherche",
  "titre": "≤ 110 caractères, une idée, pas de piège à clic",
  "resume": "≤ 300 caractères, comprend seul",
  "en_clair": ["3 paragraphes courts : ce qui s'est passé, ce que ça veut dire, ce qui est annoncé vs mesuré"],
  "pour_toi": "une action ou un réflexe concret, applicable tout de suite, ou « rien à faire » dit franchement avec ce qu'il faut retenir",
  "termes": [{"mot": "…", "def": "définition en une phrase simple"}],
  "sources": [{"nom": "éditeur — titre", "url": "https://…", "date": "AAAA-MM-JJ (date de publication de la source)", "consulte": "AAAA-MM-JJ", "type": "primaire | presse"}],
  "revue": "humaine"
}
```
Le nom du fichier commence par `date`. `revue` vaut « humaine » pendant toute la phase de validation ; « auto » seulement après décision écrite de Tears.

## Règles éditoriales (non négociables)
- Aucun chiffre, citation, date ni nom sans être dans la source lue. Ne jamais compléter de mémoire.
- Distinguer ce que l'entreprise **annonce** de ce qui est **mesuré par un tiers**. Écrire « Google dit », « selon Mistral ».
- Au moins une source de type « primaire ». Reformuler, ne jamais copier de phrase (sauf courte citation entre guillemets, attribuée).
- Expliquer chaque terme technique. Français oral et naturel, pas de traduction mot à mot de l'anglais. Pas de remplissage, pas de « révolution ».
- Pas de sujets sensibles en automatique : santé, justice, élections, personnes nommées, violences. Le validateur bloque `revue: auto` si de tels mots apparaissent.
- Incertitude : l'écrire. Un fait non confirmé n'est pas publié.
- Ne jamais écrire dans `content/correctifs/` sans demande de Tears. Une erreur trouvée après coup = fichier correctif + correction de la brève.

## Correctif (JSON dans content/correctifs/)
`{"date","titre","url","avant","apres"}` : `avant` = phrase erronée citée, `apres` = ce qui est juste.

## Garde-fous
- Bouton d'arrêt : désactiver la tâche programmée, ou supprimer le workflow `deploy.yml`.
- Compte rendu : la PR (semaine 1), puis un résumé hebdomadaire envoyé à Tears.
- Passage en autonomie : seulement si 0 erreur factuelle sur la semaine de validation et décision écrite de Tears.
