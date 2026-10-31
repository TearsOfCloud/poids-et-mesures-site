# Guide du lot quotidien (consignes de la tâche « Lot du jour »)

Objectif : produire chaque jour **1 sujet complet**, prêt à être traité en lot sur le Mac (voix Kore, vidéo 9:16, images). Cette tâche **ne publie rien** et ne touche ni aux réseaux ni à `content/`. Elle écrit uniquement dans `lots/AAAA-MM-JJ-mots-cles/`. Tears valide ; aucune publication sans son accord écrit.

## Choix du sujet (1 par jour)
- IA **ou** tech générale (pas seulement l'IA), d'actualité. Lire les brèves du jour (`content/breves/`) et `veille/candidats.json`, ou un sujet de base non périssable si rien de solide.
- Interdits : sujets déjà traités (voir `lots/` et `content/`), le MacBook Pro (déjà fait), rumeurs, sujets sensibles (santé, justice, élections, personnes nommées).
- Source primaire lue en entier, comme pour les brèves. Aucun chiffre ni citation sans source.

## Contenu du dossier du lot
1. `00-fiche.md` : sujet, pourquoi aujourd'hui, sources (nom, URL, date, type), points incertains.
2. `10-script-reel.md` : script oral FR 9:16, **80 s max** (≈190 mots dits), accroche honnête (pas de faux hook), exemple concret, test ou résultat réel quand il existe, une info **applicable tout de suite** dans le workflow du spectateur, chaque terme expliqué, tout se comprend seul. Français oral naturel, pas de traduction de l'anglais. Format : tableau scène | voix off | visuel à l'écran | durée.
3. `20-carrousel.md` : 6 à 9 slides 4:5, texte exact par slide (titre ≤ 8 mots, corps court). Différent du Reel : analyse et compréhension, pas une copie.
4. `30-texte-x.md` : fil X de 3 à 5 posts, ≤ 280 caractères chacun, texte seul.
5. `40-legendes.md` : légende Instagram, TikTok, YouTube Shorts (titre ≤ 70 caractères).
6. `50-brief-images.md` : une entrée par image nécessaire (objet seul, fond blanc uni, carré, sans texte, marque, personne ni main), 5 images maximum, avec nom de fichier prévu. Style : `DA-KIT-POSTS/00-DA-FIGEE.md` (côté Mac).
7. `99-statut.json` : `{"statut":"a-traiter","etape":"textes","images":"a-generer","voix":"a-generer","video":"a-faire"}`. Le Mac met à jour `etape` après chaque étape.

## Règles
- Ordre des assistants dans toute comparaison : ChatGPT, Claude, Gemini, Le Chat.
- Pas de « enregistre ce post » sur une actualité périssable.
- Pas de fichier `.mp4`, `.jpg` ni clé dans ce dossier : seulement du texte.
- Une pull request « Lot du JJ/MM » vers `Main`. Ne jamais fusionner soi-même. Si aucun sujet ne passe : pas de PR, une ligne pour le dire.
