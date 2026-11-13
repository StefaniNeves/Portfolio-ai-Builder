import csv
from pathlib import Path

rows = [
    ["product", "category", "quantity", "unit_price"],
    ["Coffee maker", "Appliances", 4, 189.90],
    ["Storage organizer", "Home", 12, 39.90],
    ["Desk lamp", "Home", 8, 59.90],
    ["Blender", "Appliances", 3, 249.00],
    ["Water bottle", "Accessories", 15, 29.90],
]
path = Path(__file__).resolve().parents[1] / "data" / "sample_sales.csv"
with path.open("w", newline="", encoding="utf-8") as file:
    csv.writer(file).writerows(rows)
print(f"Sample data written to {path}")
