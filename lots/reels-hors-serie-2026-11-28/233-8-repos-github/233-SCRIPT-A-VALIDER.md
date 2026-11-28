# 233 — REEL « 5 outils gratuits sur GitHub : lesquels tu peux lancer sans coder ? » — SCRIPT À VALIDER
*28/11/2026. Rien de rendu : ni voix, ni images, ni montage avant ton accord.*
Format : Reel 9:16, cible ~58 s, ~150 mots dits. DA « Le surligneur » (un badge couleur par outil : vert « sans code », jaune « un peu technique », corail « technique »). Écriture orale « B améliorée v2 » (phrases courtes, points, « ... », « intelligence artificielle », pas de respelling à l'écran).

## Angle
Question posée au début, réponse tout du long : **« Sur GitHub, des milliers d'outils gratuits. Lesquels tu peux utiliser aujourd'hui, sans savoir coder ? »** Chaque outil = 1 phrase « ce que c'est » + 1 badge de difficulté. À la fin : 1 geste applicable ce soir.
Liste = les 8 dépôts déjà traités dans le projet (choix A). Plans courts (≤ 7 s), un badge qui claque à chaque outil.

## Script voix V2 (5 outils, ≈ 150 mots, ~58 s) — HORS-SÉRIE
Choix des cinq : trois « verts » qu'un débutant lance ce soir (HatchZip, Upscayl, public-apis), un « jaune » très utile (Whisper), un « corail » pour l'avertissement honnête (Cua Driver). Écartés : PhotoCraft (alpha, pas utilisable pour travailler), rembg (nuance de licence, trop pointue pour 6 s), logo-design-skill (demande un Claude avec skills, public étroit). Ils restent pour un second Reel.

**[0-5 s] HOOK**
« Sur GitHub, des milliers d'outils gratuits. Lesquels tu peux lancer sans savoir coder ? Cinq. Je les note. »

**[5-14 s] 1 · HatchZip — VERT**
« Un : HatchZip. Il ouvre un gros zip, même si ton disque est presque plein. Clic droit, extraire. »

**[14-23 s] 2 · Upscayl — VERT**
« Deux : Upscayl. Il agrandit une image. Mais il devine les détails. Un détail deviné n'est pas une preuve. »

**[23-32 s] 3 · public-apis — VERT**
« Trois : public-apis. Une liste de sources de vraies données pour ton assistant. Cherche le mot No : pas de clé. »

**[32-42 s] 4 · Whisper — JAUNE**
« Quatre : Whisper. Il transforme une voix en texte. En ligne de commande, donc plus technique. Relis toujours : il peut inventer une phrase. »

**[42-51 s] 5 · Cua Driver — CORAIL**
« Cinq : Cua Driver. Une intelligence artificielle clique à ta place. Le plus technique. Un texte piégé peut lui donner des ordres. Pas sur ta banque. »

**[51-58 s] FIN APPLICABLE**
« Ce soir, prends un vert. HatchZip, ou public-apis avec ton assistant. Liens en description. Télécharge depuis la page officielle. »

(Voix à ~2,6 mots/s. Si > 62 s : couper « Un détail deviné n'est pas une preuve ».)

## Vérifié / déduit / incertain
**Vérifié (README lus aujourd'hui, 28/11/2026, via raw.githubusercontent.com) :**
- HatchZip : gratuit, open source, Windows/macOS/Linux, appli avec clic droit « Extract here », « fits check » avant d'écrire ; exemple 180 Go → 380 Go avec un extracteur classique contre « a little over 200 Go » ; installateur non signé (Windows affiche un avertissement) ; seul site officiel hatchzip.dev, hatchzip.com sans rapport. **Mise à jour vs mon script du 24/10 :** le README cite désormais RAR et tar.zst/tar.xz comme lus.
- Upscayl : « guessing what the details could be » (FAQ), Real-ESRGAN + Vulkan, la plupart des iGPU ne marchent pas.
- public-apis : liste par catégories avec colonne Auth ; Open-Meteo et Frankfurter listés avec Auth « No ». Comptage grossier : ~1 490 lignes « | No | » (colonne Auth ET autres colonnes confondues, donc **pas citable** ; je ne cite aucun chiffre dans le script).
- PhotoCraft : « Status: early alpha » (README, badge) ; MIT OR Apache-2.0 ; « clean-room reimplementation of Adobe Photoshop » en Rust. (« not yet a Photoshop replacement for daily professional work » vu le 17/10 ; phrase exacte non relue aujourd'hui.)
- Whisper : tailles de modèles, défaut = `turbo` en ligne de commande (`whisper audio.flac --model turbo`), le turbo ne traduit pas. Hallucination : cité dans la model card (lu le 16/10).
- rembg : modèle par défaut bria-rmbg (~1,02 Go), licence BRIA « requires a paid agreement for commercial use », « weights carry their own licenses, independent of rembg's MIT license ».
- logo-design-skill : « reference library of 1,400+ real-world SVG logos », compatible Claude, Gemini CLI, Codex CLI, Cursor, Copilot (README). Marques déposées : voir TRADEMARKS.md du dépôt (vérifié le 24/10).
- Cua : README actuel décrit surtout **Cua Spaces** (appli de bureaux virtuels, Mac) en plus de Cua Driver ; Driver = « operate Calculator » en quickstart. Les 3 modes et l'injection de prompt viennent de la doc cua.ai lue le 24/10.

**Déduit (à ne pas affirmer comme fait) :**
- Les badges vert/jaune/corail = **notre classement** de difficulté, pas celui des projets. À dire « notre note ».
- « Whisper en ligne de commande = un peu technique » : déduit du README (installation `pip`, commande).

**Incertain / non vérifié :**
- Étoiles : GitHub API bloquée depuis le cloud, **aucune étoile citée** (les chiffres du 16/10 sont périmés).
- Rien n'a été installé ni testé aujourd'hui, ni HatchZip (donc « il vide l'archive » = annoncé par le projet).
- Le comportement de Cua « en arrière-plan sans voler la souris » : annoncé, pas testé.
- Cua Driver : j'ai laissé le Driver seul dans la vidéo ; le README met maintenant Spaces en premier. À confirmer que le Driver existe toujours dans la même forme (section « Cua Driver » présente dans le README).

## Décisions de Tears (28/11)
Réduit à 5 outils ; publié hors-série (non rattaché à « IA de zéro »). Légende + hashtags + EXPORT après validation du script.

## Sources
github.com/xevrion/hatchzip · upscayl/upscayl · public-apis/public-apis · storytold/photocraft · openai/whisper · danielgatis/rembg · kaankiziltug/logo-design-skill · trycua/cua (README lus le 28/11/2026).
