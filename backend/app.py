# backend/app.py
from flask import Flask, jsonify, request, send_file
from utils import generate_openai_report, generate_pdf
import os

app = Flask(__name__)

@app.route("/api/generate-report", methods=["POST"])
def generate_report():
    data = request.json
    prompt = f"Generate a report for {data['location']} in the {data['industry']} industry, based on Beige Book version {data['version']}."

    report_text = generate_openai_report(prompt)  # Call OpenAI API
    pdf_path = generate_pdf(report_text)          # Generate PDF from the report text

    return jsonify({"report": report_text, "pdf_path": pdf_path})

@app.route("/api/download-pdf", methods=["GET"])
def download_pdf():
    pdf_path = request.args.get("pdf_path")
    return send_file(pdf_path, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
