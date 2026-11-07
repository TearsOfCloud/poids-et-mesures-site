# Carrousel 4:5 (compréhension : le mécanisme et ses limites, pas une copie du Reel)

1. **Quel modèle te répond vraiment ?**
   - Une recherche d'Anthropic (3 nov. 2026) propose de le prouver.
2. **Le problème : aucun moyen de vérifier**
   - Anthropic : face à une IA, on n'a presque aucun des indices qu'on a face à un ami (voir, entendre). Juger d'après la réponse seule n'est pas fiable.
3. **Le scénario redouté**
   - Un service de routage (il redirige ta question vers un modèle) pourrait servir en douce un modèle moins cher, ou un attaquant altérer les réponses. Aucun cas observé n'est cité.
4. **L'idée : un sceau et une preuve**
   - Étape 1 : le fournisseur publie une empreinte du modèle (poids cachés). Étape 2 : chaque réponse arrive avec une preuve. Étape 3 : tu vérifies.
5. **« Sans rien révéler »**
   - La preuve ne montre pas les poids, les nombres internes du modèle. Technique : zkSNARK, une preuve courte et rapide à vérifier qui ne dévoile rien d'autre.
6. **Les chiffres, selon Anthropic**
   - Modèle testé : Llama 4 Maverick (Meta, 400 Md de paramètres). Preuve ≈ 19 Mo par requête de 1 024 jetons. Vérification ≈ 17 à 21 s sur processeur.
7. **Le prix à payer**
   - Produire la preuve coûte environ 70 à 95 fois le temps de calcul de la réponse seule.
8. **Les limites annoncées**
   - Prototype ; 1 024 jetons seulement ; modèle de type « mélange d'experts » ; code non maintenu ; aucun déploiement prévu (TechCrunch).
9. **Ce que tu peux en retenir**
   - Un nom de modèle affiché n'est pas une preuve. Si le modèle précis compte, préfère l'accès direct au fournisseur (conseil de la rédaction). Termes : jeton, paramètres, routage, zkSNARK.
