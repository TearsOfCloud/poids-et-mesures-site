# Lot du 11/11/2026 : « Toute personne avec le lien » : les apps créées avec l'IA sont-elles vraiment privées ?

## Sujet
Le 10 novembre 2026, la société de sécurité Claroc a publié une étude : sur 43 551 adresses d'apps créées avec l'assistant Grok (mode « Build ») qu'elle a testées, 35 578 (94,7 % des apps encore en ligne) s'ouvraient pour n'importe qui, sans connexion. Angle débutant : comprendre qu'un lien « secret » n'est pas un cadenas, et en tirer un réflexe applicable tout de suite à toute app ou page publiée avec un outil d'IA : vérifier le réglage de partage, ouvrir le lien en navigation privée, ne jamais y mettre de données réelles ni de mots de passe.

## Pourquoi aujourd'hui
Étude publiée le 10/11 (Claroc), relayée le 10/11 par Ars Technica. Vaut pour tout débutant qui commence à « créer une petite app en décrivant ce qu'on veut » (Lovable, Replit, Bolt, ChatGPT, Gemini, Grok...). Sujet jamais traité dans `lots/` ni `content/` (le lot du 07/11 parle de Meta Muse et de ses mini-apps, pas de ce risque ; Grok n'apparaît nulle part).

## Sources
| Nom | URL | Date de publication | Type |
|---|---|---|---|
| Claroc, « Grok Apps Exposed xAI Secrets and Private Data » | https://blog.claroc.io/ghostshares-grok-build-apps/ | 2026-11-10 (la page indique 8 nov. pour le début des tests ; date exacte de mise en ligne à confirmer) | primaire (étude d'un éditeur de sécurité qui vend ses services : intérêt commercial) |
| Ars Technica (Dan Goodin), « Grok Build coding agent leaks oodles of confidential info, some belonging to SpaceXSI » | https://arstechnica.com/security/2026/11/grok-build-coding-agent-leaks-oodles-of-confidential-info-some-belonging-to-spacexsi/ | 2026-11-10 | presse (recoupe, ajoute la réponse de l'entreprise) |

Consultées le 2026-11-11, pages lues en entier via curl.

## Faits utilisés (tous tirés de la page Claroc, sauf mention)
- Méthode : Claroc a listé les noms d'apps sous grok.me avec des techniques classiques de découverte de sous-domaines (43 601 noms), a essayé 43 551 adresses, ouvert chaque première page une fois, sans se connecter. 37 571 étaient encore en ligne ; 35 578 (94,7 %) s'ouvraient pour tout le monde ; 1 993 (5,3 %) répondaient par une erreur 401 (réglage « Only you » ou « Invited users »).
- Contenu : la plupart des apps ouvertes sont des jeux, pages d'accueil et calculatrices. Environ 1 sur 10 contenait des données internes d'entreprise ou personnelles ; environ 2 % du matériel jugé grave ou critique (estimation de Claroc, vérifiée par échantillon). Claroc estime à 650-800 le nombre d'apps avec des données privées.
- Réglage par défaut : dans le compte payant que Claroc a utilisé, au moment de publier, « Anyone with the link » était présélectionné, à côté de « Invited users » et « Only you ». Rien ne devient public avant que l'utilisateur clique sur Publier (Claroc le reconnaît).
- Réponse de SpaceXSI (via Claroc et Ars) : les apps sont privées jusqu'à ce que leur créateur choisisse de les partager ; publier demande plusieurs étapes ; les comptes d'employés sont réglés sur « Only you » par défaut. Un représentant de Cursor (propriétaire de la plateforme selon Ars) dit que les apps sont privées par défaut ; les tests de Claroc contredisent ce point pour les comptes ordinaires. Ars écrit que les autres outils (ChatGPT, Lovable, Bolt) proposent aussi des liens partageables.
- Pourquoi c'est trouvable : chaque app publiée a sa propre adresse (nom.grok.me). Quand quelqu'un l'ouvre, son ordinateur interroge un annuaire d'adresses (DNS) ; des services d'archives de ces requêtes (« passive DNS ») les conservent, et n'importe qui peut les rechercher. Un lien avec 4 mots aléatoires n'est donc pas « secret » dans ce cas.
- Comparaison faite par Claroc : dans son test, l'app publiée via ChatGPT était réglée sur « Only me » jusqu'à ce qu'on change ; ses adresses restent trouvables de la même façon, mais mènent à une app que seul le propriétaire ouvre. Les conversations partagées de Claude (artifacts publiés), ChatGPT et Gemini placent la partie secrète du lien dans le chemin (après le nom de domaine), que le DNS ne voit pas. Claroc précise qu'un chemin n'est pas privé non plus : en août 2025, plus de 370 000 conversations Grok partagées sont apparues dans Google.
- Test sur ses propres apps (données fictives) : une app « liste de contacts » créée sans demander de connexion laissait n'importe quel visiteur ajouter une ligne ; une app « équipe de 4 personnes » avec connexion Google laissait un compte Google quelconque lire, modifier et supprimer des enregistrements (test mené uniquement sur ses propres apps).
- 24 apps ouvertes avaient été créées par le personnel de SpaceXSI et X ; elles ont été retirées après le signalement ; pas celles des autres utilisateurs (selon Claroc). Claroc écrit n'avoir ni signé, ni soumis de formulaire, ni utilisé de mot de passe vu, et cache les noms d'organisations.

## Points incertains / à ne pas dire
- Tous les chiffres sont ceux de Claroc, société qui vend de la sécurité d'apps : « selon Claroc ». Aucune vérification indépendante lue. L'estimation « 2 % graves » et « 650-800 » vient d'un modèle d'IA vérifié par échantillon, donc approximative.
- Ne pas affirmer que les apps des autres outils sont aussi exposées : seul Grok a été mesuré à grande échelle. Claroc dit seulement que d'autres outils donnent aussi une adresse par app, donc l'adresse est trouvable de la même façon.
- Ne pas citer de données personnelles, de santé, ni d'entreprises tierces (la source les décrit par type, nous aussi). Ne pas nommer de personne. Le Chat (Mistral) : non couvert par la source.
- « SpaceXSI » : nom donné par les deux sources pour l'entreprise issue de la fusion SpaceX et xAI.
