# Lot du 14/11/2026 : « Skills » : écrire une fois la tâche que tu réexpliques à l'IA

## Sujet
Le 12 novembre 2026, le blog de GitHub a publié un guide pratique sur les « agent skills » : des dossiers réutilisables, centrés sur un fichier `SKILL.md`, qui décrivent quand et comment faire une tâche répétitive. Angle débutant : arrêter de réexpliquer la même chose à son assistant IA, et comprendre ce qu'une skill fait (donner des instructions) et ne fait pas (donner des accès). Application immédiate : choisir la tâche qu'on réexplique le plus et l'écrire en trois blocs (ce qu'il faut, où ça s'arrête, ce que le relecteur vérifie), conseil donné par l'article.

## Pourquoi aujourd'hui
Article publié le 12/11 (présenté à GitHub Universe 2026). Sujet jamais traité dans `lots/` ni `content/` (recherche « skill » : seul un article sur des outils gratuits pour Claude le mentionne, pas ce guide). Pas de rumeur, pas de nom de personne dans nos textes.

## Sources
| Nom | URL | Date de publication | Type |
|---|---|---|---|
| GitHub Blog, « Build once, run on any agent: A practical guide to agent skills » | https://github.blog/ai-and-ml/github-copilot/build-once-run-on-any-agent-a-practical-guide-to-agent-skills/ | 2026-11-12 | primaire (article d'un éditeur d'outils, donc un point de vue : GitHub vend Copilot) |

Consultée le 2026-11-14, page lue en entier via curl (texte complet extrait). Écartés ce jour-là : ChatGPT Wallet (page OpenAI illisible par les outils : anti-robot, pas de source primaire lue), Claude Duet (annoncé le 21/10, source primaire non retrouvée, page Verge bloquée), llama.cpp 1.0 et Gemini 4 Hydrogen (déjà dans `content/`/`lots/`), affaire Nvidia (personnes nommées, sujet sensible).

## Faits utilisés (tous tirés de la page, rien de mémoire)
- Définition : une skill est « un répertoire versionné centré sur un fichier SKILL.md qui décrit quand et comment faire une tâche répétable ». On peut partager ces instructions entre agents, mais l'environnement doit fournir outils, identifiants et permissions. Exemple de la page : une skill peut décrire comment interroger une base de données, elle ne donne pas accès à cette base.
- Exemple « Proof Agent » : un agent qui vérifie les changements produits par une IA par rapport à la demande d'origine. Si le même agent juge son propre travail, son explication peut influencer la relecture ; on utilise donc un vérificateur séparé qui donne des preuves. Règle citée : « self-verification is not verification ». En-tête du SKILL.md : `name` et `description`.
- Le vérificateur renvoie PASS, FAIL ou PARTIAL et doit citer des preuves dans les fichiers modifiés. Il fait une relecture statique du diff (il n'exécute ni code ni tests). Dans la démo, `block-on-fail: false` : les résultats étaient consultatifs.
- Exemple « Data Forge » : quatre skills (`forge-init`, `forge-builder`, `forge-dbx`, `forge-lint`) qui lisent un même fichier de configuration (« manifest ») au lieu de coder en dur les noms de projet. Workflow à 7 phases, avec un point de contrôle humain à chaque phase ; approbation demandée avant les changements de schéma.
- Quand utiliser une skill : tâche bornée et répétable (liste de contrôle, publication, migration, pipeline de métriques). Si le flux demande interface stable, état partagé, journal d'audit, contrôle long ou permissions imposées hors du modèle : une application convient mieux.
- Packaging : `skills/*/SKILL.md` comme source ; un script génère les fichiers propres à Claude Code (`.claude-plugin/plugin.json`), Cursor (`.cursor-plugin/plugin.json`) et GitHub Copilot (`.github/agents/*.agent.md`). Après installation : vérifier que l'outil reconnaît la skill, charge ses références, peut utiliser les outils requis et renvoie les preuves attendues.
- Conseil de fin d'article : « Start with the task you're tired of explaining. Write down what it needs, where it stops, and what a reviewer sees. Then try it with another agent. »

## Points incertains / à ne pas dire
- Aucun chiffre mesuré, aucun test indépendant : c'est un guide de pratiques, pas une étude. Dire « selon GitHub » et ne pas promettre de gain de temps.
- La page décrit des exemples pour développeurs (pipelines de données, revue de code). La traduction « tâche de tous les jours » (mail type, compte rendu, post) est l'angle de la rédaction, pas un exemple de la source.
- Ne pas affirmer que ChatGPT, Gemini ou Le Chat gèrent les fichiers SKILL.md : la source ne cite que Claude Code, Cursor et GitHub Copilot. Pour les autres : coller la notice au début de la conversation (conseil de rédaction, à tester).
- Ne pas nommer l'auteure ni les intervenants. Ne pas parler des dépôts « Proof Agent » / « Data Forge » comme de produits à installer : ce sont des démos de l'article.
