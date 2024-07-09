import PyPDF2
import os

# Define the input PDF file path
input_pdf = "CS_JobSearch.pdf"

# Define the page ranges for each section
sections = [
    {"name": "Cover_Letter", "start": 0, "end": 0},
    {"name": "RS_Mujtaba", "start": 1, "end": 1},
    {"name": "TS_Mujtaba", "start": 2, "end": 2},
    {"name": "DS_Mujtaba", "start": 3, "end": 3},
    {"name": "References_List", "start": 4, "end": 4},
	]

# Create a PDF reader
pdf_reader = PyPDF2.PdfReader(input_pdf)

pdf_path = 'jobApp'
os.makedirs(pdf_path, exist_ok=True)

# Iterate through the sections and extract them
for section in sections:
    pdf_writer = PyPDF2.PdfWriter()
    for page_num in range(section["start"], section["end"] + 1):
        page = pdf_reader.pages[page_num]
        pdf_writer.add_page(page)

    output_pdf = os.path.join(pdf_path, f"{section['name']}.pdf")
    with open(output_pdf, "wb") as output_file:
        pdf_writer.write(output_file)

print("PDF sections extracted successfully!")

os.remove(input_pdf)
print("PDF deleteted!")

# pip install PyPDF2
