from pathlib import Path  # Library for handling file paths in a platform-independent way.
import os  # Module for interacting with the operating system (e.g., paths, directories).
import PyPDF2  # Library for working with PDF files (e.g., reading and extracting text).
from services.data.doc_extraction import extract_pdf_data  # Function to extract data from PDFs.
from services.data.image_analysis import analyse_pdf  # Function to analyze PDFs for image-based content.
from crew.crew import document_summary  # Function to summarize text or document content.
from services.data.split_txt import split_text_file  # Function to split large text files into smaller parts.
from utils.helpers import format_response_success, format_response_fail  # Utility functions for formatting success and failure responses.

# Function to extract data from PDF files.
def pdf_extraction(file):
    """
    Extracts data from a PDF file, summarizes the content, and provides file metadata.

    Args:
        token (str): Authorization token for validation.
        file (Path): Path to the PDF file.

    Returns:
        dict: A success response with summary, file size, number of tokens, and character count.
        tuple: A failure response with error message and HTTP status code 400 on failure.
    """
    print("this is the file :",file)  # Debugging statement to check the file being processed.
    parsing_mode = analyse_pdf(file)
    print("this is the parsing mode :",parsing_mode)  # Determine the parsing mode ('lattice' or 'stream') based on PDF analysis.
    try:
        pdf_extract_output = extract_pdf_data(str(file), parsing_mode)  # Attempt to extract data from the PDF using the determined mode.
        print("this is the pdf extract output :",pdf_extract_output)  # Print the output of the extraction for debugging.
    except Exception as e:  # Handle exceptions that occur during extraction.
        if e == 'No tables found in the PDF.':  # Specific exception for missing tables.
            if parsing_mode == 'lattice':  # If the initial mode was 'lattice', switch to 'stream' mode.
                try:
                    pdf_extract_output = extract_pdf_data(str(file), 'stream')
                except Exception as e:  # Handle errors for the 'stream' mode.
                    return format_response_fail(f"Error: {str(e)}"), 400
            else:  # If the initial mode was 'stream', switch to 'lattice' mode.
                try:
                    pdf_extract_output = extract_pdf_data(str(file), 'lattice')
                except Exception as e:  # Handle errors for the 'lattice' mode.
                    return format_response_fail(f"Error: {str(e)}"), 400

    split_text_file(pdf_extract_output)  # Split the extracted text into smaller files for processing.
    with open(pdf_extract_output, 'r') as output:  # Open the output text file.
        pdf_extract_output = output.read() # Read the extracted content.
    pdf_extract_output_json = document_summary(pdf_extract_output)  # Summarize the first 10,000 characters of the extracted content.
    size_of_uploaded_pdf_file = os.path.getsize(str(file))/1000  # Calculate the size of the uploaded PDF file in KB.
    num_chars = sum(len(page.extract_text()) for page in PyPDF2.PdfReader(str(file)).pages)  # Calculate the total number of characters in the PDF.
    number_of_tokens = num_chars / 4  # Estimate the number of tokens based on character count.
    return format_response_success({  # Return a success response with extracted details.
        'summary': pdf_extract_output_json
    })


