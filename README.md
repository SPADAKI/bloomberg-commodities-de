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

Dashboard Snapshots:
<img width="856" height="670" alt="Screenshot 2025-11-05 at 3 26 23 PM" src="https://github.com/user-attachments/assets/3fb9c60c-5217-4149-9f50-29e397c9f117" />
<img width="811" height="695" alt="Screenshot 2025-11-05 at 3 26 01 PM" src="https://github.com/user-attachments/assets/2a52eeac-4e53-422f-a14a-425b24d5f4b4" />
