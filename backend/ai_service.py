import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def generate_summary(data):

    prompt = f"""
    Analyze the following sales data and generate a professional executive summary.

    Include:
    - Total revenue insight
    - Best performing region
    - Product trends
    - Any anomalies

    Data:
    {data}
    """

    response = model.generate_content(prompt)

    return response.text