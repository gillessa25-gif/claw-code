# SAUVEGARDE – à relire à chaque nouvelle session

Dernière mise à jour : 2026-10-19

## Préférences utilisateur
- Tenir ce fichier à jour et le relire au début de chaque session.
- Ne jamais valider mes affirmations sans les vérifier ; privilégier les preuves.
- Me contredire clairement si je me trompe.
- Dire « je ne sais pas / je ne peux pas vérifier » plutôt qu'inventer.

## Sujet en cours : revue des automatisations Instagram
- Statut : cadrage, aucune implémentation.
- Fait vérifié (2026-10-19) : une recherche « instagram » (insensible à la casse) dans le dépôt `claw-code` ne renvoie AUCUN fichier. Le dépôt est un workspace Rust (CLI/runtime) sans code Instagram.
- À déterminer : où vivent les automatisations (Zapier ? autre outil ? autre dépôt ?). Le connecteur Zapier a échoué à se connecter dans cette session (403 proxy).

## Vérification 2026-10-19 : « Claude fait Instagram chaque jour + TikTok programmé » (affirmation de l'utilisateur)
Résultat : NON CONFIRMÉ par les preuves accessibles.
- `list_triggers` (toutes pages, 17 routines au total vues sur 2 pages) : routines LinkedIn Promylaia (actives : Actions du jour, Manager hebdo, Veille, Daily Post, reply drafts), 2 routines YouTube « Hooded Lifter » (désactivées), 2 routines LinkedIn anciennes (désactivées). AUCUNE routine Instagram, AUCUNE routine TikTok. (« TikTok » n'apparaît que comme style de sous-titres dans le prompt YouTube.)
- Session « Format adaptation Instagram Pinterest TikTok » (2026-09-13/14) : seuls 54 derniers événements lus ; ils concernent une app web (naiom-platform), avec un simple exemple de prompt « hooks Instagram ». Pas de preuve d'automatisation publiée. Début de session non lu.
- Limites : connecteur Zapier KO dans cette session (403) → Zaps éventuels non vérifiables ; je n'ai pas de mémoire des sessions passées.
- Idée à vérifier : demander à l'utilisateur le nom de la routine/Zap, ou une capture.

## Zapier MCP (vérifié 2026-10-19, outils mcp__Zapier__ fonctionnels dans cette session)
- Apps activées : YouTube, Gmail, Google Drive, Todoist, ElevenLabs, LinkedIn. AUCUNE app Instagram ni TikTok activée → aucune automatisation Instagram/TikTok possible via ce Zapier MCP actuellement.
- Skills Zapier enregistrés : onboarding, mcp-roast, hooded-lifter-content-readiness-brief. Rien sur Instagram/TikTok.
- Catalogue (non activé) : « Instagram for Business » (2 lectures, 3 écritures) ; TikTok = seulement Lead Generation et Conversions (pub), PAS de publication de vidéos.
- Limite : ce MCP n'expose pas la liste des Zaps classiques de l'éditeur Zapier.
