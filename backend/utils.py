# backend/utils.py
import os
import openai
from fpdf import FPDF

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_openai_report(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error: {e}")
        return "Report generation failed."

def generate_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, text)
    pdf_path = "report.pdf"
    pdf.output(pdf_path)
    return pdf_path
