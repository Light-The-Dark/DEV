# TODO: incoming_calls_only - remove all outgoing calls
# TODO: Detailed stats. IL to IL, IL to non-IL, non-IL to non-IL, non-IL to IL
# NOTE: All numbers are filtered by answer only.

import pandas as pd
from datetime import time

# Load the CSV file
path = r"PBX reports"
file = "cdr__1726409904ci.pbx.avipc.net.csv"
csv_file_path = f'C:/Users/Aharon/Downloads/{file}'
df = pd.read_csv(csv_file_path)

# Counts how many times someone called a IL/non IL number
def did_number_count(df):
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

        # if not df_starts_with_972.empty:
        #     Save the filtered DataFrame to a new CSV file
        #     starts_with_972_csv_file_path = path + '972_did.csv'
        #     df_starts_with_972.to_csv(starts_with_972_csv_file_path, index=False)

        #     print(f"The 'did' numbers starting with '972' have been saved as {starts_with_972_csv_file_path}.")
        # else:
        #     print("No 'did' numbers found starting with '972'.")
    else:
        print("The 'did' column does not exist in the CSV file.")

# Sorts by call destination number
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
        # sorted_csv_file_path = path + 'sorted_path_to_your_file.csv'
        # df_sorted.to_csv(sorted_csv_file_path, index=False)

        # print(f"The sorted CSV file has been saved as {sorted_csv_file_path}.")
        print("\nCounts of each number in the 'did' column:")

        # Format the numbers to avoid scientific notation
        with pd.option_context('display.float_format', '{:,.0f}'.format):
            print(counts)
    else:
        print("The 'did' column does not exist in the CSV file.")

# Summarizes source calls from IL and non IL
def answered_calls(df):
    # Check if the 'clid' column exists in the DataFrame
    if 'clid' in df.columns:
        # Convert the 'clid' column to string
        df['clid'] = df['clid'].astype(str)

        # Drop any rows where 'clid' is NaN (optional, depends on your data)
        df = df.dropna(subset=['clid'])

        # Remove leading non-digit characters
        df['cleaned_clid'] = df['clid'].str.extract(r'(\d+)')

        # Check if the first three digits are '972'
        df['starts_with_972'] = df['cleaned_clid'].str[:3] == '972'

        # Count how many non-null 'clid' numbers do not start with '972'
        count_does_not_start_with_972 = df[df['cleaned_clid'].notnull() & ~df['starts_with_972']].shape[0]

        # Filter the DataFrame to include only rows where starts_with_972 is True
        df_filtered = df[df['starts_with_972']]

        # Save the updated DataFrame to a new CSV file
        # updated_csv_file_path = path + 'IL_numbers.csv'
        # df_filtered.to_csv(updated_csv_file_path, index=False)

        total = count_does_not_start_with_972 + df_filtered.shape[0]
        # Print the summary of how many numbers started with '972'
        print(f"{df_filtered.shape[0]} numbers from IL.")
        print(f"{count_does_not_start_with_972} numbers from chul.")
        print(f"{total} numbers total.")
    else:
        print("The 'clid' column does not exist in the CSV file.")


def sort_cs_tech(df):
    if 'cnam' in df.columns:
        # Convert the 'cnam' column to string
        df['cnam'] = df['cnam'].astype(str)

        # Drop any rows where 'cnam' is NaN (optional, depends on your data)
        df = df.dropna(subset=['cnam'])

        # Counts total "Tech" and "CS"
        tech_count = df['cnam'].str.contains('Tech', case=False, na=False).sum()
        cs_count = df['cnam'].str.contains('CS', case=False, na=False).sum()

        print(f"Total Tech/CS calls: {tech_count + cs_count}")
        print(f"Total Tech count: {tech_count}")
        print(f"Total CS count: {cs_count}")

def analyze_call_times(df):
    # Convert 'calldate' to datetime type
    df['calldate'] = pd.to_datetime(df['calldate'])
    
    # Define time ranges
    time_ranges = {
        'morning': (time(9, 30), time(14, 0)),
        'afternoon': (time(14, 1), time(22, 0)),
        'night': (time(22, 1), time(9, 29))
    }

    # Define search terms
    search_terms = ['Tech', 'CS', 'Hebrew Tech', 'Hebrew CS']

    results = {}

    for term in search_terms:
        results[term] = {range_name: 0 for range_name in time_ranges}

    for range_name, (start, end) in time_ranges.items():
        if start < end:
            mask = (df['calldate'].dt.time >= start) & (df['calldate'].dt.time <= end)
        else:
            mask = (df['calldate'].dt.time >= start) | (df['calldate'].dt.time <= end)

        for term in search_terms:
            count = df[mask]['cnam'].str.contains(term, case=False, na=False).sum()
            results[term][range_name] = count

    # Print results
    for term in search_terms:
        print(f"\n{term} counts:")
        for range_name, count in results[term].items():
            print(f"  {range_name.capitalize()}: {count}")

# sort_number(df)
# did_number_count(df)
# answered_calls(df)
# sort_cs_tech(df)
analyze_call_times(df)