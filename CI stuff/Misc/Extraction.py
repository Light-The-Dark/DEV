import pandas as pd

# Load the CSV file
file = "123.xlsx"
excel_file_path = f'C:/Users/Aharon/Downloads/{file}'
df = pd.read_excel(excel_file_path)


import pandas as pd

# Load the Excel file
path = r"Misc"
file = "123.xlsx"
excel_file_path = f'C:/Users/Aharon/Downloads/{file}'

# Read the Excel file
df = pd.read_excel(excel_file_path)

# Extract the number that follows 'ICCID' and store it in a new column 'ICCID_Number'
df['ICCID_Number'] = df.apply(lambda row: row.astype(str).str.extract(r'ICCID\s*(\d+)', expand=False).dropna(), axis=1).bfill(axis=1).iloc[:, 0]

# Remove the .0 from the numbers in the second column (if any), ensuring they are treated as integers
df.iloc[:, 1] = df.iloc[:, 1].fillna('').apply(lambda x: str(int(float(x))) if x != '' and x != 'nan' else x)

# Update the first column by appending 'hello_world/' with the value from the second column
df.iloc[:, 0] = 'https://cellularisrael.com/admin_ci613/sales/order/view/order_id/' + df.iloc[:, 1].astype(str)

# Drop rows where no ICCID was found
df_iccid = df.dropna(subset=['ICCID_Number'])

# Save the updated DataFrame to a new Excel file
output_file_path = f'C:/Users/Aharon/Downloads/combined_functionality.xlsx'
df_iccid.to_excel(output_file_path, index=False)

print(f"File saved to {output_file_path}")





