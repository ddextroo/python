from flask import Flask, request, send_file, jsonify
import pandas as pd
import json
from io import BytesIO

app = Flask(__name__)

@app.route('/export', methods=['POST'])
def convert_json_to_excel():
    try:
        json_data = request.json  # Assumes the client sends a JSON object in the request body

        # Check if the "type" key exists and modify its values
        for entry in json_data:
            if 'type' in entry:
                entry['type'] = 'Cash in' if entry['type'] == 'Income' else 'Cash out'

        # Process the modified JSON and create Excel file
        excel_output = json_to_excel(json_data)

        if excel_output:
            return send_file(
                excel_output,
                as_attachment=True,
                download_name='output.xlsx',
                mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )
        else:
            return jsonify({"error": "Error processing JSON"}), 400

    except json.JSONDecodeError as e:
        return jsonify({"error": f"Error decoding JSON: {e}"}), 400

def json_to_excel(json_data, excel_file_name='output.xlsx'):
    try:
        # Create a DataFrame from the modified JSON data
        df = pd.json_normalize(json_data)  # Flatten nested JSON structure

        # Save DataFrame to Excel file
        excel_output = BytesIO()
        df.to_excel(excel_output, index=False)
        excel_output.seek(0)

        return excel_output

    except Exception as e:
        print(f'Error processing JSON: {e}')
        return None

if __name__ == '__main__':
    app.run(debug=True)
