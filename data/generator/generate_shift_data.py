"""
Generate synthetic shift-level productivity data.

Usage:
    python data/generator/generate_shift_data.py --days 14
"""
import argparse, numpy as np, pandas as pd
from pathlib import Path

def generate(days: int, out_path: str):
    np.random.seed(7)
    dates  = pd.date_range("2025-01-01", periods=days, freq="D")
    shifts = ["DAY", "SWING", "NIGHT"]
    buckets = ["S", "M", "L", "XL"]

    rows = []
    for d in dates:
        for sh in shifts:
            mix = np.random.dirichlet(np.ones(len(buckets)))
            for bkt, pct in zip(buckets, mix):
                rows.append({
                    "date": d.date(),
                    "shift": sh,
                    "size_bucket": bkt,
                    "units_scanned": int(np.random.normal(5000, 800) * pct),
                    "target_rate": np.random.randint(350, 420)
                })
    df = pd.DataFrame(rows)
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=False)
    print(f"✓ Saved {out_path}  ({len(df):,} rows)")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=14,
                    help="number of days to simulate")
    ap.add_argument("--out", type=str,
                    default="data/raw/shift_productivity_sample.csv",
                    help="output CSV path")
    args = ap.parse_args()
    generate(args.days, args.out)

