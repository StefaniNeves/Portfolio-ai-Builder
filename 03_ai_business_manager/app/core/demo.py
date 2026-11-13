from __future__ import annotations
from typing import Any


def build_demo_analysis(metrics: dict[str, Any]) -> dict[str, Any]:
    """Create transparent, deterministic insights without calling an LLM."""
    categories = metrics.get("revenue_by_category", {})
    top_products = metrics.get("top_products", [])
    total = float(metrics.get("total_revenue", 0))
    units = float(metrics.get("units_sold", 0))

    if categories:
        best_category, best_revenue = max(categories.items(), key=lambda item: item[1])
        category_text = (
            f"A categoria com maior faturamento foi **{best_category}**, "
            f"com R$ {best_revenue:,.2f}."
        )
    else:
        category_text = "Não há categorias suficientes para comparação."

    if top_products:
        leader = top_products[0]
        product_text = (
            f"O produto com maior faturamento foi **{leader['product']}**, "
            f"com R$ {leader['revenue']:,.2f}."
        )
    else:
        product_text = "Não há produtos suficientes para identificar um destaque."

    recommendations = [
        "Compare o desempenho da categoria líder com os períodos anteriores antes de aumentar o estoque.",
        "Investigue os produtos com menor faturamento para identificar oportunidades de preço, divulgação ou mix.",
        "Acompanhe faturamento e unidades vendidas em períodos regulares para identificar mudanças na demanda.",
    ]
    summary = (
        "### Análise demonstrativa (regras locais)\n\n"
        f"Foram analisados **{metrics.get('record_count', 0)} registros**, "
        f"com faturamento calculado de **R$ {total:,.2f}** e "
        f"**{units:,.0f} unidades** vendidas.\n\n"
        f"{category_text}\n\n{product_text}\n\n"
        "**Recomendações para avaliação:**\n"
        + "\n".join(f"- {item}" for item in recommendations)
        + "\n\n**Limitação:** esta resposta é gerada por regras determinísticas locais; "
          "não foi produzida por GPT, Claude ou Gemini."
    )
    return {
        "mode": "demo",
        "results": [{
            "provider": "Demo Engine",
            "status": "success",
            "analysis": summary,
            "source": "local_rules",
        }],
    }
