import pandas as pd
import glob

# List of CSV files to be combined
csv_files = ['results1.csv', 'results2.csv', 'results3.csv', 'results4.csv', 'results5.csv']

# Initialize an empty list to hold the DataFrames
data_frames = []

# Loop through the list of CSV files and read each one into a DataFrame
for file in csv_files:
    df = pd.read_csv(file)
    data_frames.append(df)

# Concatenate all DataFrames in the list into a single DataFrame
combined_df = pd.concat(data_frames, ignore_index=True)

# Save the combined DataFrame to a new CSV file
combined_df.to_csv('combined_results.csv', index=False)

print("CSV files have been combined successfully!")
