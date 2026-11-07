# Lot du 05/11/2026 : Anthropic veut pouvoir prouver quel modèle d'IA a écrit une réponse (FlashProve)

## Sujet
Anthropic a publié (2 novembre 2026) un prototype de recherche, FlashProve, qui vise à permettre à n'importe qui de vérifier qu'une réponse vient bien du modèle d'IA demandé, sans connaître les réglages internes (les « poids ») du modèle. Public : débutant qui utilise un assistant IA et se demande si c'est bien le modèle annoncé qui répond.

## Pourquoi aujourd'hui
Publication de l'étude le 02/11, reprise par TechCrunch le 03/11 : c'est l'actualité IA la plus compréhensible du jour (peu de jargon une fois expliqué, enjeu simple : « est-ce bien le modèle que je paie ? »). Sujets écartés : Images 2.6 / GIF de ChatGPT (page OpenAI inaccessible depuis le cloud, seule la presse lisible, donc pas de source primaire), Uber et les agents (source primaire = résultats financiers non lus), StateBench (trop technique pour un Reel débutant), data centers et élections (politique).

## Sources
| Nom | URL | Date de publication | Type |
|---|---|---|---|
| Anthropic, « Progress on provable inference for large language models » | https://www.anthropic.com/research/provable-inference | 2026-11-02 | primaire |
| TechCrunch, « Anthropic is working on a system to prove AI models' identity » | https://techcrunch.com/2026/11/03/anthropic-is-working-on-a-system-to-prove-ai-models-identity/ | 2026-11-03 | presse |
| Code et rapport technique (liés depuis l'étude) | https://github.com/anthropics/FlashProve/ | non lu | primaire (non lu) |

Consultées le 2026-11-05. Les deux pages ont été lues via l'outil de lecture web (qui renvoie un résumé détaillé de la page, pas le HTML brut).

## Chiffres utilisés (tous tirés de la page Anthropic)
- Environ 70 à 95 fois plus long de produire la preuve que de servir la réponse normalement (mesure sur Llama 4 Maverick, une GPU H100 contre huit pour la référence vLLM : comparaison par GPU).
- Preuves couvrant des contextes jusqu'à 1 024 tokens.
- Une preuve pèse environ 19 Mo pour une requête de 1 024 tokens.
- Licence Apache 2.0.
**À revérifier sur la page avant de passer à la voix** (lecture par résumé) : ces 4 chiffres et la formulation « environ 70 à 95 fois ».

## Points incertains
- Aucune annonce de déploiement : TechCrunch écrit qu'il n'y a pas de plan pour déployer FlashProve chez Anthropic ou un autre laboratoire ; Anthropic parle d'un prototype de recherche et de « progrès intermédiaire ».
- Le test porte sur Llama 4 Maverick (modèle ouvert de Meta), pas sur Claude.
- La preuve couvre une version entière (en nombres entiers) du modèle avec décodage « greedy » (le mot le plus probable à chaque fois) ; les réponses échantillonnées ou en virgule flottante peuvent différer. Limite déclarée par Anthropic.
- Anthropic précise aussi un autre projet interne (signature du trafic d'inférence) : ne pas l'amalgamer avec FlashProve.
- Ne pas dire que c'est « inviolable » : la sécurité repose sur des hypothèses cryptographiques que les auteurs qualifient de largement admises.
