# Bloomberg Commodities ETL – Simple & Scalable

**Built in < 1 hour** – no Bloomberg Terminal, no live data, just **6 real Kaggle commodity CSVs**.

---

## Goal
Show a **clean, maintainable ETL pipeline** that:
- Auto-detects `Date` and numeric columns (`Price`, `High`, `Low`, etc.)
- Handles real-world messiness: commas in numbers, missing columns, mixed formats
- Combines all assets into one clean file
- Delivers an **interactive dashboard** for instant insight

> *Designed for junior onboarding – runs in 60 seconds.*

---

## Tech Stack
| Tool | Purpose |
|------|--------|
| **Polars** | Fast, memory-efficient data processing |
| **Streamlit** | One-click interactive dashboard |
| **CSV → CSV** | Simple, portable, no external storage |

---

## Folder Structure
bloomberg-commodities-de/
├── data/
│   └── raw/               # ← Your 6 Kaggle CSVs go here
├── pipeline.py            # ← Ingest + clean + combine
├── dashboard.py           # ← Interactive chart
└── README.md
