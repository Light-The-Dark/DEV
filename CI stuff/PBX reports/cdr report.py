# TODO: Detailed stats. IL to IL, IL to non-IL, non-IL to non-IL, non-IL to IL
# NOTE: All numbers are filtered by answer only.

import pandas as pd
from datetime import time

# Load the CSV file
path = r"PBX reports"
file = "cdr__1730611959ci.pbx.avipc.net.csv"
csv_file_path = f'C:/Users/Aharon/Downloads/{file}'
virtual_number_path = r"C:\Users\Aharon\Downloads\Virtual numbers.csv"
df = pd.read_csv(csv_file_path)
vn_file = pd.read_csv(virtual_number_path)

# Counts how many times someone called an IL/non IL number
def did_number_count(df):
    print("\n\n########################################################\nDID NUMBER COUNT")
    print("How many times we received a phone call to one of our IL/non IL numbers\n\n")
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
        print(f"Numbers customer called starting with '972': {count_starts_with_972}")
        print(f"Numbers customer called not starting with '972': {count_does_not_start_with_972}")

        # Filter the DataFrame to include only rows where 'did' starts with '972'
        # df_starts_with_972 = df[df['starts_with_972']]

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
    print("\n\n########################################################\nSORT NUMBER")
    print("Sorts numbers by which number the customer called\n\n")
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
        print("\nCounts of each number in the 'did' column:")

        # Format the numbers to avoid scientific notation
        with pd.option_context('display.float_format', '{:,.0f}'.format):
            print(counts)
    else:
        print("The 'did' column does not exist in the CSV file.")

# Splits calls based on time of day and totals Sales, CS, Tech
def analyze_calls(df):
    print("\n\n########################################################\nANALYZE CALLS")
    print("Analyze the time calls were made and to which department\n\n")
    # Convert 'calldate' to datetime type
    df['calldate'] = pd.to_datetime(df['calldate'])
    
    # Define time ranges
    time_ranges = {
        'morning': (time(9, 30), time(14, 0)),
        'afternoon': (time(14, 1), time(22, 0)),
        'night': (time(22, 1), time(9, 29))
    }

    # Define search terms
    search_terms = ['Sales - English', 'CS - English', 'Tech - English', 'Sales - Hebrew', 'CS - Hebrew', 'Tech - Hebrew']

    results = {}

    for term in search_terms:
        results[term] = {range_name: 0 for range_name in time_ranges}
        results[term]['total'] = 0  # Add a total for each term

    for range_name, (start, end) in time_ranges.items():
        if start < end:
            mask = (df['calldate'].dt.time >= start) & (df['calldate'].dt.time <= end)
        else:
            mask = (df['calldate'].dt.time >= start) | (df['calldate'].dt.time <= end)

        for term in search_terms:
            count = df[mask]['cnam'].str.contains(term, case=False, na=False).sum()
            results[term][range_name] = count
            results[term]['total'] += count  # Add to the total

    # Print results
    for term in search_terms:
        print(f"\n{term} counts:")
        for range_name, count in results[term].items():
            print(f"  {range_name.capitalize()}: {count}")

    
    # Calculate and print totals
    categories = ['Sales', 'CS', 'Tech']
    print("\n\n\n\nTotals:")
    for category in categories:
        english_total = results[f'{category} - English']['total']
        hebrew_total = results[f'{category} - Hebrew']['total']
        total = english_total + hebrew_total
        print(f"  {category}:")
        print(f"    English: {english_total}")
        print(f"    Hebrew: {hebrew_total}")
        print(f"    Total: {total}")

# Summarizes source calls from IL and non IL. Virtual numbers are considered IL even if non IL
def answered_calls(df, virtual_numbers_file):

    print("\n\n########################################################\nANSWERED CALLS")
    print("Summary of calls that were made from IL/non IL. VN's are considered IL even if not starting with 972\n\n")
    if 'clid' not in df.columns:
        print("The 'clid' column does not exist in the CSV file.")
        return

    # Convert the 'clid' column to string and clean it
    df['clid'] = df['clid'].astype(str)
    original_count = df.shape[0]
    df = df.dropna(subset=['clid'])
    after_dropna_count = df.shape[0]

    df['cleaned_clid'] = df['clid'].str.extract(r'(\d+)')
    
    # Check if the first three digits are '972'
    df['starts_with_972'] = df['cleaned_clid'].str[:3] == '972'
    initial_972_count = df['starts_with_972'].sum()
    print(f"Numbers starting with 972: {initial_972_count}")

    # Load additional IL numbers
    try:
        virtual_numbers = set(virtual_numbers_file['number'].astype(str))
        print(f"Loaded {len(virtual_numbers)} virtual numbers")
    except Exception as e:
        print(f"Error loading virtual numbers: {e}")
        virtual_numbers = set()

    # Function to check if a number is in the additional IL numbers list
    def virtual_number(number):
        return number in virtual_numbers
    # Apply the check to all numbers
    df['virtual_number'] = df['cleaned_clid'].apply(virtual_number)
    virtual_number_count = df['virtual_number'].sum()
    print(f"Numbers found in virtual number list: {virtual_number_count}")

    # Determine final IL status (either starts with 972 or is in the additional IL list)
    df['final_is_il'] = df['starts_with_972'] | df['virtual_number']

    # Calculate counts
    il_count = df['final_is_il'].sum()
    non_il_count = df.shape[0] - il_count

    print("\nFinal Results:")
    print(f"(Source call) {il_count} numbers from IL.")
    print(f"(Source call) {non_il_count} numbers from chul.")
    total = il_count + non_il_count
    print(f"(Source call) {total} numbers total.")



did_number_count(df)
sort_number(df)
analyze_calls(df)
answered_calls(df, vn_file)