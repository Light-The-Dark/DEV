import pandas as pd

# Load the CSV file
file = "cdr__1719988075ci.pbx.avipc.net.csv"
csv_file_path = f'C:/Users/Aharon/Downloads/{file}'
df = pd.read_csv(csv_file_path)

# Check if the 'did' column exists in the DataFrame
if 'did' in df.columns:
    # Convert the 'did' column to numeric if necessary
    df['did'] = pd.to_numeric(df['did'], errors='coerce')

    # Drop any rows where 'did' is NaN (optional, depends on your data)
    df = df.dropna(subset=['did'])

    # Sort the DataFrame by the 'did' column
    df_sorted = df.sort_values(by='did').reset_index(drop=True)

    # Count the occurrences of each number in the 'did' column
    counts = df_sorted['did'].value_counts().sort_index()

    # Save the sorted DataFrame to a new CSV file
    sorted_csv_file_path = 'sorted_path_to_your_file.csv'
    df_sorted.to_csv(sorted_csv_file_path, index=False)

    print(f"The sorted CSV file has been saved as {sorted_csv_file_path}.")
    print("\nCounts of each number in the 'did' column:")

    # Format the numbers to avoid scientific notation
    with pd.option_context('display.float_format', '{:,.0f}'.format):
        print(counts)
else:
    print("The 'did' column does not exist in the CSV file.")
