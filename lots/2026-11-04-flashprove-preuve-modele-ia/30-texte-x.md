# Fil X (texte seul)

1/ Comment savoir que l'IA qui te répond est bien le modèle annoncé ? Aujourd'hui, tu ne peux pas le vérifier : Anthropic écrit que juger d'après la réponse seule n'est pas fiable. Elle publie FlashProve, une piste pour le prouver.

2/ Le principe : le fournisseur publie une empreinte du modèle, comme un sceau, puis joint une preuve à chaque réponse. Tu vérifies sans voir les poids (les nombres internes du modèle), sur un processeur ordinaire, en 17 à 21 s selon Anthropic.

3/ Le coût, selon Anthropic, testé sur Llama 4 Maverick (Meta, 400 Md de paramètres) : ≈ 19 Mo de preuve pour 1 024 jetons, et environ 70 à 95 fois le temps de calcul de la réponse. Un jeton = un petit morceau de texte.

4/ Limites : prototype, 1 024 jetons seulement, aucun déploiement prévu (TechCrunch). Aucune source ne dit que des fournisseurs changent de modèle en douce aujourd'hui. Réflexe : un nom affiché n'est pas une preuve. Source : anthropic.com/research/provable-inference
