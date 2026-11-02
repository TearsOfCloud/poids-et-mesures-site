# Fiche : pourquoi ton quota Claude fond (le coût d'un long historique)

- **Sujet** : une société (Flamerix AI) a montré que Claude Code, l'outil de programmation d'Anthropic, renvoie tout l'historique de chaque « agent » au modèle toutes les ~30 s, juste pour écrire une étiquette de 3 à 5 mots. Anthropic confirme le mécanisme, conteste l'ampleur. On en tire le principe pour un débutant : **la longueur d'une conversation pèse sur le quota**, et trois réflexes tirés de l'aide officielle d'Anthropic.
- **Pourquoi aujourd'hui** : l'histoire est reprise par Numerama le 29/10 puis dans son récap du 01/11 ; le gist de Flamerix a été mis à jour le 02/11. Sujet tech, hors MacBook Pro, absent de `lots/` et `content/` (le mot « token » n'apparaît que dans 4 brèves, jamais en sujet).
- **Public visé** : débutant qui utilise un assistant (ChatGPT, Claude, Gemini, Le Chat) et se demande pourquoi sa limite arrive vite. Le Reel reste compréhensible sans connaître Claude Code.

## Sources (toutes lues en entier le 2026-11-02)
1. **Primaire** : Flamerix AI, « Claude Code burns ~15–20% of your tokens on a 3-word status line », gist GitHub, mis à jour le 2026-11-02 (premier état le 2026-10-28). https://gist.github.com/flamerix-ai/c3905705cc4205e5de3011fa2e74efce
2. **Primaire** : edwinarbus (se présente comme travaillant sur Claude Code), commentaire Hacker News, 2026-10-29. https://news.ycombinator.com/item?id=50284699 (lu via l'API Algolia de HN : https://hn.algolia.com/api/v1/items/50284699)
3. **Primaire** : Anthropic, « Usage limit best practices », centre d'aide, page « mise à jour cette semaine » (lue le 2026-11-02). https://support.claude.com/en/articles/9797557-usage-limit-best-practices
4. **Primaire** : Anthropic, « How do usage and length limits work? », centre d'aide (lue le 2026-11-02). https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work
5. **Presse** : Numerama, Amine Baba Aissa, « Trois mots qui brulent « 15 à 20 % » des tokens… », 2026-10-29 ; récap tech du 2026-11-01. https://www.numerama.com/tech/2363117-trois-mots-qui-brulent-15-a-20-des-tokens-ils-publient-une-astuce-pour-couper-ce-gaspillage-de-claude-code.html

## Chiffres autorisés (et d'où ils viennent)
- « toutes les ~30 secondes », « 3 à 5 mots », « historique complet » : gist (1) et commentaire Anthropic (2, « about every 30 seconds »).
- « 15 à 20 % des tokens » : **titre de Flamerix** (1). Dans son tableau : 16,4 % de la dépense Claude Code de son équipe (conversation principale : 15,7 %), 19,7 % des requêtes. À présenter comme **mesure d'une équipe qui lance beaucoup d'agents**, pas comme moyenne.
- « environ 2 % du coût au tarif public de l'API, un peu moins de 4 % des requêtes, environ 6 % dans le terminal » : Anthropic (2), semaine précédant le 29/10, utilisateurs qui envoient leur télémétrie.
- « correctif depuis la version 2.1.311 pour que ces résumés utilisent le cache » ; « un mode moins cher, avec notes courtes et petit modèle, en préparation » : Anthropic (2). Ne pas dire que c'est terminé.
- Aide Anthropic (3, 4) : la longueur de la conversation, de messages, de pièces jointes, les outils, le modèle et le niveau d'effort jouent sur l'usage ; les contenus d'un projet sont mis en cache et comptent moins quand ils sont réutilisés ; le cache expire après une période d'inactivité ; les conversations longues qui déclenchent la gestion automatique du contexte consomment plus : « essayez une nouvelle conversation » ; couper les connecteurs et la recherche web inutiles ; regrouper les questions liées en un message ; page Settings > Usage avec barres session 5 h et hebdomadaire (**plans payants**).

## Points incertains / à vérifier avant la voix
- Le libellé français de « Settings > Usage » n'a pas été vérifié dans l'interface : le Reel dit « la page Usage dans les réglages ». À contrôler sur le Mac.
- Les réflexes viennent de l'aide **Claude**. Rien n'a été vérifié pour ChatGPT, Gemini, Le Chat : le Reel et le carrousel ne disent pas que c'est identique chez eux.
- Le fait que « chaque message renvoie toute la conversation » n'est **pas** affirmé tel quel (non écrit dans les sources lues). On s'appuie sur ce que disent les sources : l'étiquette relit tout l'historique, l'aide dit que la longueur compte.
- Flamerix vend des services d'IA (flamerix.ai) : intérêt possible à publier ce chiffre. Anthropic n'a pas vu la télémétrie de Flamerix (il propose d'enquêter).
- Le script de Flamerix : **ne pas le recommander** (code tiers, modifie le fonctionnement d'un outil, son auteur dit qu'une mise à jour peut l'annuler sans avertir, et ses conditions d'usage ne sont pas vérifiées).
- Numerama écrit « Anthropic évalue son coût à 2 % » ; la source dit « cost at API list prices » : formulation du Reel : « environ 2 % du coût ».
