import pytest
from app.core.analysis import analyze_sales


def test_calculates_revenue_and_units():
    result = analyze_sales([
        {"product": "A", "category": "Home", "quantity": 2, "unit_price": 10},
        {"product": "B", "category": "Food", "quantity": 3, "unit_price": 5},
    ])
    assert result["total_revenue"] == 35
    assert result["units_sold"] == 5
    assert result["record_count"] == 2
    assert result["revenue_by_category"] == {"Home": 20, "Food": 15}


def test_rejects_empty_records():
    with pytest.raises(ValueError):
        analyze_sales([])


def test_rejects_negative_values():
    with pytest.raises(ValueError):
        analyze_sales([{"quantity": -1, "unit_price": 10}])


def test_rejects_missing_numeric_field():
    with pytest.raises(ValueError):
        analyze_sales([{"quantity": 1}])
