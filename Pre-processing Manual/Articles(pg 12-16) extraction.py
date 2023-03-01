import PyPDF2
import re
import os

# Open the PDF file in binary mode
with open("C:\\Users\\h02si\\Downloads\\BUDGET MANUAL FINAL -15-11-22.pdf", 'rb') as pdf_file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    # Get the number of pages in the PDF file
    num_pages = pdf_reader.getNumPages()
    current_section = ''
    current_text = ''
    numbers = tuple([str(i) for i in range(10)])
    

    if not os.path.exists('Annexures'):
        os.makedirs('Annexures')

    # Loop through each page in the PDF file
    for page_num in range(13,18):
        # Get the current page object
        page_obj = pdf_reader.getPage(page_num)

        # Extract the text from the current page
        page_text = page_obj.extractText()

        # Split the page text into lines
        lines = page_text.split('\n')

        for line in lines:
            if line.startswith("Article"):
                if current_section != '':
                    with open(os.path.join('Annexures',current_section + '.txt'), 'w' ,encoding="utf-8") as output_file:
                        output_file.write(current_text)
        
                current_section = line.split(" ")[0] + line.split(" ")[1]
                #current_section = re.sub("[^a-zA-Z]",'',current_section)
                current_text = ''

            line = re.sub(r'^\d+\.\d+\.\d+|\d+\.\d+', ' ',line)
            current_text += line + ' '
            current_text = current_text.replace('\n', ' ')
            current_text = " ".join(current_text.split())