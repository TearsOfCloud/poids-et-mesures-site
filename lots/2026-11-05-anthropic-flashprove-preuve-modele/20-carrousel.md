# Carrousel 4:5, 8 slides (analyse, pas une copie du Reel)

Ordre : problème, mécanisme, ce que ça prouve et ne prouve pas, limites mesurées, quoi retenir. Sources en pied de slide.

1. **Titre :** Qui t'écrit vraiment ?
   **Corps :** Anthropic propose un moyen de prouver quel modèle d'IA a produit une réponse. Prototype de recherche, 2 novembre 2026.
2. **Titre :** Le problème : tu ne vois pas le moteur
   **Corps :** Une réponse ne porte pas la signature de son modèle. Selon Anthropic, un service intermédiaire pourrait en glisser un moins cher sans que ça se voie.
3. **Titre :** L'empreinte du modèle
   **Corps :** Le fournisseur publie un code court qui correspond à un seul modèle précis. Les réglages internes (les « poids ») restent secrets.
4. **Titre :** La preuve, réponse par réponse
   **Corps :** Pour une réponse donnée, il produit une preuve mathématique. Toute personne qui a l'empreinte peut la vérifier sans le modèle. Comparaison de TechCrunch : une signature d'e-mail.
5. **Titre :** Ce que ça prouve
   **Corps :** Que la réponse vient du modèle dont l'empreinte est publiée, pas d'un autre. Pas que la réponse est juste : un bon modèle peut se tromper.
6. **Titre :** Ce que ça coûte, mesuré
   **Corps :** Test sur Llama 4 Maverick (modèle ouvert de Meta, pas Claude) : preuve environ 70 à 95 fois plus longue à produire que la réponse. Une preuve pèse environ 19 Mo pour 1 024 tokens.
7. **Titre :** Les limites annoncées
   **Corps :** Textes courts (1 024 tokens maximum), un seul type de décodage, architecture non cachée. Selon TechCrunch, aucun déploiement n'est prévu.
8. **Titre :** Ce que tu peux faire déjà
   **Corps :** Regarde le modèle affiché par ton assistant et note-le quand un résultat compte. Pour une décision importante, compare avec un second assistant. Source : Anthropic, TechCrunch.

Glossaire en pied de slide 3 ou 6 : token = petit morceau de mot que l'IA compte ; poids = réglages internes d'un modèle ; décodage = façon de choisir le mot suivant.
