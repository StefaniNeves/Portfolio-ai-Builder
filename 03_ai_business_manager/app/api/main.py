from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from app.core.service import analyze_business

app = FastAPI(title="AI Business Manager API", version="1.0.0",
              description="Sales analytics with local demo insights or optional multi-provider AI analysis.")

class SaleRecord(BaseModel):
    product: str = "Unspecified product"
    category: str = "Uncategorized"
    quantity: float = Field(ge=0)
    unit_price: float = Field(ge=0)

class AnalysisRequest(BaseModel):
    records: list[SaleRecord] = Field(min_length=1)
    use_ai: bool = False

@app.get("/health")
def health():
    return {"status": "ok", "service": "ai-business-manager"}

@app.post("/analyze")
def analyze(payload: AnalysisRequest):
    try:
        return analyze_business([r.model_dump() for r in payload.records], payload.use_ai)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
