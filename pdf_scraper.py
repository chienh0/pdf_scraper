import PyPDF2
import tabula
import pandas as pd


def extract_table_from_pdf(file_path):
    # Open the PDF file
    with open(file_path, 'rb') as file:
        # Initialize a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)
        
        # Get the number of pages in the PDF
        num_pages = len(pdf_reader.pages)
        
        # Create an empty list to store the table data
        table_data = []
        
        # Loop through each page in the PDF
        for page_number in range(num_pages):
            # Read the table data from the current page using tabula-py
            current_page_tables = tabula.read_pdf(file_path, pages=page_number+1, multiple_tables=True)
            
            # Append the table data to the list
            table_data.extend(current_page_tables)
    
    # Concatenate the tables into a single dataframe
    df = pd.concat(table_data)
    
    return df

pdf_file = '/Users/chienho/my_dev/projects/pdf_scraper/publication-msr-hb-accident-health.pdf'
dataframe = extract_table_from_pdf(pdf_file)


