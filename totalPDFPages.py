from flask import Flask, request, jsonify
import requests
import PyPDF2
from io import BytesIO

app = Flask(__name__)

@app.route('/gpa/total_pages', methods=['POST'])
def get_total_pages():
    data = request.get_json()
    pdf_url = data.get('pdf_url')

    if not pdf_url:
        return jsonify({'error': 'pdf_url parameter is required'}), 400

    response = requests.get(pdf_url)
    if response.status_code == 200:
        pdf_content = BytesIO(response.content)
        pdf_reader = PyPDF2.PdfReader(pdf_content)
        total_pages = len(pdf_reader.pages)
        return jsonify({'total_pages': total_pages})
    else:
        return jsonify({'error': 'Failed to fetch PDF from the URL'}), 500

if __name__ == '__main__':
    app.run(debug=True)
