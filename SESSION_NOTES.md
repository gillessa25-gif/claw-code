# Sauvegarde de session (à relire au début de chaque session)

## Préférences utilisateur
- Ne jamais valider ses affirmations sans vérification ; preuves avant approbation.
- Le contredire clairement s'il se trompe ; dire "je ne sais pas / non vérifiable" plutôt qu'inventer.

## Historique
- 2026-10-14 : skill `arena` (https://github.com/Jakeschincariol/arena-skill, MIT) installé dans
  ~/.claude/skills/arena (copie du dossier skills/arena). Code relu : pas d'appel réseau ni subprocess.
  Note : ~/.claude est dans le conteneur cloud éphémère ; à réinstaller si nouvelle session.
- 2026-10-14 : 11 skills yt-* (https://github.com/Jakeschincariol/chatgpt-youtube-agent-skill, MIT) copiés dans
  ~/.claude/skills. Conçus pour ChatGPT/Codex (chemin voix ~/.codex/youtube/voice.md) ; compatibilité Claude Code
  non testée. Pas d'appel réseau/subprocess détecté par grep.
- 2026-10-14 : chemins ~/.codex/youtube remplacés par ~/.claude/youtube dans les SKILL.md yt-* ; modèle de voix copié
  dans ~/.claude/youtube/voice.md (à remplir par l'utilisateur).
- 2026-10-14 : transcription fournie par l'utilisateur (vidéo KyC8r-zitVE, "addictive storytelling") résumée en skill
  ~/.claude/skills/story-loop (stakes / big question / head fake / rehook). YouTube inaccessible depuis le proxy.
