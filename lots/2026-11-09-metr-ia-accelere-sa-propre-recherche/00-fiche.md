# Lot du 09/11/2026 : METR, l'IA accélère-t-elle sa propre fabrication ? (et comment lire un « 12 fois plus productif »)

## Sujet
Le 5 novembre 2026, METR (organisation indépendante qui évalue les risques de l'IA) a publié son évaluation de 11 semaines à l'intérieur d'Anthropic : les modèles de l'entreprise progressent environ deux fois plus vite qu'avant, et METR estime que cette accélération vient en grande partie de l'usage de l'IA dans la recherche elle-même. Angle débutant : comprendre ce que « l'IA aide à fabriquer l'IA » veut dire concrètement, et surtout apprendre à lire un chiffre de productivité annoncé (sondage interne « 12x » contre mesure sur benchmarks « ~2x »), puis en tirer un réflexe applicable : re-tester ses propres tâches avec les outils récents.

## Pourquoi aujourd'hui
Rapport publié le 05/11, couvert par la presse le 07/11 (The Verge). Source primaire lue en entier (page METR, ~82 000 caractères extraits). Sujet jamais traité dans `lots/` ni `content/` (le mot « METR » n'apparaît qu'en passant dans un article sur les agents, une brève Cursor et un brief d'images).
Écartés : Jensen Huang / Nvidia et Megaspeed (personne nommée, enquête, sensible) ; poursuites contre Suno (justice) ; NYT Cooking IA (iOS abonnés américains, source primaire non lue, test de presse seul) ; Siri plus « agentique » (presse seule, pas d'annonce) ; néoclouds et bourse, midterms et centres de données (finance, politique) ; communiqués NVIDIA Corée (annonces d'écosystème, peu de contenu applicable à un débutant).

## Sources
| Nom | URL | Date de publication | Type |
|---|---|---|---|
| METR, « Independent Assessment of AI R&D Acceleration at Anthropic in October 2026 » | https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment/ | 2026-11-05 | primaire |
| The Verge (Robert Hart), « Why a new report on Anthropic automating AI development is alarming researchers » | https://www.theverge.com/ai-artificial-intelligence/1029126/anthropic-metr-report-accelerating-ai-development | 2026-11-07 | presse (recoupe, ajoute le contexte) |

Consultées le 2026-11-09 (page METR lue en HTML via curl, texte extrait en entier ; The Verge lu en partie, utilisé seulement pour le contexte).

## Faits utilisés (tous tirés de la page METR)
- Évaluation menée du 12 août au 29 octobre 2026, 11 semaines, par l'équivalent de 2,5 personnes à temps plein de METR, sur des appareils fournis par Anthropic. METR dit ne pas avoir pris de paiement d'Anthropic ; Anthropic a fourni des jetons (crédits d'utilisation) gratuits, utilisés surtout pour l'analyse de données.
- Définition de METR : une « accélération de 2x » signifie que deux ans de progrès historique sont réalisés en un an.
- Conclusion de METR (jugement subjectif, incertitude élevée) : en octobre 2026, Anthropic améliore les capacités de ses modèles sur des tâches bien définies à environ deux fois le rythme de mars 2024 à octobre 2025. Fourchette citée : « pas surpris » si c'est plutôt 1,3x ou 3x.
- Mesure sur benchmarks (AECI, version d'Anthropic de l'Epoch Capabilities Index) : depuis octobre 2025, rythme de croissance 1,9x l'ancien [intervalle de confiance à 95 % : 1,5 à 2,8x] ; « environ deux ans de progrès historique en un an ». Les tests de robustesse donnent entre 1,1x et 2,9x.
- METR est « confiant » que l'accélération ne vient pas d'une accélération de la puissance de calcul d'entraînement.
- METR devine qu'une majorité (« peut-être ≈ 80 % ») de l'accélération actuelle est due à l'IA, avec « une incertitude substantielle ». Une partie de l'accélération fin 2025 vient probablement d'autres facteurs.
- Sondages internes (réactions Slack) : accélération perçue moyenne d'environ 12x pour le modèle interne le plus capable en octobre 2026. METR : « très faible preuve », réponses « peu réfléchies », sous-ensemble de personnel probablement non représentatif. Ce chiffre n'est pas une accélération au sens de METR.
- Aujourd'hui, la recherche est accélérée surtout par l'IA qui assiste des humains, pas par une IA autonome ; METR voit des « signes de vie » qui laissent penser que les contributions autonomes pourraient compter bientôt.
- METR n'a pas vu de goulot d'étranglement clair sur les 12 prochains mois (algorithmes, calcul, données), mais écrit ne pas être confiant : sa compréhension a changé plusieurs fois.
- Limites listées par METR : l'accélération pourrait être sous-estimée (automatisation plus proche, benchmarks qui sous-estiment l'impact réel) ou surestimée (facteurs non liés à l'IA, tâches « propres » faciles à noter, rythme historique inhabituellement bas).
- Transparence : Anthropic pouvait caviarder toute information non publique ; METR écrit qu'Anthropic a caviardé « la majorité des preuves que nous avons jugées les plus informatives » pour ses conclusions. Anthropic justifie par « retirer des informations confidentielles qui pourraient accélérer d'autres développeurs d'IA ». METR a aussi remis un rapport complet d'environ 100 pages à Anthropic. Le volet « vérification de l'allocation du calcul entre capacités et sécurité » a été retiré du périmètre par Anthropic en cours de route (raison donnée : rester centré sur l'évaluation du risque).
- Le public doit donc faire davantage confiance au jugement de METR que ce qui serait idéal (formulation de METR).

## Points incertains
- Tout repose sur la lecture de METR de données que le public ne peut pas vérifier (caviardées). Dire « METR estime », jamais « il est prouvé ».
- Le « 2x » concerne des benchmarks de tâches bien définies, pas l'utilité réelle d'un assistant pour un particulier.
- Ne pas confondre : 12x (sondage interne, perception) et ~2x (rythme de progrès des scores). METR le dit lui-même.
- Anthropic est un acteur du paysage dont les modèles sont cités : rester neutre, attribuer chaque chiffre, ne pas présenter le rapport comme une publicité ni comme une alerte. Le média n'a aucun lien commercial avec Anthropic (à confirmer par Tears si besoin pour les mentions).
- Modèles internes non publiés (cités par METR sous des noms de code) : ne pas les nommer, ne rien affirmer sur leurs capacités réelles.
- Ne pas nommer de personnes (dirigeants, chercheurs). Ne pas dire « l'IA va s'emballer » : METR parle d'un risque et d'incertitude.
- Le réflexe « re-tester ses tâches tous les quelques mois » est un conseil de la rédaction, pas une recommandation de METR : à dire comme tel.
