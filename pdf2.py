import tabula
import pandas as pd
import re
from flask import Flask, request, jsonify

app = Flask(__name__)

def process_pdf(**details):
    tables = tabula.read_pdf(details.get("pdf_url"), pages=details.get("page"), multiple_tables=True)
    
    # Initialize empty lists to store data for each page
    all_tables = []
    all_semester_indices = []
    all_semesters_available = []
    all_semester_pages = []

    for page_number, table_df in enumerate(tables, start=1):
        # Process each page's table
        pattern = r'^[0-9]+(st|nd|rd|th) Semester'
        semester_changes = table_df.iloc[:, 2].str.match(pattern, na=False)  # Using column number 2 for DESCRIPTION
        semester_indices = semester_changes.cumsum() - 1
        semesters_available = table_df.loc[semester_changes, table_df.columns[2]]

        all_tables.append(table_df)
        all_semester_indices.append(semester_indices)
        all_semesters_available.append(semesters_available)
        all_semester_pages.extend([page_number] * len(semesters_available))

    # Concatenate data from all pages
    full_table = pd.concat(all_tables, ignore_index=True)
    all_semester_indices = pd.concat(all_semester_indices, ignore_index=True)
    all_semesters_available = pd.concat(all_semesters_available, ignore_index=True)

    return full_table, all_semester_indices, all_semesters_available, all_semester_pages


@app.route('/gpa/process_pdf', methods=['POST'])
def api_process_pdf():
    data = request.json
    pdf_url = data.get('pdf_url')
    
    if pdf_url:
        _, _, semesters_available, semester_pages = process_pdf(pdf_url = pdf_url, page = 'all')
        
        result = []
        semesters_list = semesters_available.tolist()
        result = [{'semester': semester, 'page': page} for semester, page in zip(semesters_list, semester_pages)]
        return jsonify(result)
    else:
        return jsonify({'error': 'Missing PDF URL in the request'}), 400

@app.route('/gpa/retrieve_semester', methods=['POST'])
def api_retrieve_semester():
    data = request.json
    pdf_url = data.get('pdf_url')
    selected_semester_idx = data.get('selected_semester_idx')
    page = data.get('page')
    
    if pdf_url and selected_semester_idx is not None:
        full_table, semester_indices, semesters_available, page = process_pdf(pdf_url = pdf_url, page = page)
        
        if 0 <= selected_semester_idx < len(semesters_available):
            selected_semester_table = full_table[semester_indices == selected_semester_idx]
            
            comp_row = selected_semester_table[selected_semester_table.iloc[:, 2] == '7']  # Using column number 2 for DESCRIPTION
            grade_row = selected_semester_table[selected_semester_table.iloc[:, 2] == '8']  # Using column number 2 for DESCRIPTION
            if not comp_row.empty and not pd.isna(comp_row.iloc[0, 7]):  # Using column number 7 for GRADE
                selected_semester_table.loc[grade_row.index, full_table.columns[7]] = comp_row.iloc[0, 7]  # Using column number 7 for GRADE
            
            selected_semester_table.loc[
                selected_semester_table.iloc[:, 7].isna() & selected_semester_table.iloc[:, 8].notna(),  # Using column numbers 7 and 8 for GRADE and COMP
                full_table.columns[7]  # Using column number 7 for GRADE
            ] = selected_semester_table.iloc[:, 8]  # Using column number 8 for COMP
            
            filtered_table = selected_semester_table.iloc[:, [1, 2, 3, 7]].dropna()  # Using column numbers 1, 2, 3, and 7
            
            # Rename columns to new keys
            filtered_table.columns = ['SUBJECT', 'DESCRIPTION', 'UNIT', 'GRADE']
            
            return jsonify(filtered_table.to_dict(orient='records'))
        else:
            return jsonify({'error': 'Invalid semester index'}), 400
    else:
        return jsonify({'error': 'Missing PDF URL or selected semester index in the request'}), 400



if __name__ == '__main__':
    app.run(debug=True)
