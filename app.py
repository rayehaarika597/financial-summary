from flask import Flask, request, jsonify
import tempfile
from pathlib import Path

from utils.pdf_parser import pdf_extraction
from crew.crew import document_summary  # your function that runs agents

app = Flask(__name__)

@app.route('/summary', methods=['POST'])
def analyze_pdf():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    file = request.files['file']

    with tempfile.NamedTemporaryFile(delete=False,suffix=".pdf") as tmp:
        tmp.write(file.read())
        tmp_path = Path(tmp.name)

    extract_result = pdf_extraction(tmp_path)
    print("this is the extracted result:",extract_result)
    if extract_result["status"] != "success":
        return jsonify(extract_result), 400

    summary = extract_result["data"]["summary"]

    # summary = document_summary(extracted_text)

    return jsonify({
        "summary": summary
    })

if __name__ == '__main__':
    app.run(debug=True)
