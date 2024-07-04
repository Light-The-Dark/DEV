import pandas as pd

# Load the CSV file
path = r"CI stuff/"
file = "cdr__1719988075ci.pbx.avipc.net.csv"
csv_file_path = f'C:/Users/Aharon/Downloads/{file}'
df = pd.read_csv(csv_file_path)


def count_number_called(df):
    # Check if the 'did' column exists in the DataFrame
    if 'did' in df.columns:
        # Convert the 'did' column to string
        df['did'] = df['did'].astype(str)

        # Remove leading non-digit characters
        df['cleaned_did'] = df['did'].str.extract(r'(\d+)')

        # Check if the first three digits are '972'
        df['starts_with_972'] = df['cleaned_did'].str[:3] == '972'

        # Count how many 'did' numbers start with '972'
        count_starts_with_972 = df[df['starts_with_972']].shape[0]

        # Count how many non-null 'did' numbers do not start with '972'
        count_does_not_start_with_972 = df[df['cleaned_did'].notnull() & ~df['starts_with_972']].shape[0]

        # Print the summary
        print(f"Summary:")
        print(f"Numbers starting with '972': {count_starts_with_972}")
        print(f"Numbers not starting with '972': {count_does_not_start_with_972}")

        # Filter the DataFrame to include only rows where 'did' starts with '972'
        df_starts_with_972 = df[df['starts_with_972']]

        if not df_starts_with_972.empty:
            # Save the filtered DataFrame to a new CSV file
            starts_with_972_csv_file_path = path + 'starts_with_972_did.csv'
            df_starts_with_972.to_csv(starts_with_972_csv_file_path, index=False)

            print(f"The 'did' numbers starting with '972' have been saved as {starts_with_972_csv_file_path}.")
        else:
            print("No 'did' numbers found starting with '972'.")
    else:
        print("The 'did' column does not exist in the CSV file.")

def sort_number(df):
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










# sort_number(df)
# count_number_called(df)
