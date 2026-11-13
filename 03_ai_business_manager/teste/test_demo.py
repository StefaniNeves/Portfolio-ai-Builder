from app.core.service import analyze_business


def test_demo_mode_returns_local_analysis_without_api_keys(monkeypatch):
    monkeypatch.setenv("AI_MODE", "demo")
    result = analyze_business([
        {"product": "Desk", "category": "Office", "quantity": 2, "unit_price": 50},
        {"product": "Chair", "category": "Office", "quantity": 1, "unit_price": 80},
    ], use_ai=True)

    assert result["ai"]["mode"] == "demo"
    assert result["ai"]["results"][0]["provider"] == "Demo Engine"
    assert "não foi produzida por GPT, Claude ou Gemini" in result["ai"]["results"][0]["analysis"]
