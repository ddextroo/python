from datetime import datetime
excel_filename = f"{datetime.utcnow().strftime('%Y%m%d%H%M%S%f')}.xlsx"
print(excel_filename) 