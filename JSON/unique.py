import pandas as pd

# List of CSV file names
csv_files = ['merged_results.csv']

# Dictionary to store the count of entries for each file
entry_counts = {}
total = 0
# Loop through each file and count the entries
for file in csv_files:
    try:
        df = pd.read_csv(file)
        entry_counts[file] = len(df)
        total+= len(df)
    except Exception as e:
        entry_counts[file] = f"Error reading file: {e}"

# Print the counts
for file, count in entry_counts.items():
    print(f"{file}: {count} entries")
print(total)