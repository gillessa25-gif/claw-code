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

## Vérification de sécurité (find-skills)

- Contenu : un seul fichier `SKILL.md` (Markdown), aucun script ni exécutable, aucun caractère caché (seulement — et →), aucun commentaire HTML.
- Intégrité : identique octet pour octet à `vercel-labs/skills` @ `13e4063` (2026-10-09), fichier `skills/find-skills/SKILL.md`.
- Effet : pousse l'agent à proposer `npx skills find/add`. La skill elle-même suggère `-g -y` (installation globale sans confirmation) → toujours demander avant d'installer une autre skill.
- CLI `skills` (npm 1.7.2, mainteneurs rauchg / quuu, dépôt vercel-labs/skills) : envoie une télémétrie à skills.sh (source, skills, agent détecté, version). Désactivable via `DISABLE_TELEMETRY=1` ou `DO_NOT_TRACK=1`.
- Non vérifié : le code exact du paquet npm publié n'a pas été comparé au dépôt GitHub.

## À faire / ouvert

- Rien en attente.
