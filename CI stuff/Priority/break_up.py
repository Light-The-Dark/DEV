import pandas as pd

original = "Priority/Original.xlsx"
converted = "Priority/converted2.xlsx"

def split_excel_sheet(input_file, output_file, max_lines_per_sheet=49):
    # Load the Excel file
    df = pd.read_excel(input_file)

    # Calculate the number of sheets needed
    num_sheets = -(-len(df) // max_lines_per_sheet)  # Ceiling division

    # Write each chunk to a new sheet
    with pd.ExcelWriter(output_file) as writer:
        for i in range(num_sheets):
            start_row = i * max_lines_per_sheet
            end_row = start_row + max_lines_per_sheet
            chunk_df = df.iloc[start_row:end_row]
            chunk_df.to_excel(writer, sheet_name=f'Sheet_{i + 1}', index=False)

# Example usage
split_excel_sheet(original, converted)
