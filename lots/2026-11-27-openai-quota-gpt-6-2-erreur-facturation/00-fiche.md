# Lot du 27/11/2026 : OpenAI corrige une « erreur de facturation » et les quotas GPT-6.2 fondent plus vite

## Sujet
Le 26 novembre 2026, un responsable d'OpenAI a reconnu sur X une erreur de facturation faite au lancement de GPT-6.2 : l'usage de deux modèles, GPT-6.2 Astra et GPT-6.2 Sol, était décompté avec une remise qui n'aurait pas dû s'appliquer. Après correction, une même tâche consomme plus du quota de l'abonnement. D'après OpenAI : on atteint ses limites « 40 % plus vite » avec Astra et « 25 % plus vite » avec Sol. Les autres modèles ne sont pas touchés, la différence sur l'usage passé n'est pas facturée, et OpenAI ajoute une « remise à zéro mise en réserve » (banked reset) pour les abonnés Go, Plus, Pro et Business.
Deuxième information, dans la page d'aide d'OpenAI : à partir de décembre, ChatGPT et Codex partageront un quota unique pour les forfaits Plus, Pro et Business, mesuré en tokens. Les conversations en mode « Instantané » ne sont pas décomptées. Le quota restant se consulte dans Paramètres → Utilisation.
Angle débutant : comprendre ce qu'est un quota, savoir où le lire, et savoir ce qui le vide (modèle puissant, tâche complexe) plutôt que le découvrir en étant bloqué.

## Pourquoi aujourd'hui
Annonce du 26/11/2026, deux jours après l'annonce du quota partagé. Concerne tous les abonnés payants de ChatGPT. Sujet différent des lots « quota Claude » (02/11) et « Apple quotas » (10/11) : ici c'est OpenAI, une correction datée, et une page d'aide mise à jour. Jamais traité : recherche « gpt-6.2 » et « banked » dans `lots/` et `content/` sans résultat. Pas le MacBook Pro. Pas de rumeur : l'erreur est reconnue par OpenAI.

## Sources
| Nom | URL | Date | Type |
|---|---|---|---|
| Message de l'équipe ChatGPT et Codex d'OpenAI sur X (« We made a billing mistake at launch of GPT-6.2… ») | https://x.com/thsottiaux/status/2125784147889393806 | 2026-11-26 | primaire (OpenAI, point de vue de l'éditeur) |
| OpenAI Help Center, « Understanding ChatGPT and Codex usage limits » | https://help.openai.com/en/articles/20001625-understanding-chatgpt-and-codex-usage-limits | page mise à jour le 2026-11-27 (« Updated: 4 hours ago » à la lecture) | primaire |
| Numerama, « On a fait une erreur de facturation : OpenAI corrige le tir… » | https://www.numerama.com/tech/2385489-on-a-fait-une-erreur-de-facturation-openai-corrige-le-tir-et-vos-quotas-gpt-6-2-vont-fondre-jusqua-40-plus-vite.html | 2026-11-26 | presse (contexte : date de lancement du 17/11, description d'Astra et Sol) |

Consultées le 2026-11-27, pages lues en entier via curl (texte extrait).
Écartés ce jour : Character.AI et la vente de conversations (procédure judiciaire entre États et entreprise, sujet sensible pour la règle auto), jouets IA à New York (enfants), GPT-6 et protéines (biologie, préprint), Nvidia et Jensen Huang (personnes nommées, affaires), Anthropic et cours de bourse (finance), Tidal et musique IA (déjà proche d'un sujet de la veille précédente), Muse et Amazon (rumeurs de négociations).

## Faits utilisés (tous tirés des pages primaires, sauf mention)
- X, 26/11 : « billing mistake at launch of GPT-6.2 that incorrectly discounted GPT-6.2 Astra and Sol usage for most users ». Corrigé ; par rapport à la semaine dernière, limites atteintes « 40 % plus vite » avec Astra et « 25 % plus vite » avec Sol. Ces deux modèles devraient quand même aller plus loin que GPT-6 Astra et GPT-6.1 Sol (« You should still see these go further in usage compared to 6 Astra and 6.1 Sol »). Autres modèles non touchés. Pas de facturation de la différence sur l'usage passé. Un « banked reset » ajouté pour tous les abonnés Go, Plus, Pro et Business.
- Page d'aide : à partir de décembre, usage partagé entre ChatGPT et Codex pour Plus, Pro et Business ; mesuré en tokens (« les unités d'information qu'un modèle traite et génère ») ; plus le modèle est avancé et la tâche complexe, plus on consomme ; le mode Instantané ne décompte pas ; consultation dans Paramètres → Utilisation (quota restant et heures de réinitialisation) ; à la limite : attendre la réinitialisation, passer à un forfait supérieur ou acheter des crédits ; certains utilisateurs peuvent voir le changement avant décembre ; OpenAI estime que la plupart n'auront pas à attendre plus souvent qu'aujourd'hui.
- Presse (Numerama, non vérifié ailleurs) : GPT-6.2 lancé le 17 novembre ; Astra = modèle haut de gamme, Sol = déclinaison pour le travail quotidien ; reset activé pour tous les concernés selon un autre employé d'OpenAI sur X.

## Points incertains / à ne pas dire
- « 40 % plus vite » est la formulation d'OpenAI sur la vitesse d'atteinte de la limite. Ne pas la traduire en « quota réduit de 40 % » : le calcul n'est pas donné.
- La taille du quota par forfait n'est pas publiée. Aucun chiffre en messages ou en tokens.
- Où et comment on déclenche le « banked reset » : non vérifié (pas de page d'aide lue). Dire seulement qu'OpenAI l'a annoncé.
- Le forfait gratuit n'est pas cité par OpenAI dans cette annonce : ne rien dire dessus.
- Nous n'avons pas mesuré les quotas nous-mêmes. Tout vient d'OpenAI : dire « selon OpenAI ». Aucune comparaison avec d'autres assistants (non vérifiée).
- Ne pas nommer l'employé qui a publié (personne nommée).
