import pandas as pd

# Load the CSV file
file_path = "./Toto Winning Numbers.csv"
df = pd.read_csv(file_path)

# Columns to drop
columns_to_drop = [
    "Division 1 Winners","Division 1 Prize", "Division 2 Winners", "Division 2 Prize", "Division 3 Winners",
    "Division 3 Prize", "Division 4 Winners", "Division 4 Prize", "Division 5 Winners",
    "Division 5 Prize", "Division 6 Winners", "Division 6 Prize", "Division 7 Winners", "Division 7 Prize"
]

# Drop the specified columns if they exist in the dataframe
df_cleaned = df.drop(columns=[col for col in columns_to_drop if col in df.columns])

# Save cleaned dataset
cleaned_file_path = "./toto_cleaned_final.csv"
df_cleaned.to_csv(cleaned_file_path, index=False)