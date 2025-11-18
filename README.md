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

## Dashboard Snapshots:
<img width="811" height="695" alt="Screenshot 2025-11-05 at 3 26 01 PM" src="https://github.com/user-attachments/assets/2a52eeac-4e53-422f-a14a-425b24d5f4b4" />
<img width="790" height="660" alt="Screenshot 2025-11-05 at 3 35 43 PM" src="https://github.com/user-attachments/assets/ebd1f398-bbfc-46f9-92ea-1010809aca19" />
<img width="856" height="670" alt="Screenshot 2025-11-05 at 3 26 23 PM" src="https://github.com/user-attachments/assets/3fb9c60c-5217-4149-9f50-29e397c9f117" />
<img width="775" height="622" alt="Screenshot 2025-11-05 at 3 35 56 PM" src="https://github.com/user-attachments/assets/ac672b1b-1d6b-4763-bf1e-cdd3e7306594" />
<img width="761" height="645" alt="Screenshot 2025-11-05 at 3 35 30 PM" src="https://github.com/user-attachments/assets/0c94853f-5443-4d9c-9c5a-5caf3eab12e9" />

##Run Instructions:
```bash
# 1. Install (once)
pip3 install polars streamlit

# 2. Run ETL
python3 pipeline.py

# Bloomberg Commodities ETL – Day 1 Ready (ML + Anomaly Detection)

Built for Bloomberg interview prep: From Kaggle mocked CSVs to production-grade pipeline in <2 hours.  
**Now with Data Quality (DQ) guards + Z-Score anomaly detection** — catches negative prices and 3σ outliers instantly.

## 🚀 What's New in Day 1
- **DQ Check**: Auto-removes invalid prices ≤ 0 (critical for finance).
- **Anomaly Detection**: Log-transform + Z-Score (3σ rule) on prices — industry standard for commodity volatility.
- **Robustness**: Column-name agnostic (works with "Price", "Close", etc.).
- **Zero Extra Deps**: Pure Polars + NumPy/SciPy — no Great Expectations bloat.

**Sample Output**:

# 3. Launch dashboard
streamlit run dashboard.py


## 🎯 Goal
Scalable ETL for commodity data:
- Ingests messy CSVs (commas, % signs, mixed formats).
- Cleans, combines, and validates.
- Flags anomalies for trading desk alerts.
- Ready for Prefect orchestration (Day 2).

## 🛠 Tech Stack
| Tool | Purpose |
|------|---------|
| **Polars** | Lightning-fast data processing (10x Pandas). |
| **NumPy/SciPy** | Z-Score stats (log-normal for prices). |
| **Pandas** (minimal) | Temp conversions only. |
| **CSV Output** | Portable + human-readable (Parquet ready for prod). |

## 📁 Folder Structure
bloomberg-commodities-de/
├── data/
│   ├── raw/              # Drop your 6 Kaggle CSVs here (e.g., crude_oil.csv)
│   ├── combined_commodities.csv     # Raw combined output
│   └── combined_commodities_clean.csv  # DQ + anomaly-flagged
├── pipeline.py           # Full ETL + Day 1 upgrades
├── dashboard.py          # Interactive Streamlit viz (launch with streamlit run dashboard.py)
└── README.md




