from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import pandas as pd
import streamlit as st
from app.core.service import analyze_business

st.set_page_config(page_title="AI Business Manager", page_icon="📊", layout="wide")
st.title("📊 AI Business Manager")
st.caption("Sales analytics with a local demonstration mode and optional live LLM integrations.")

sample_path = Path(__file__).resolve().parents[1] / "data" / "sample_sales.csv"
upload = st.file_uploader("Upload a CSV", type=["csv"])
try:
    df = pd.read_csv(upload) if upload else pd.read_csv(sample_path)
    required = {"product", "category", "quantity", "unit_price"}
    if not required.issubset(df.columns):
        st.error("CSV must contain: product, category, quantity, unit_price")
        st.stop()
    st.subheader("Sales data")
    st.dataframe(df, use_container_width=True)
    use_ai = st.checkbox("Generate analysis", value=True)
    st.caption("In AI_MODE=demo, insights use local deterministic rules. In AI_MODE=live, configured provider APIs are called.")
    if st.button("Analyze sales", type="primary"):
        result = analyze_business(df.to_dict(orient="records"), use_ai=use_ai)
        metrics = result["metrics"]
        a, b, c = st.columns(3)
        a.metric("Total revenue", f"R$ {metrics['total_revenue']:,.2f}")
        b.metric("Units sold", f"{metrics['units_sold']:,.0f}")
        c.metric("Average per record", f"R$ {metrics['average_revenue_per_record']:,.2f}")
        st.subheader("Revenue by category")
        st.bar_chart(pd.Series(metrics["revenue_by_category"]))
        st.subheader("Top products")
        st.dataframe(pd.DataFrame(metrics["top_products"]), use_container_width=True)
        st.subheader("Analysis results")
        if result["ai"]["mode"] == "demo":
            st.info("Demonstration mode: this analysis uses local rules and does not call an external AI model.")
        if not use_ai:
            st.info("Analysis was not requested. Metrics above are calculated deterministically.")
        elif result["ai"]["mode"] == "not_configured":
            st.warning("No provider returned a live response. Check AI_MODE and API credentials in your local .env.")
            st.json(result["ai"])
        else:
            for item in result["ai"]["results"]:
                with st.expander(item["provider"] + " — " + item["status"]):
                    st.write(item.get("analysis", item.get("error", "")))
except Exception as exc:
    st.error(f"Could not process the file: {exc}")
