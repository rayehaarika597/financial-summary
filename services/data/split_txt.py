import math
from pathlib import Path


def split_text_file(file_path):
    # Step 1: Convert file_path to a Path object
    print(file_path)
    file_path = Path(file_path)
    if not file_path.exists():
        print(f"Error: The file {file_path} does not exist.")
        return

    # Step 2: Create an output directory with the filename (without extension)
    output_dir = file_path.parent / file_path.stem  # Use stem to get filename without extension
    print(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)  # Create the directory if it doesn't exist

    with file_path.open('r', encoding='utf-8') as file:
        data = file.read()  # Read all lines in the text file

    char_limit = 30000
    # Step 5: Split the text file into parts
    split_files = [
        data[i:i + char_limit]
        for i in range(0, len(data), char_limit)
    ]

    # Step 6: Save each split as a separate text file in the output directory
    for idx, split in enumerate(split_files):
        output_file = output_dir / f"split_{idx + 1}.txt"
        with output_file.open('w', encoding='utf-8') as file:
            file.writelines(split)
        print(f"Saved: {output_file}")



# # Step 1: Load the text file
# file_path = r'D:\marquee magic\prolifics_api_loans\6f582b2f6e26ef844febdf7795f5327f\extracted_files\6f582b2f6e26ef844febdf7795f5327f_ABHUDAY 1-8-19 TO 31-10-19_ABHUDAYA_BANK_extracted.txt'  # Replace with your actual file path
# split_text_file(file_path)
