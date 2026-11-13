# Lot du 13/11/2026 : Gemini 4 Hydrogen, le nouveau modèle « de tous les jours » de Google (et comment lire ses scores)

## Sujet
Le 12 novembre 2026, Google annonce Gemini 4 Hydrogen, un modèle d'IA rapide présenté comme un « daily driver » (modèle de tous les jours) pour le code et les tâches « agentiques » (l'IA enchaîne plusieurs actions seule). Il arrive dans l'appli Gemini (sélection automatique pour les comptes gratuits), dans Google Search pour tous les utilisateurs, et dans l'API pour les développeurs. Angle débutant : ce qui change concrètement pour toi, et comment lire les scores annoncés par Google (qui les a mesurés ?).

## Pourquoi aujourd'hui
Annonce du 12/11, deux sources primaires Google lues. Sujet utile à un débutant : un modèle gratuit potentiellement meilleur dans l'appli qu'il utilise déjà, et un réflexe de lecture des benchmarks. Écartés : ChatGPT Wallet (page OpenAI illisible depuis la rédaction, la presse seule ne suffit pas), llama.cpp v1.0.0 (page sans commande d'installation, proche du lot « IA hors ligne » du 02/11), sagas Nvidia / Jensen Huang (personne nommée, politique), pannes Outlook et Claude (faits divers sans action utile), sujets sécurité de l'IA et « takeover » (sensibles).

## Sources
| Nom | URL | Date de publication | Type |
|---|---|---|---|
| Google (Koray Kavukcuoglu, DeepMind), « Introducing Gemini 4 Hydrogen » | https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/ | 2026-11-12 | primaire |
| Google (Robby Stein, Search), « Google Search gets a major upgrade with Gemini 4 Hydrogen » | https://blog.google/products-and-platforms/products/search/gemini-4-hydrogen-search-upgrade/ | 2026-11-12 | primaire |

Consultées le 2026-11-13 via l'outil de lecture web (résumé détaillé de chaque page, pas le HTML brut). L'adresse deepmind.google/blog/introducing-gemini-4-hydrogen/ redirige vers la première page. Ars Technica : accès bloqué, non lu.

## Chiffres utilisés (tous tirés des pages Google)
- Prix API : 1,50 $ par million de « tokens » (morceaux de mots) en entrée, 7,50 $ par million en sortie, prix identique sur toute la fenêtre de 1 million de tokens.
- Quatre niveaux de réflexion : low, medium, high (par défaut), xhigh (nouveau).
- Artificial Analysis Intelligence Index : 51 en réflexion « high », contre 50 pour Gemini 4 Argon ; 54 en xhigh. (Artificial Analysis est un tiers, mais la page est un billet Google.)
- Terminal-Bench 4.1 : 57 % contre 18,2 % pour Gemini 3.8 Flash. La page ne dit pas qui a fait passer le test.
- Vitesse : environ 2,5 fois plus rapide que Gemini 3.8 Flash en réflexion « high » (Google) ; tests de partenaires : 2 à 2,8 fois plus rapide, 12 à 23 % de tokens en moins sur des tâches de données en entreprise.
- Accès : appli Gemini, menu de choix du modèle ; comptes gratuits via la sélection automatique « quand ça convient au message » ; Google Search « pour tous les utilisateurs » ; Google Antigravity pour les abonnés AI Pro et Ultra ; API et AI Studio.
- Search (Robby Stein) : meilleure compréhension des questions complexes, en plusieurs parties, avec fautes de frappe ; réponses avec plus d'images, tableaux comparatifs ; Google lance plusieurs recherches en parallèle sur des sous-thèmes (« query fan-out »). Déploiement « mondial », « toutes les langues d'AI Mode ».
- Le billet Search ne donne aucun chiffre de performance.

## Points incertains
- Presque tous les scores viennent de Google ou de ses partenaires ; certains sont relayés par des tiers (Artificial Analysis, Vals.ai, arena.ai) mais pas tous vérifiés indépendamment. Dire « selon Google ».
- Pas de limites d'usage gratuit, ni de calendrier par pays, ni liste des langues. France non confirmée explicitement : dire « pays non précisés ».
- Le billet ne dit pas que Hydrogen remplace 3.8 Flash partout.
- Les chiffres de sécurité (ex. « 81 % de dépassements en moins ») sont des auto-évaluations Google : non repris.
- « Gemini 4 Hydrogen » est un nom de modèle ; ne pas parler d'une appli du même nom.
