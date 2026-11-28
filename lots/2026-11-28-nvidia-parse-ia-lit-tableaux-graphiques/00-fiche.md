# Lot du 28/11/2026 : comment une IA lit un tableau ou un graphique dans un document (Nvidia Nemotron 3.5 Parse)

## Sujet
Le 26 novembre 2026, Nvidia a publié sur le blog Hugging Face un article sur « Nemotron 3.5 Parse », un petit modèle (0,6 milliard de paramètres, d'après la liste des modèles de la page) qui transforme l'image d'une page en données structurées : ordre de lecture, titres, paragraphes, tableaux, graphiques, avec la position de chaque élément. Nvidia dit qu'il lit mieux les graphiques et tableaux difficiles, par exemple un diagramme à barres sans valeurs écrites : le modèle déduit les valeurs d'après les axes et la hauteur des barres. L'article reconnaît que les tableaux sont délicats : « une ligne ou une colonne décalée peut changer totalement le sens ».
Nvidia publie aussi trois jeux de données d'entraînement ouverts et mesure une amélioration après un second entraînement par « apprentissage par renforcement » : les pages où le modèle se met à boucler passent de 126 à 29 ; le score global passe de 66,24 à 71,38 (tests de Nvidia, versions de développement).
Angle débutant : quand on donne un tableau ou un graphique à une IA, elle lit une image de page. Ce qu'elle rend pour un tableau est une reconstruction ; pour un graphique sans chiffres, c'est une estimation. Savoir ça permet de vérifier au bon endroit.

## Pourquoi aujourd'hui
Article publié le 26/11/2026, dans la veille du jour (Hugging Face). Nouveauté non périssable côté usage (comment une IA lit une page), ancrée dans une actualité datée. Sujet jamais traité : recherches « nemotron », « parse », « tableau » dans `lots/` et `content/` sans résultat sur ce thème. Pas le MacBook Pro.

## Sources
| Nom | URL | Date | Type |
|---|---|---|---|
| Nvidia, « Building on Nemotron 3.5 Parse: Open Data, Fine-Tuning, and Faster Inference » (Hugging Face) | https://huggingface.co/blog/nvidia/building-on-nemotron-35-parse-open-data-fine-tunin | 2026-11-26 | primaire (Nvidia, point de vue de l'éditeur) |

Consultée le 2026-11-28, page lue en entier via curl (texte extrait).
Écartés ce jour : jouets IA à New York (enfants, loi : déjà écarté le 27/11 par la règle des sujets sensibles ; les sources primaires existent si Tears veut lever la règle), Nothing Ear (note) (aucune source primaire lisible, produit pas encore sorti), tableau de bord llama.cpp sur AMD (trop technique, voisin du lot « IA hors ligne »), Ai2 et scientifiques (17 entretiens, recherche, peu applicable), Character.AI et conversations (procédure judiciaire), Nvidia/Jensen Huang et S&P (personnes nommées, finance), SpaceX et satellites (proche du lot du 31/10 sur les centres de données dans l'espace), Palantir/OTAN (militaire).

## Faits utilisés (tous tirés de la page primaire)
- Parse : « modèle de document compact » qui transforme des images de pages en données structurées pour la recherche augmentée (RAG) et les agents. Il extrait le contenu dans l'ordre de lecture, attribue des classes (titres, paragraphes, tableaux, graphiques), renvoie des rectangles de position.
- Graphiques sans valeurs marquées : le modèle « peut déduire les valeurs en regardant les axes et la hauteur de la barre ». Exemple de la figure 2 : « 18, 27, 39, 54 ».
- Tableaux : « la structure est si porteuse de sens qu'une ligne ou une colonne décalée peut changer totalement l'interprétation ».
- Données ouvertes : Synthetic Charts V1 (9,98 M d'exemples), Synthetic Tables V1 (1 M), OCR Synthetic Multilingual v2 (7,9 M), générées par ordinateur avec des réponses connues.
- Entraînement en deux phases, dont un apprentissage par renforcement avec récompenses vérifiables. Comparaison de Nvidia sur des versions de développement : pages avec boucle 126 → 29 (environ 77 % de moins), sorties atteignant la limite de 9 000 tokens 185 → 35, score global 66,24 → 71,38 (+5,18 points pour les tableaux, +4,15 pour les graphiques).
- Passes multiples : une passe pour le texte, la mise en page, tableaux et graphiques ; double passe pour les tableaux denses et les petits détails de graphiques ; triple passe pour vérifier que rien n'a été oublié. Selon Nvidia, +2,18 et +2,46 points sur ParseBench par rapport à une seule passe.

## Points incertains / à ne pas dire
- L'article parle d'un modèle spécialisé de Nvidia, pas de ChatGPT, Claude, Gemini ou Le Chat. Ne pas écrire que ces assistants se trompent de la même façon : non vérifié. Le conseil d'application est un conseil de la rédaction (vérifier par échantillon), pas un résultat de l'article.
- Les scores sont ceux de Nvidia sur ses propres tests et sur des synthétiques ; pas de mesure indépendante lue. Dire « selon Nvidia ».
- Le total de pages testées pour 126 → 29 n'est pas donné : ne pas en faire un pourcentage global.
- « 18, 27, 39, 54 » vient d'une figure d'illustration de l'article ; ne pas dire que c'est un test réel d'un assistant grand public.
- Nous n'avons rien testé nous-mêmes.
