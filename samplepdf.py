import tabula
import pandas as pd

# Path to your PDF file
pdf_path = 'MyGrades.pdf'

# List to store extracted column data from all pages
all_column_data = []

# Column index you want to extract (0-based indexing)
column_index = 2

# Get the total number of pages in the PDF
total_pages = len(tabula.read_pdf(pdf_path, pages='all'))

# Iterate through each page and extract the specified column
for page in range(1, total_pages + 1):
    # Use tabula to extract tables from the current page into a list of DataFrames
    tables = tabula.read_pdf(pdf_path, pages=page, multiple_tables=True)
    
    # If there's at least one table detected on the page
    if tables:
        # Extract data from the specified column (assuming the table has at least column_index + 1 columns)
        column_data = tables[0].iloc[:, column_index]
        
        # Append the column data to the list
        all_column_data.append(column_data)

# Concatenate the column data from all pages into a single Series
merged_column_data = pd.concat(all_column_data, ignore_index=True)

# Display the extracted column data from all pages
print(merged_column_data)
