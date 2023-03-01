import PyPDF2
import re
import os

# Open the PDF file in binary mode
with open("C:\\Users\\h02si\\Downloads\\BUDGET MANUAL FINAL -15-11-22.pdf", 'rb') as pdf_file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    # Get the number of pages in the PDF file
    num_pages = pdf_reader.getNumPages()
    #Create variables to store the section heading and it's corresponding text
    current_section = ''    # This will store the section heading
    current_text = ''       # This will store the content of the section

    # We create this variable to shorten our if condition later on, when we find out if a new heading is starting
    numbers = ('1.', '2.', '3.', '4.', '5.', '6.', '7.')

    # The 2 lines below create a folder "Chapters" if it doesn't exist in the directory. This folder will store the extracted text
    if not os.path.exists('Chapters'):
        os.makedirs('Chapters')

    # Loop through the chapter pages in the PDF file
    for page_num in range(16,80):
        # Get the current page object
        page_obj = pdf_reader.getPage(page_num)

        # Extract the text from the current page
        page_text = page_obj.extractText()

        # Split the page text into lines
        lines = page_text.split('\n')

        # Loop through each line in the page text
        for line in lines:
          # the if condition below is written by manually seeing the pdf so that different sections can be extracted seperately
          if (line.startswith(numbers) and ((len(line.split(" ")[0])==3) or len(line.split(" ")[0])==4)) or (line.startswith(numbers) and line[4].isalpha()):
            if current_section != '':
              with open(os.path.join('Chapters',current_section + '.txt'), 'w' ,encoding="utf-8") as output_file: 
                output_file.write(current_text)              #Save the output file with the name of the section that was extracted
            else:
              current_section = line
              current_section = re.sub("[^a-zA-Z]",' ',current_section) # Replaces all non-alphabetic characters in section heading with a space.
              current_text = ''

          line = re.sub(r'^\d+\.\d+\.\d+|\d+\.\d+', ' ',line)       # replaces any occurrences of a decimal number seperated by dots
          current_text += line + ' '             # We add the lines to the variable to capture the content of a section
          current_text = current_text.replace('\n', ' ')
          current_text = " ".join(current_text.split())