# Module de Synthèse Métaphysique

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.x-3776ab)](scripts/)


Le module de Synthèse Métaphysique est un paquet réutilisable pour agents d’intelligence artificielle consacré au BaZi, au Meihua Yishu, au Liuyao, au Feng Shui directionnel et au Tarot. Ce n'est pas une simple instruction de divination. C'est une méthode structurée qui aide un assistant IA à choisir le bon système, vérifier les entrées, formuler un verdict, présenter les preuves, estimer le délai, proposer des actions et définir des signes de vérification. Il peut être utilisé avec Codex, Claude Code ou tout autre agent capable de lire un dossier local contenant des instructions, des références et des scripts.

La plupart des réponses de divination générées par IA deviennent trop générales. Elles mélangent astrologie chinoise, Yi King, Feng Shui et Tarot comme s'il s'agissait d'un seul langage symbolique. Elles prennent parfois un seul signe, une seule carte ou un seul conflit et en font une conclusion dramatique. Ce module évite cette dérive. Le BaZi sert à lire la structure de vie et les cycles de chance. Le Meihua Yishu sert aux questions soudaines, aux horaires, aux nombres et aux présages. Le Liuyao sert aux résultats concrets: contrat, poste, supérieur, salaire, projet, relation spécifique. Le Feng Shui sert à lire l'espace, la direction, le soutien arrière, l'ouverture devant soi, les portes, les fenêtres, les flux et la visibilité. Le Tarot sert à lire les dynamiques psychologiques, relationnelles et décisionnelles.

Le module est conçu pour être direct sans être irresponsable. Il peut donner un verdict ferme lorsque les signes convergent, mais il marque aussi les limites. Chaque méthode peut être `runnable`, `partial` ou `blocked`. Une heure de naissance incertaine ne permet pas une lecture détaillée du pilier de l'heure. Six lignes Liuyao sans ordre clair ne permettent pas une lecture Najia complète. Une analyse Feng Shui sans plan ni boussole ne permet pas de conclure sur les formules avancées. Un tirage Tarot fourni par l'utilisateur ne doit pas être remplacé par un nouveau tirage. Cette discipline rend l'outil plus fiable et plus facile à intégrer dans des agents différents.

## Langues

- [anglais](README.md)
- [chinois simplifié](README.zh-CN.md)
- [coréen](README.ko-KR.md)
- [japonais](README.ja-JP.md)
- [français](README.fr-FR.md)
- [espagnol](README.es-ES.md)

## Pour qui

Ce dépôt s'adresse aux personnes qui veulent donner à un agent IA une méthode stable pour traiter des questions métaphysiques sans réécrire une longue instruction à chaque fois. Il est aussi utile pour créer un outil de consultation, un assistant personnel, un flux de recherche symbolique ou un système interne de lecture structurée. Les fichiers de référence séparent les méthodes, les scripts évitent de réécrire des opérations déterministes, et les modèles de sortie permettent de garder un style clair.

L'objectif n'est pas de rendre la divination plus vague ou plus spectaculaire. L'objectif est de la rendre plus lisible. Une bonne réponse doit dire ce qui est fort, ce qui est faible, ce qui manque, ce qui peut être vérifié et quelle action concrète suivre. Le style peut être symbolique, mais le processus doit rester propre.

## Systèmes pris en charge

