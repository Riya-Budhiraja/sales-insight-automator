from fastapi import FastAPI, UploadFile, File, Form
import pandas as pd
import os
from slowapi import Limiter
from slowapi.util import get_remote_address

app = FastAPI()
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

@app.post("/analyze")
@limiter.limit("5/minute")
async def analyze(file: UploadFile = File(...), email: str = Form(...)):
    # Validate file type
    if not file.filename.endswith((".csv", ".xlsx")):
        return {"error": "Invalid file type. Only CSV or XLSX allowed"}

    # Read file
    if file.filename.endswith(".csv"):
        df = pd.read_csv(file.file)
    else:
        df = pd.read_excel(file.file)

    total_revenue = df["Revenue"].sum()
    top_region = df.groupby("Region")["Revenue"].sum().idxmax()

    summary = f"Total Revenue: {total_revenue}\nTop Performing Region: {top_region}"

    return {"summary": summary}