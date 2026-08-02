import pandas as pd

def extract_data(filepath):
    """Extract raw loan data from CSV"""
    df = pd.read_csv(filepath)
    print(f"Extracted {len(df)} rows")
    return df

if __name__ == "__main__":
    df = extract_data("data/raw/loan_data.csv")
    df.to_parquet("data/staging/loan_data_raw.parquet", index=False)
