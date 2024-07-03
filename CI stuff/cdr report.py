import pandas as pd

# Load the CSV file
path = r"CI stuff/"
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

    # Save the counts to a new CSV file
    counts_csv_file_path = path + 'counts_path_to_your_file.csv'
    counts.to_csv(counts_csv_file_path, header=['count'])

    print(f"The counts CSV file has been saved as {counts_csv_file_path}.")
    print("\nCounts of each number in the 'did' column:")

    # Format the numbers to avoid scientific notation
    with pd.option_context('display.float_format', '{:,.0f}'.format):
        print(counts)
else:
    print("The 'did' column does not exist in the CSV file.")


# Check if the 'clid' column exists in the DataFrame
if 'clid' in df.columns:
    # Convert the 'clid' column to string
    df['clid'] = df['clid'].astype(str)

    # Remove leading non-digit characters
    df['cleaned_clid'] = df['clid'].str.extract('(\d+)')

    # Check if the first three digits are '972'
    df['starts_with_972'] = df['cleaned_clid'].str[:3] == '972'

    # Filter the DataFrame to include only rows where starts_with_972 is True
    df_filtered = df[df['starts_with_972']]

    # Save the updated DataFrame to a new CSV file
    updated_csv_file_path = path + 'IL_numbers.csv'
    df_filtered.to_csv(updated_csv_file_path, index=False)

    # Print the summary of how many numbers started with '972'
    print(f"Summary: {df_filtered.shape[0]} numbers started with '972'.")
else:
    print("The 'clid' column does not exist in the CSV file.")

