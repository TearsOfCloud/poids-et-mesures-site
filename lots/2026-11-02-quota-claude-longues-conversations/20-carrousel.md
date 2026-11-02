# Carrousel 4:5 (compréhension : le mécanisme et les limites, pas une copie du Reel)

1. **Pourquoi ton quota fond** : le coût d'un long historique
   - Un cas de la semaine, trois enseignements.
2. **Le cas** : une étiquette de 3 à 5 mots
   - Claude Code (outil de programmation d'Anthropic) fait écrire à l'IA un court résumé de ce que fait chaque agent, environ toutes les 30 s.
3. **Le coût caché** : tout l'historique est relu
   - Pour écrire 3 à 5 mots, l'outil renvoie tout l'historique de l'agent. Plus l'agent travaille, plus chaque étiquette coûte.
4. **Deux mesures, deux chiffres**
   - Flamerix (une équipe, beaucoup d'agents) : 16,4 % de sa dépense. Anthropic (moyenne des utilisateurs qui envoient leur télémétrie) : ≈ 2 % du coût, ≈ 6 % dans le terminal.
5. **Ce qui est établi** : le mécanisme
   - Les deux camps sont d'accord sur le mécanisme. Un correctif (version 2.1.311) utilise le cache ; un mode moins cher est en préparation.
6. **Ce que ça t'apprend** : la longueur compte
   - L'aide d'Anthropic liste ce qui pèse sur ton usage : longueur de la conversation, pièces jointes, outils, modèle, niveau d'effort.
7. **3 réflexes** : applicables aujourd'hui
   - Nouveau sujet = nouvelle conversation. Questions liées = un seul message. Connecteurs et web inutiles = coupés.
8. **Le cache, en une phrase**
   - Un projet garde tes documents en cache : les réutiliser compte moins. Mais le cache expire après une pause : le premier message compte plein tarif.
9. **Limites et réflexe de lecteur**
   - Source des réflexes : l'aide de Claude ; pas vérifié pour ChatGPT, Gemini ou Le Chat. Un chiffre choc vient souvent d'un seul cas : demande « sur quoi, mesuré par qui ? ». Termes : token, agent, cache, quota.
