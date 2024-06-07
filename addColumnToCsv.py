# It seems there was an issue with the previous code execution. Let's try again with a fresh approach.

# Re-importing necessary libraries
import pandas as pd
import numpy as np

# Define the file path again just to ensure everything is clear and correctly specified
csv_file_path = './funds.csv'

# Attempt to read the CSV file again
try:
    df = pd.read_csv(csv_file_path)

    # Define the asset classes
    asset_classes = ['Equity', 'Fixed Income', 'Alternative', 'Multi-Asset']

    # Randomly assign an asset class to each row
    np.random.seed(42)  # Seed for reproducibility
    df['ASSET CLASS'] = np.random.choice(asset_classes, size=len(df))

    # Specify the path for the modified CSV file
    modified_csv_file_path = './funds_modified.csv'
    df.to_csv(modified_csv_file_path, index=False)

    modified_csv_file_path
except Exception as e:
    print(f"An error occurred: {e}")
