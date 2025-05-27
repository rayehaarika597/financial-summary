import os
import random
import fitz
from collections import Counter

def get_mode(string_list):
    """
    Finds the mode of a list of strings.

    Args:
        string_list (list): List of strings.

    Returns:
        list: A list of the most frequent string(s). 
              Multiple strings are returned if there is a tie.
    """
    if not string_list:
        return []

    # Count the occurrences of each string
    counter = Counter(string_list)
    max_count = max(counter.values())
    
    # Find all strings with the maximum count
    mode = [key for key, count in counter.items() if count == max_count]

    return mode

def extract_random_pages_as_images(pdf_path, output_folder, num_pages=5):
    """
    Extracts random pages from a PDF as images.
    
    Args:
        pdf_path (str): Path to the input PDF file.
        output_folder (str): Folder to save the extracted images.
        num_pages (int): Number of random pages to extract.
    """
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Open the PDF
    pdf_document = fitz.open(pdf_path)
    total_pages = len(pdf_document)
    
    if total_pages == 0:
        print("The PDF is empty.")
        return
    
    if num_pages > total_pages:
        print(f"The PDF has only {total_pages} pages. Extracting all available pages.")
        num_pages = total_pages
    
    # Select random pages
    selected_pages = random.sample(range(total_pages), num_pages)
    
    for page_number in selected_pages:
        # Get the page
        page = pdf_document[page_number]
        
        # Render the page as a pixmap
        pix = page.get_pixmap()
        
        # Save the page as an image
        output_path = os.path.join(output_folder, f"page_{page_number + 1}.png")
        pix.save(output_path)
        print(f"Saved page {page_number + 1} as {output_path}")
    
    # Close the PDF document
    pdf_document.close()
