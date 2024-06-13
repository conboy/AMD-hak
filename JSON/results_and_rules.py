import pandas as pd

# Read the combined_results.csv into a DataFrame
combined_df = pd.read_csv('combined_results.csv')

# Read the flattened_rules.csv into a DataFrame
flattened_rules_df = pd.read_csv('flattened_rules.csv')

# Perform a left outer join on the 'id' column
merged_df = pd.merge(combined_df, flattened_rules_df, on='ruleId', how='left')

# Save the resulting DataFrame to a new CSV file
merged_df.to_csv('merged_results.csv', index=False)

print("Files have been successfully merged and saved to 'merged_results.csv'")
