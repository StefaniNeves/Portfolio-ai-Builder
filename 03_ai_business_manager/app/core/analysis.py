from __future__ import annotations

from collections import Counter
from typing import Any


def analyze_sales(records: list[dict[str, Any]]) -> dict[str, Any]:
    """Calculate transparent business metrics from sales records.

    Expected fields: product, category, quantity, unit_price.
    Missing optional product/category values receive safe defaults.
    """
    if not records:
        raise ValueError("At least one sales record is required.")

    normalized: list[dict[str, Any]] = []
    for index, row in enumerate(records):
        try:
            quantity = float(row["quantity"])
            unit_price = float(row["unit_price"])
        except (KeyError, TypeError, ValueError) as exc:
            raise ValueError(
                f"Record {index + 1} must contain numeric quantity and unit_price."
            ) from exc
        if quantity < 0 or unit_price < 0:
            raise ValueError(f"Record {index + 1} cannot contain negative values.")
        normalized.append({
            "product": str(row.get("product") or "Unspecified product"),
            "category": str(row.get("category") or "Uncategorized"),
            "quantity": quantity,
            "unit_price": unit_price,
            "revenue": quantity * unit_price,
        })

    total_revenue = sum(row["revenue"] for row in normalized)
    total_units = sum(row["quantity"] for row in normalized)
    category_revenue: Counter[str] = Counter()
    product_revenue: Counter[str] = Counter()
    for row in normalized:
        category_revenue[row["category"]] += row["revenue"]
        product_revenue[row["product"]] += row["revenue"]

    return {
        "record_count": len(normalized),
        "total_revenue": round(total_revenue, 2),
        "units_sold": round(total_units, 2),
        "average_revenue_per_record": round(total_revenue / len(normalized), 2),
        "revenue_by_category": dict(category_revenue.most_common()),
        "top_products": [
            {"product": name, "revenue": round(value, 2)}
            for name, value in product_revenue.most_common(5)
        ],
        "records": normalized,
    }
