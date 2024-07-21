import pandas as pd

original = "Priority/Original.xlsx"
converted = "Priority/converted.xlsx"

# df = pd.read_excel(file)

def expand_excel_rows(input_file, output_file):
    try:
        # Read the original Excel file
        df = pd.read_excel(input_file, engine='openpyxl')
        
        # Create a new DataFrame to hold the expanded rows
        expanded_rows = []

        # Iterate over each row in the original DataFrame
        for _, row in df.iterrows():
            # Create 5 rows for each original row
            for i in range(1, 6):
                if i == 1:
                    # The first row contains the data
                    new_row = row.copy()
                else:
                    # Subsequent rows are empty except for the index
                    new_row = pd.Series(index=row.index, dtype='object')
                
                # Set the index
                new_row['Index'] = i
                expanded_rows.append(new_row)

        # Convert the list of expanded rows back into a DataFrame
        expanded_df = pd.DataFrame(expanded_rows)

        # Reorder the columns to ensure 'Index' is the first column
        cols = ['Index'] + [col for col in df.columns if col != 'Index']
        expanded_df = expanded_df[cols]

        # Remove the first row with labels
        expanded_df = expanded_df.iloc[1:]
        
        # Write the expanded DataFrame to a new Excel file
        expanded_df.to_excel(output_file, index=False)
        print(f"File written successfully to {output_file}")
    
    except Exception as e:
        print(f"An error occurred: {e}")



expand_excel_rows(original, converted)
