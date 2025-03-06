import pandas as pd
import os

def clean_fama_french_file(input_file: str, output_file: str, date_format: str = '%Y%m') -> None:
    """
    Cleans a raw Fama-French CSV file:
      - Detects the header row (assumed to start with "Date")
      - Removes rows that do not have a valid numeric Date
      - Converts the 'Date' column into a datetime object using the given format
      - Saves the cleaned data to the specified output file
    """
    # Read the file line-by-line to detect the header row.
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    header_index = None
    for i, line in enumerate(lines):
        if line.startswith("Date"):
            header_index = i
            break
            
    if header_index is None:
        raise ValueError(f"Header row starting with 'Date' not found in {input_file}")
    
    # Read CSV from the detected header row.
    df = pd.read_csv(input_file, skiprows=header_index)
    
    # Remove rows with non-numeric Date values (likely footers or notes).
    df = df[pd.to_numeric(df['Date'], errors='coerce').notnull()]
    
    # Convert the Date column to datetime.
    df['Date'] = pd.to_datetime(df['Date'], format=date_format, errors='coerce')
    df = df[df['Date'].notnull()]  # Drop any rows where conversion failed.
    
    # Optionally strip whitespace from column names.
    df.columns = [col.strip() for col in df.columns]
    
    # Save the cleaned DataFrame.
    df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")

def ensure_folder(folder: str) -> None:
    """Ensure that a folder exists; if not, create it."""
    os.makedirs(folder, exist_ok=True)
