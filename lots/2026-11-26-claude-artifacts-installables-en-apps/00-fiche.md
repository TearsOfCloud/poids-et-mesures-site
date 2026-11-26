# Lot du 26/11/2026 : Claude peut transformer ce qu'il construit en vraie application de bureau

## Sujet
Le 24 novembre 2026, Anthropic a ajouté en bêta une fonction : un « artifact » (la petite appli ou page que Claude construit dans la conversation) peut être installé comme une application sur Mac ou Windows. Elle a sa propre fenêtre et son icône, s'ouvre comme n'importe quelle appli, et peut demander des droits (notifications, élément dans la barre de menus, raccourcis clavier, etc.). Angle débutant : tu décris un petit outil en une phrase, tu l'obtiens sous forme d'appli, sans écrire de code. Et un réflexe de sécurité : refuser par défaut le niveau de droits le plus haut (« accès complet à l'ordinateur »).

## Pourquoi aujourd'hui
Entrée datée du 24/11/2026 dans les notes de version officielles de Claude, relayée le même jour par la presse spécialisée. Sujet jamais traité dans `lots/` ni `content/` (recherche « artifact » : seulement des mentions des artifacts publiés/partagés dans le lot du 11/11, pas cette fonction). Pas de rumeur, pas de personne nommée dans nos textes. Ce n'est pas le MacBook Pro.

## Sources
| Nom | URL | Date | Type |
|---|---|---|---|
| Claude Help Center, « Install an artifact as an app » | https://support.claude.com/en/articles/18516354-install-an-artifact-as-an-app | non datée sur la page (annoncée le 2026-11-24 dans les notes de version) | primaire (documentation de l'éditeur : point de vue d'Anthropic) |
| Claude Help Center, notes de version, entrée du 24 novembre 2026 « Install artifacts as apps (beta) » | https://support.claude.com/en/articles/12138966-release-notes | 2026-11-24 | primaire |
| The Decoder, « Anthropic turns Claude Artifacts into standalone desktop apps for macOS and Windows » | https://the-decoder.com/anthropic-turns-claude-artifacts-into-standalone-desktop-apps-for-macos-and-windows/ | 2026-11-24 (date donnée par la veille ActuIA du 25/11) | presse (contexte seulement, aucun chiffre repris) |

Consultées le 2026-11-26, pages lues en entier via curl (texte extrait). Écartés ce jour-là : Tidal et les titres 100 % IA, jouets IA à New York (sujet lié aux enfants, sensible), GPT-6 et protéines (santé/biologie, préprint), Muse dans les messages Instagram (Muse déjà traité les 07/11), Free « Traduction Live » (réservé à un forfait, utile à très peu de lecteurs), rumeurs sur des modèles « trop puissants » (Axios via The Decoder : sources anonymes).

## Faits utilisés (tous tirés des pages primaires, rien de mémoire)
- Un artifact que Claude crée peut s'installer comme appli sur Mac ou Windows : fenêtre et icône propres, s'ouvre comme une autre appli. Les fonctions « Ajouter au Dock / à l'écran d'accueil » d'un navigateur ne font qu'un raccourci, sans ces fonctions.
- Disponibilité : bêta, forfaits Free, Pro, Max, Ultra, Team, Enterprise. Il faut Claude pour Mac ou Windows, version 6.28899.0 ou plus récente. Team : activé par défaut, mais le niveau « accès complet » est désactivé tant qu'un admin ne l'active pas. Enterprise : fonction désactivée jusqu'à ce qu'un propriétaire l'active.
- Pas disponible : Linux, web, mobile. Les artifacts issus de modèles (Docs, Slides, Sheets) ne s'installent pas.
- Exemples de demandes donnés par la page : un minuteur Pomodoro dans la barre de menus ; une petite appli Mac qui rappelle de s'étirer toutes les heures ; une appli Windows qui renomme par date les photos d'un dossier.
- Installation : ouvrir l'artifact dans la fenêtre principale de Claude Desktop, menu du titre ou clic droit → « Install as app », puis confirmer. Aussi dans Partager. Si l'option manque : mettre Claude Desktop à jour.
- C'est le même artifact : si tu (ou un autre éditeur) le modifies, l'appli change aussi. Pour l'ouvrir, il faut être en ligne et connecté à Claude Desktop.
- Droits : l'appli doit demander avant chaque fonction : notifications ; raccourcis clavier ; flotter au-dessus des autres fenêtres (et lire la position de la souris) ; élément dans la barre de menus (Mac) ou icône de la zone de notification (Windows) ; accès complet à l'ordinateur (lancer des programmes, lire, modifier ou supprimer des fichiers sans redemander). Un « Autoriser » ne vaut que pour une version de l'appli : après toute mise à jour, y compris tes propres modifications, Claude redemande. Un « Ne pas autoriser » reste valable jusqu'à ce que tu le changes. On peut retirer un droit : nom de l'appli dans la barre de menus → Permissions (Mac) ; clic droit sur la barre de titre → Permissions (Windows) ; ou Fichier → Apps dans Claude Desktop.
- Avertissement de la page : « Anthropic doesn't review apps before you install them » (Anthropic ne vérifie pas les applis avant installation). Pour l'accès complet : ne l'autoriser que si l'on fait confiance à tous ceux qui ont écrit l'appli. Claude n'autorise généralement pas une demande d'accès complet si quelqu'un d'extérieur à l'organisation a écrit une partie de l'appli ou si l'auteur n'est pas confirmé. Si une appli charge du code d'un autre site, ce code peut changer sans nouvelle demande.
- Désinstaller : Fichier → Apps → choisir l'appli → Uninstall. Sur Mac l'appli va à la corbeille. Désinstaller retire les droits accordés mais ne supprime pas l'artifact.
- Limites d'usage : construire l'appli et ses requêtes à Claude comptent dans les limites du forfait.

## Points incertains / à ne pas dire
- C'est une bêta : le comportement peut changer. Dire « en bêta » à l'oral.
- La page d'aide ne chiffre rien (ni nombre d'utilisateurs, ni durée, ni coût). Ne rien promettre. Ne pas reprendre de chiffres de la presse.
- Le texte de la presse parle d'exemples comme « terminaux personnalisés, gestionnaires de fichiers, éditeurs vidéo » : c'est la presse qui les cite, non testé par nous. Ne pas les promettre.
- Nous n'avons pas testé la fonction nous-mêmes (aucun accès à l'app Claude Desktop ici). Ne pas écrire « on l'a testé ».
- Source primaire = Anthropic, qui vend Claude : dire « selon la documentation d'Anthropic ». Ne pas affirmer que ChatGPT ou Gemini n'ont pas d'équivalent (non vérifié).
- Ne pas nommer l'employé qui a présenté la fonction sur X (source presse, personne nommée).
