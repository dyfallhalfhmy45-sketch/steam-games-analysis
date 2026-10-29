import pandas as pd

# 1. Read CSV File
csv_path = r"C:\Users\dyfal\Downloads\archive\games.csv"
print("Reading file...")
df = pd.read_csv(csv_path)

print("\n================ DATA SUMMARY ================")
print(f"Total Rows (Games): {len(df)}")
print(f"Columns: {list(df.columns)}")

# 2. Basic Statistics
if 'Price' in df.columns:
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce').fillna(0)
    free_count = (df['Price'] == 0).sum()
    paid_count = (df['Price'] > 0).sum()
    
    print(f"\nFree Games: {free_count}")
    print(f"Paid Games: {paid_count}")
    print(f"Average Price (Paid): ${df[df['Price'] > 0]['Price'].mean():.2f}")
    print(f"Max Price: ${df['Price'].max():.2f}")

# 3. Export to Excel
output_excel = r"C:\Users\dyfal\Downloads\archive\full_games_analysis.xlsx"
df.to_excel(output_excel, index=False)
print(f"\nSUCCESS! File saved to: {output_excel}")