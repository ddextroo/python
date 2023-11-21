from flask import Flask, request, jsonify
import pandas as pd
import requests
from io import BytesIO

app = Flask(__name__)

def excel_to_json(excel_content):
    try:
        # Read Excel content into a DataFrame
        df = pd.read_excel(BytesIO(excel_content))

        # Convert DataFrame to a list of dictionaries
        json_data = df.to_dict(orient='records')

        # Modify the 'type' key based on the condition
        for entry in json_data:
            entry['type'] = 'Income' if entry['type'] == 'Cash in' else 'Expense'

        # Convert the modified data back to JSON string
        modified_json_string = pd.DataFrame(json_data).to_json(orient='records')

        return modified_json_string
    except Exception as e:
        return str(e)

@app.route('/import', methods=['POST'])
def process_excel():
    try:
        data = request.json
        excel_url = data.get('url')

        # Download the Excel file, allowing redirects
        response = requests.get(excel_url, allow_redirects=True)
        response.raise_for_status()  # Check for errors in the HTTP request

        # Convert Excel to JSON with type modification
        json_string = excel_to_json(response.content)

        return jsonify({'result': 'success', 'json_data': json_string})
    except Exception as e:
        return jsonify({'result': 'error', 'message': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
