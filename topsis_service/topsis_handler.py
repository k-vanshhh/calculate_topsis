import os
import importlib
import pandas as pd

# Dynamically import the package
topsis = importlib.import_module('Topsis-Vansh-102203021')

def run_topsis(input_file, weights, impacts, output_dir, cleanup_temp=True):
    """
    Run the TOPSIS method and generate both a CSV and Excel output file.
    
    Args:
        input_file (str): Path to the input CSV file.
        weights (str): Weights for TOPSIS (comma-separated).
        impacts (str): Impacts for TOPSIS (comma-separated with + or -).
        output_dir (str): Directory to save the results.
        cleanup_temp (bool): Whether to delete the temporary CSV file after conversion (default: True).
    
    Returns:
        str: Path to the final Excel file.
    
    Raises:
        FileNotFoundError: If the input file does not exist.
        ValueError: If there is an issue generating or converting the output files.
    """
    # Check if input file exists
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file '{input_file}' not found.")

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Temporary CSV output path
    temp_csv_name = f"temp_result_{os.path.basename(input_file).replace('.csv', '')}.csv"
    temp_csv_path = os.path.join(output_dir, temp_csv_name)

    # Final Excel output path
    final_excel_name = f"result_{os.path.basename(input_file).replace('.csv', '')}.xlsx"
    final_excel_path = os.path.join(output_dir, final_excel_name)

    try:
        # Call the TOPSIS function
        topsis.topsis(input_file, weights, impacts, temp_csv_path)

        # Check if the CSV file was created
        if not os.path.exists(temp_csv_path):
            raise ValueError(f"TOPSIS failed to generate the CSV output file: {temp_csv_path}")

        # Read the CSV file and save it as an Excel file
        df = pd.read_csv(temp_csv_path)
        df.to_excel(final_excel_path, index=False)

        # Check if the Excel file was created
        if not os.path.exists(final_excel_path):
            raise ValueError(f"Failed to generate the Excel output file: {final_excel_path}")

        # Optionally delete the temporary CSV file
        if cleanup_temp:
            os.remove(temp_csv_path)

        return final_excel_path

    except Exception as e:
        raise ValueError(f"Error running TOPSIS: {str(e)}")
