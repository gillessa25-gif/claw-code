# SAUVEGARDE — Vidéo hype Promylaia 30 s

> Fichier de reprise : relire en début de chaque nouvelle session avant de toucher à la vidéo.
> Dernière mise à jour : 2026-10-21.

## État
- ✅ 3 vidéos rendues et vérifiées (30,00 s, 30 i/s, 900 images, H.264 + AAC, crête audio −2 dBFS, aucune saturation) :
  - `out/promylaia-hype-9x16.mp4` (1080×1920 : Reels, TikTok, Shorts, Stories)
  - `out/promylaia-hype-1x1.mp4` (1080×1080 : fil LinkedIn ou Instagram)
  - `out/promylaia-hype-16x9.mp4` (1920×1080 : LinkedIn, YouTube, site)
- ❌ Rien n'a été publié. Le repo `promylaia-reels` (publication automatique depuis `main` via `schedule.json`) n'a **pas** été modifié.

## Sources utilisées (vérifiées dans les repos)
- `Websits/promylaia/` (export du site en ligne) : textes, agents, offres, logo, polices Space Grotesk + Inter.
- `Websits/promylaia/llms.txt`, `pricing.md` : offres, « déploiement 1 à 2 semaines » (agent plug & play).
- `Websits/linkedin-assets/EDITORIAL_STRATEGY.md` : positionnement « Nous ne vendons pas de l'IA. Nous supprimons du travail inutile. », cible PME, vouvoiement, aucun chiffre inventé.
- `Websits/CLAUDE.md` : palette officielle (#17123a, #241c55, #5b3df5, #e0dcf7, #ece9fa, #f6f5fb, #ff6a4d).

## Choix volontaires (garde-fous)
- **Aucun chiffre client, aucun témoignage, aucun logo client** : le site lui-même indique que les témoignages et logos sont fictifs et que les compteurs (+40 agents, +22 clients…) sont des objectifs non constatés. Le « +30 % de temps gagné » du site n'est pas utilisé non plus (non vérifiable).
- Seul chiffre utilisé : « 1 à 2 semaines » pour un agent plug & play (pricing.md + llms.txt).
- **Rôles des agents : ceux du site en ligne** (Kai Commercial, Nova Créatrice de contenu, Zeno Support client, Yuki Coordinatrice RH, Raiden Setter & Closer, Vega Assistante de direction).
  ⚠️ Conflit non résolu : `linkedin-assets/README.md` attribue d'autres rôles (Nova = Support, Vega = Devis & Facturation, Yuki = Organisation, Zeno = RH, Raiden = Reporting & CRM). À trancher avec Gilles.
- Domaine affiché : promylaia.fr (sitemap + llms.txt).

## Script (FR) et techniques, calés sur une musique à 120 BPM
| Temps | Écran | Technique |
|---|---|---|
| 0–2 s | « STOP » puis « au travail inutile. » | Accroche dès la 1re image : flash corail, slam + tremblement, soulignement |
| 2–8 s | ENCORE À LA MAIN ? Les relances · Les devis · La saisie · Le tri des e-mails · Les plannings · Le reporting | Typo cinétique, 1 corvée par seconde, barrée sur le contretemps, fond qui change à chaque coupe |
| 8–10 s | « Et si tout ça se faisait tout seul ? » : 6 tuiles fusionnent en un point | Jeu de formes (carrés → cercle → point indigo du logo) |
| 10–12 s | « Nous ne vendons pas de l'IA. » | Breakdown, poussée caméra lente, point qui pulse |
| 12–14 s | « Nous supprimons du travail inutile. » | Drop : le point explose en volet circulaire indigo, rotation caméra |
| 14–20 s | « Des agents IA qui travaillent pour vous. » + Kai, Nova, Zeno, Yuki, Raiden, Vega → « 6 agents. Chacun son métier. » | Travelling caméra, mise au point par agent, dézoom final |
| 20–24 s | Plug & play · Sur mesure · Branchés sur vos outils · Un agent opérationnel en 1 à 2 semaines | 4 changements de couleur, 4 volets différents (cercle, diagonale, ouverture, coin) |
| 24–27 s | « Moins de corvées. Plus de croissance. » | Barré, puis plongée caméra dans le point final |
| 27–30 s | Logo qui se dessine, Promylaia, « Nous supprimons du travail inutile. », « Réservez un appel · promylaia.fr » | Le point devient celui du logo ; image fixe et lisible à partir de 28,8 s |

## Refaire / modifier
```bash
cd promylaia-hype
python3 music.py out/music.wav               # bande-son synthétisée (aucune licence tierce)
node render.cjs v,s,h                        # rendu complet (~5 min pour les 3 formats)
node render.cjs v --stills 0,12.5,29.5       # images de contrôle -> out/stills/
```
- Tout le visuel est dans `index.html` (`render(t)` = fonction pure du temps, une section par scène).
- Textes : chercher la phrase dans `index.html` et la modifier ; les tailles s'ajustent seules (`fit`).

## Pistes non faites / à valider
- Pas de voix off (non demandée). Musique synthétique maison, aucun droit à gérer ; elle n'a pas été écoutée par un humain : à valider à l'oreille.
- Pas de sous-titres nécessaires : tout le message est déjà à l'écran.
- Zone de sécurité Reels : contenu clé entre ~11 % et ~76 % de la hauteur en 9:16 (la légende Instagram couvre le bas).
