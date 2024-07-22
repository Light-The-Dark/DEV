#TODO remove first row with label. Get it to work!!!

import pandas as pd

original = "Priority/Original.xlsx"
converted = "Priority/converted.xlsx"


def expand_excel_rows(input_file, output_file):
    try:
        # Read the original Excel file
        df = pd.read_excel(input_file)
        
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
        
        # Write the expanded DataFrame to a new Excel file
        expanded_df.to_excel(output_file, index=False)
        print(f"File written successfully to {output_file}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

def rearrange_and_expand_rows(input_file, output_file):
    try:
        # Read the Excel file into a DataFrame
        df = pd.read_excel(input_file)
        
        # Define the desired column sets for each continuation
        column_sets = [
            ['OrderID', 'CustomerName', 'OrderDate', 'ItemNumber', 'RecieptNumber', 'TransactionID', 'store'],
            ['ItemNumber', 'sku', 'qty', 'qty', 'price'],
            ['qty', 'price', 'OrderDate'],
            ['qty', 'Email Address'],
            ['OrderID']
        ]
        
        dict = {}
        j = 0


        for num in range(10):
            df[num] = None  # Add new columns with default value



        for _, row in df.iterrows():
        # Iterate over each column in the row
            if row["Index"] == 1:
                for col in row.index:
                # Add the column name as the key and the corresponding value as the value
                    dict[col] = row[col]
            for i, column_set in enumerate(column_sets):
                if row["Index"] == i + 1:  # Match the index to the appropriate column set
                    for col in column_set:
                        df.iat[row["Index"], j] = dict[col]  # Use `iat` for integer-based indexing
                        j += 1

            if row["Index"] == 5:
                j = 0

        print(df)


        # Write the expanded DataFrame to a new Excel file
        df.to_excel(output_file, index=False)
        print(f"File written successfully to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")





# expand_excel_rows(original, converted)
rearrange_and_expand_rows(converted,converted)