| Système | Présentation d'environ 100 mots | Fichier principal |
| --- | --- | --- |
| [BaZi / astrologie chinoise](https://fr.wikipedia.org/wiki/Astrologie_chinoise) | Le BaZi, ou quatre piliers, utilise l'année, le mois, le jour et l'heure de naissance pour établir une structure symbolique fondée sur les troncs célestes, les branches terrestres et les cinq phases. Dans ce module, il sert aux tendances longues: carrière, richesse, mariage, santé, cycles décennaux et déclencheurs annuels. | `references/bazi.md` |
| [Meihua Yishu / Yi Jing](https://fr.wikipedia.org/wiki/Yi_Jing) | Le Meihua Yishu est une approche image-nombre liée au Livre des Mutations. Il est utile pour les événements proches, les signes extérieurs, les horaires, les nombres, les directions et les changements soudains. Le module distingue l'hexagramme principal, la ligne mobile, l'hexagramme mutuel, l'hexagramme transformé et la relation Ti/Yong. | `references/meihua.md` |
| [Liuyao / Wenwanggua](https://en.wikipedia.org/wiki/Wenwanggua) | Le Liuyao lit six lignes, les lignes mobiles, les rôles, les relations et les déclencheurs temporels pour répondre à des questions concrètes. Il convient aux contrats, promotions, supérieurs, salaires, projets et relations spécifiques. Le module impose l'ordre de bas en haut et limite la lecture si les données Najia manquent. | `references/liuyao.md` |
| [Feng Shui](https://fr.wikipedia.org/wiki/Feng_shui) | Le Feng Shui étudie l'orientation, la forme, les flux, le soutien arrière, les ouvertures, le bruit, la lumière et la circulation. Ce module lit d'abord l'environnement observable avant les formules directionnelles. Il privilégie les ajustements pratiques: clarté, stabilité, attention, confidentialité et visibilité. | `references/fengshui.md` |
| [Tarot divinatoire](https://fr.wikipedia.org/wiki/Tarot_divinatoire) | Le Tarot utilise un tirage, les positions, les images, les suites, les nombres, les cartes droites ou inversées et les relations entre cartes pour explorer psychologie, relation et choix. Ce module permet des tirages reproductibles avec seed afin d'éviter de retirer les cartes jusqu'à obtenir une réponse agréable. | `references/tarot.md` |

## Méthode de réponse

1. Reformuler la question.
2. Sélectionner le système adapté.
3. Vérifier les entrées nécessaires.
4. Marquer la méthode comme `runnable`, `partial` ou `blocked`.
5. Lire chaque système séparément avant toute synthèse.
6. Ne synthétiser que les signaux compatibles.
7. Répondre avec verdict, preuves, timing, action et vérification.

Format de réponse typique:

```text
Verdict :
Preuves :
Timing / force :
Action :
Signes de vérification :
Hypothèses de faible confiance :
```

## Installation pour tous les agents d’intelligence artificielle

### Installation universelle

```bash
mkdir -p ~/agent-skills
git clone https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill.git ~/agent-skills/metaphysics-synthesis
cd ~/agent-skills/metaphysics-synthesis
python3 scripts/validate_skill.py
```

Indiquez ensuite à votre agent:

```text
Utilise le module local situé dans ~/agent-skills/metaphysics-synthesis/SKILL.md. Charge uniquement le fichier de référence adapté au système demandé.
```

### Codex

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill.git ~/.codex/skills/metaphysics-synthesis
python3 ~/.codex/skills/metaphysics-synthesis/scripts/validate_skill.py
```

### Claude Code

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill.git ~/.claude/skills/metaphysics-synthesis
python3 ~/.claude/skills/metaphysics-synthesis/scripts/validate_skill.py
```

### Dossier personnalisé

```bash
AGENT_SKILLS_DIR="$HOME/.your-agent/skills"
mkdir -p "$AGENT_SKILLS_DIR"
git clone https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill.git "$AGENT_SKILLS_DIR/metaphysics-synthesis"
python3 "$AGENT_SKILLS_DIR/metaphysics-synthesis/scripts/validate_skill.py"
```

### Une seule copie pour plusieurs agents

```bash
mkdir -p ~/agent-skills
git clone https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill.git ~/agent-skills/metaphysics-synthesis

mkdir -p ~/.codex/skills ~/.claude/skills
ln -sfn ~/agent-skills/metaphysics-synthesis ~/.codex/skills/metaphysics-synthesis
ln -sfn ~/agent-skills/metaphysics-synthesis ~/.claude/skills/metaphysics-synthesis
```

## Exemples

```text
Analyse ce thème BaZi pour la carrière et la richesse de 2026 à 2036. Sépare la structure natale, la chance décennale, les déclencheurs annuels, les conclusions fortes et les hypothèses faibles.
```

```text
Utilise le Meihua Yishu pour lire si ce lancement de produit peut créer une percée professionnelle visible. La question est apparue le 2026-06-12 à 10:36, avec comme signe externe un manager discutant du planning au nord-ouest.
```

```text
Utilise le Liuyao pour juger si ce projet peut devenir la preuve principale d'une promotion. Les six lignes de bas en haut sont 5 / 4 / 25 / 12 / 22 / 17.
```

```text
Analyse mon poste de travail avec la logique des directions Feng Shui. Je fais face au sud-est, mon manager direct est au nord-ouest, le grand responsable est au sud, et un manager transversal est à l'est.
```

```text
Fais un tirage Tarot de cinq cartes pour une décision professionnelle. Affiche le valeur de départ, les positions, les cartes droites ou inversées, le verdict, l'action et les signes de vérification.
```

## Scripts utiles

```bash
python3 scripts/meihua_calc.py time 2026 6 12 10
python3 scripts/meihua_calc.py num 22 5 18
python3 scripts/tarot_draw.py --spread relationship --question "Cette collaboration va-t-elle mûrir ?" --seed 42
python3 scripts/validate_skill.py
python3 scripts/privacy_check.py
```

## Limites de sécurité

Ce dépôt considère la divination comme un cadre culturel, symbolique, réflexif et stratégique. Il ne remplace pas un avis médical, juridique, financier, psychologique, d'urgence ou de sécurité. Pour les sujets à risque, utilisez d'abord les preuves directes et les professionnels qualifiés.

## Licence

MIT License. Voir [LICENSE](LICENSE).
