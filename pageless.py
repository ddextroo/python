import fitz  # PyMuPDF
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def convert_pdf_without_page_breaks(pdf_path, output_path):
    pdf_document = fitz.open(pdf_path)
    
    output_pdf = canvas.Canvas(output_path, pagesize=letter)
    
    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number]
        text = page.get_text("text")
        
        # Draw the extracted text on the canvas
        output_pdf.drawString(50, 750, text)
        
        if page_number < pdf_document.page_count - 1:
            output_pdf.showPage()
    
    output_pdf.save()
    pdf_document.close()

input_pdf_path = "MyGrades.pdf"
output_pdf_path = "output_pdf_without_page_breaks.pdf"
convert_pdf_without_page_breaks(input_pdf_path, output_pdf_path)
