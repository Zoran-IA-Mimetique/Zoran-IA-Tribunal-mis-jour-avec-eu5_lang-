# EU-5 — Micro-langue universelle (FR/EN/DE/ES/IT)

**But** : être compris instantanément via **64 concepts** (emoji + mot EU5) et une **grammaire minimale** (SVO, `no-` pour la négation, `++` pour «et», `?` pour question).  
**Domaine** : secours, santé, mobilité, achat, orientation.

## Démarrage rapide
```bash
python main.py --lexicon
python main.py --from eu5 --to fr "WHERE TOILET ?"
python main.py --from fr --to eu5 "prix billet train"
```

## Fichiers
- `lexicon.json` — 64 concepts (emoji, EU5, FR/EN/DE/ES/IT)
- `phrasebook.csv` — phrases types multi-langues
- `main.py` — convertisseur EU5↔langues (proto dictionnaire)
- `eu5_block.zgs` — balise glyphique IA↔IA

**Contact** : tabary01@gmail.com · **Date** : 2025-08-26