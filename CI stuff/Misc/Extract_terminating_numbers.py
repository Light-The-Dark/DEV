import pandas as pd
from datetime import datetime, timedelta

# Load the CSV file
df = pd.read_csv(r'C:\Users\Aharon\Downloads\Virtual number report 9.25.24 - Active X2one 8.24.csv')

# Filter rows where the 'Action' column contains the keyword 'terminate'
filtered_df = df[df['Action'].str.contains('terminate', case=False, na=False)]

# Step 1: Add an incrementing ID starting at 12000
# filtered_df['id'] = range(12000, 12000 + len(filtered_df))

# Step 2: Extract the phone number
filtered_df['phone_number'] = filtered_df['number'].apply(lambda x: str(int(float(x))) if pd.notnull(x) else '')

# Step 3: Extract the country
filtered_df['country'] = filtered_df['Country']

# Step 4: Extract the area code
filtered_df['area_code'] = filtered_df['area code'].apply(lambda x: str(int(float(x))) if pd.notnull(x) else '')

# Step 5: Extract the prefix
filtered_df['prefix'] = filtered_df['prefix'].apply(lambda x: str(int(float(x))) if pd.notnull(x) else '')

# Assuming filtered_df is already defined and contains your processed data
# Add the current date minus one year twice
one_year_ago = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')

# Add new columns to the DataFrame
filtered_df['date1'] = one_year_ago
filtered_df['date2'] = one_year_ago

filtered_df['status'] = filtered_df['status']
filtered_df['provider_id'] = "6"


output_df = filtered_df[['prefix', 'area_code', 'phone_number', 'country', 'date1', 'date2', 'status', 'provider_id']]

formatted_rows = []
for index, row in output_df.iterrows():
    formatted_row = f"('{row['prefix']}', '{row['area_code']}', '{row['phone_number']}', '{row['country']}', '{row['date1']}', '{row['date2']}', '{row['status']}', '{row['provider_id']}')"
    formatted_rows.append(formatted_row)

# Join the formatted rows into a single string with a newline
output = ",\n".join(formatted_rows)

# Save to a text file
with open('formatted_output.txt', 'w') as f:
    f.write(output)

print(output)  # Optionally print to the console

# Save the processed data to a new CSV file (optional)
# filtered_df[['id', 'prefix', 'area_code', 'phone_number', 'country', 'date1', 'date2', 'status', 'provider_id']].to_csv('processed_output.csv', index=False)

# Alternatively, continue processing for database insertion...

