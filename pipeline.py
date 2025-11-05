# pipeline.py — FINAL, BULLETPROOF
import polars as pl
import os

dfs = []
for file in os.listdir("data/raw"):
    if file.endswith(".csv"):
        path = f"data/raw/{file}"
        df = pl.read_csv(path, infer_schema_length=0)
        
        date_col = next((c for c in df.columns if "date" in c.lower()), None)
        numeric_cols = [c for c in df.columns if any(x in c.lower() for x in ["price", "open", "high", "low", "vol", "change"])]
        
        if date_col and numeric_cols:
            select_exprs = [
                pl.col(date_col).str.to_date().alias("Date"),
                pl.lit(file.split(".")[0].replace("_", " ").title()).alias("Asset")
            ]
            for col in numeric_cols:
                clean_col = (
                    pl.col(col)
                    .str.replace_all(",", "")
                    .str.replace_all("%", "")
                    .cast(pl.Float64, strict=False)
                    .fill_null(0)  # Fill nulls with 0
                    .alias(col)
                )
                select_exprs.append(clean_col)
            
            clean = df.select(select_exprs)
            dfs.append(clean)

# Combine
data = pl.concat(dfs).sort("Date")
os.makedirs("data", exist_ok=True)
data.write_csv("data/combined_commodities.csv")
print(f"DONE: {len(data)} rows from {len(dfs)} files → data/combined_commodities.csv")