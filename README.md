# Racial Voting

This repository scaffolds a reproducible pipeline for studying racial voting patterns using ANES data.
It is organized for transparent ingestion, parsing, transformation, and descriptive analysis.
The codebase separates source data handling from derived analytical outputs.
Project documentation includes decisions, prompts, and a living session log for traceability.
Data moves from `data/raw/` to `data/interim/` to `data/clean/` before analysis.
Figures, tables, and report artifacts are written under `outputs/`.

## Quickstart
```bash
python scripts/00_bootstrap.py
python scripts/01_download_anes.py
python scripts/04_make_figures.py
```
