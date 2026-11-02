# Lot du 02/11/2026 : une IA qui marche sans internet (Survival LLM)

**Sujet** : Survival LLM, un assistant IA gratuit et libre qui tourne entièrement sur l'ordinateur, sans connexion, et qui montre ses sources. Angle débutant : « une IA hors ligne, c'est possible, mais la qualité dépend de la mémoire de ton ordinateur, et il faut vérifier ses sources ».

**Pourquoi aujourd'hui** : Numerama en parle le 01/11 (outil remonté sur Hacker News cette semaine). Le sujet répond à une question de débutant (« une IA peut-elle marcher sans internet, et mes questions restent-elles chez moi ? ») et se prolonge avec le futur sujet « vie privée ». Hors Mac Pro, hors lots/content existants : aucun sujet IA locale / hors ligne dans `content/` ni `lots/` (recherche « hors ligne », « local », « ollama » faite).

## Sources (lues en entier le 02/11/2026)
| Nom | URL | Date | Type |
|---|---|---|---|
| Survival LLM, README du dépôt (méthode et tableau des tests) | https://github.com/anonnerdfrenzy/survival-llm | README consulté le 02/11/2026 (version plus récente que la 0.3.4) | primaire |
| Survival LLM, page du projet | https://www.brangus.io/survival-llm | consultée le 02/11/2026 | primaire |
| Numerama, « Conçu pour les situations d'urgence » : cette IA hors ligne… (A. Baba Aissa) | https://www.numerama.com/tech/2364545-concu-pour-les-situations-durgence-cette-ia-hors-ligne-veut-vous-aider-a-survivre-a-la-fin-du-monde-ou-au-moins-a-une-panne-de-courant.html | 2026-11-01 | presse |

## Chiffres utilisés et où ils sont
- Tourne sans internet, questions qui restent sur l'ordinateur, sources affichées : README et page projet (« Nothing you ask leaves it »).
- Bibliothèque : environ 930 000 articles Wikipédia parmi les plus lus (README, Numerama) ; environ 1,5 million d'articles au total (500 000 dans le petit téléchargement) : README.
- Mac 128 Go ou plus : Nemotron 3.5 Super, 80 Go. Ordinateur 16 à 31 Go : IBM Granite 4.2 8B, 6 Go : README et Numerama.
- Test de l'auteur : 22 questions (coupure de courant, premiers secours), notées à l'aveugle par des IA juges contre les guides officiels. « Essentiel juste » : 21/22 (Nemotron Super et Qwen3.8 27B), 14/22 (Granite 4.2 8B) : README. Tests faits sur une version plus ancienne de la bibliothèque : README, à dire.
- Sources inventées : dans un test à part (14 questions, 24/10/2026), des modèles citent des sources qu'ils n'ont pas ouvertes ; l'appli vérifie la ligne « Sources » et la remplace par les articles réellement lus : README.
- 8 Go de mémoire : aucun modèle testé jugé assez sûr, l'appli ne propose que la recherche dans la bibliothèque : README.
- Le plus petit modèle testé (Granite 4.2 3B) a donné 5 réponses nuisibles et n'est pas proposé : README.

## Points incertains
- Tous les chiffres de test viennent de l'auteur du projet, pas d'un tiers. Les juges sont des IA, pas des médecins. À écrire « selon l'auteur ».
- Le README évolue (version plus récente que la 0.3.4 citée par Numerama) : les tailles de modèles peuvent changer.
- Sujet à frontière santé : le lot parle de l'outil et de ses limites, pas de conseils médicaux. Aucune consigne de soin dans les textes. À relire par Tears.
- Astuce « mémoire vive » (menu du Mac, Gestionnaire des tâches Windows) : connaissance générale, pas dans la source. À vérifier sur le Mac avant la voix.
- Pas de test maison (l'outil n'a pas été installé). Si Tears veut un vrai test, passer par une session Mac.
