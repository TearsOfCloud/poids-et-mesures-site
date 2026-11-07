# Fiche : comment prouver quel modèle d'IA t'a répondu (FlashProve, Anthropic)

- **Sujet** : le 3 novembre 2026, Anthropic publie une recherche et un code libre, FlashProve, qui permet à un fournisseur d'IA de joindre à chaque réponse une **preuve cryptographique** que la réponse vient bien d'un modèle précis, sans révéler ses « poids » (les nombres internes du modèle). Aujourd'hui, un utilisateur ne peut pas vérifier le modèle qui lui répond.
- **Pourquoi aujourd'hui** : annonce du 03/11 (TechCrunch le même jour). Sujet IA, absent de `lots/` et `content/` (aucune occurrence de FlashProve ni de « preuve d'inférence »), hors MacBook Pro. Public visé : débutant qui utilise un assistant et se demande ce qu'il y a derrière le nom affiché. Le Reel se comprend sans connaître la cryptographie.
- **Ce n'est pas** : un outil que le spectateur peut utiliser. Le lot le dit franchement ; l'info applicable est un réflexe de lecteur (voir plus bas), signalé comme conseil de la rédaction.

## Sources (lues en entier le 2026-11-04)
1. **Primaire** : Anthropic (Rinberg, Allain et al.), « Progress on provable inference for large language models », page de recherche, mise en ligne autour du 2026-11-03 (la page cite des mises à jour du 19/10 ; date exacte de première publication non affichée dans le texte lu). https://www.anthropic.com/research/provable-inference
2. **Primaire** : dépôt GitHub anthropics/FlashProve, README (version 0.16.0, « research artifact : not maintained, not accepting contributions », licence Apache 2.0). https://github.com/anthropics/FlashProve/
3. **Presse** : TechCrunch, Russell Brandom, « Anthropic is working on a system to prove AI models' identity », 2026-11-03. https://techcrunch.com/2026/11/03/anthropic-is-working-on-a-system-to-prove-ai-models-identity/

## Chiffres autorisés (tous de la source 1 sauf mention)
- Modèle testé : Llama 4 Maverick (modèle de Meta), 400 milliards de paramètres, version « 4 bits » publique ; environ 17 milliards utilisés par jeton (architecture « mixture of experts »).
- Un seul GPU H100 : environ 110 tokens par seconde pour produire les preuves ; preuve d'environ 19 Mo (18,78 Mo mesuré) pour une requête de 1 024 tokens.
- Vérification : 17 s sur 24 threads, 21 s sur un seul thread, sur CPU ordinaire, sans GPU ; le client télécharge une « empreinte » (commitment) d'environ 6,5 Mo.
- Surcoût : environ 72 fois le temps GPU de vLLM (66 à 77 selon les essais), 94 fois à charge maximale. Le billet dit « environ 70 à 95 fois ».
- Contexte maximal prouvé : 1 024 tokens.
- Objectifs cités par Anthropic : vérifier qu'un modèle n'a pas été remplacé en douce (par un service de routage, « pour des raisons de coût »), détecter une falsification du flux de réponses, aider les évaluateurs indépendants, prouver qu'un modèle a bien analysé quelque chose.
- Étape « jamais déployé » : TechCrunch écrit « no plans to deploy it at Anthropic or any other lab » ; le billet dit « intermediate progress, not a completed research agenda ».

## Points incertains / à ne pas affirmer
- **Aucune source ne dit que des fournisseurs remplacent aujourd'hui un modèle par un autre.** Le billet décrit un risque et un besoin, pas des cas observés. Le Reel dit « pourrait », jamais « ça arrive ».
- Les chiffres de performance sont **ceux d'Anthropic**, sur un seul modèle (Llama 4 Maverick, pas Claude). Aucun tiers ne les a mesurés dans les sources lues. Dire « selon Anthropic ».
- Le billet dit que la preuve porte sur une version « entière » (en nombres entiers) du modèle avec décodage « glouton » ; une réponse produite autrement pourrait ne pas coller. Ne pas promettre que ça marcherait sur n'importe quelle réponse de chatbot.
- Le billet mentionne un projet séparé d'Anthropic (signature du trafic + recalcul sur serveur de confiance) et le changement de nom « inference verification » (note du 19/10). Non développé dans le lot.
- Le conseil « passer par le fournisseur officiel quand le modèle précis compte » est un **réflexe de rédaction**, déduit du scénario « routage par un tiers » du billet ; ce n'est pas une recommandation d'Anthropic.
- Prononciation à contrôler avant la voix : « FlashProve » (« flache-prouve »), « Llama » (« lama »).
