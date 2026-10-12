# Sauvegarde de session

Fichier à relire au début de chaque nouvelle session.

## 2026-10-12 — branche `claude/vercel-labs-skills-setup-n330rl`

- Commande demandée : `npx skills add vercel-labs/skills --skill find-skills`
- Exécutée en mode non interactif : `npx -y skills@latest add vercel-labs/skills --skill find-skills -a claude-code -y`
- Résultat vérifié :
  - `.claude/skills/find-skills/SKILL.md` (copie, pas de lien symbolique ; Markdown seul, aucun script)
  - `skills-lock.json` (source `vercel-labs/skills`, hash `913b9d37…c396`)
- Installation au niveau projet (pas `-g`) : la skill n'est chargée que dans ce dépôt.
- Remarque : la skill s'appuie sur `npx skills find` et sur https://skills.sh/ ; elle demande de vérifier le nombre d'installations et la source avant de recommander une skill.

## À faire / ouvert

- Rien en attente.
