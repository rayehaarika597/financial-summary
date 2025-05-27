import os
import camelot
from camelot import read_pdf
import pandas as pd
from pathlib import Path


def extract_pdf_data(pdf_file, parsing_mode="lattice"):
    """
    Extracts table data from a PDF and saves it as a CSV file named as `token_<token_number>_<filename>_extracted.csv`.

    Parameters:
        pdf_file (str): Path to the input PDF file.
        token_number (str): A user-provided token number for naming the output file.
        parsing_mode (str): Either 'lattice' or 'stream' for Camelot parsing.
    """
    try:
        # Extract tables using the specified parsing mode
        tables = camelot.read_pdf(pdf_file, pages="all", flavor='stream')
        if len(tables) == 0:
            print("No tables found in the PDF.")
            return

        # Combine all extracted tables
        combined_data = pd.DataFrame()

        for table in tables:
            df = table.df  # Extract data as DataFrame
            combined_data = pd.concat([combined_data, df], ignore_index=True)

        pdf = Path(pdf_file)
        # Generate the output filename
        base_name = str(pdf.name)
        output_path = Path(f"outputs/extracted_files")
        output_path.mkdir(parents=True, exist_ok=True)
        output_file = output_path / f"{base_name}_extracted.txt"

        # Save combined data to CSV
        combined_data.to_csv(output_file, index=False)

        print(f"Data saved successfully to {output_file}.")
        return output_file

    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
# pdf_path = "table.pdf"  # Replace with your PDF file path
# token_number = "12345"    # Replace with the desired token number
# parsing_mode = "lattice"  # Use 'lattice' for structured tables or 'stream' for loosely structured tables

# extract_pdf_data(pdf_path, token, parsing_mode=parsing_mode)
