# Headcount-Optimization Tool

Synthetic demo of the labour-planning model that saved **\$252 K per month** during my Amazon internship.

## Dataset
| File | Purpose |
|------|---------|
| `data/raw/shift_productivity_sample.csv` | tiny sample (10 rows) |
| `data/generator/generate_shift_data.py` | script to generate a larger dataset |

## Quick start
```bash
pip install -r requirements.txt
python data/generator/generate_shift_data.py --days 14      # regenerate data
jupyter notebook notebooks/01_optimize_demo.ipynb
