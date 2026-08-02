import pandas as pd
from sqlalchemy import create_engine
from schema import loan_schema

def transform_data(df):
    """Validate + Feature engineering"""
    validated_df = loan_schema.validate(df)
    
    validated_df['income_to_loan_ratio'] = validated_df['income'] / validated_df['loan_amount']
    validated_df['is_high_risk'] = (validated_df['credit_score'] < 650).astype(int)
    
    validated_df = validated_df.fillna(validated_df.median(numeric_only=True))
    print("Transformation complete")
    return validated_df

def load_to_sql(df, db_path="sqlite:///data/warehouse/credit_risk.db"):
    """Load to SQL database"""
    engine = create_engine(db_path)
    df.to_sql('credit_risk_clean', engine, if_exists='replace', index=False)
    print(f"Loaded {len(df)} rows to database")

if __name__ == "__main__":
    df = pd.read_parquet("data/staging/loan_data_raw.parquet")
    df_clean = transform_data(df)
    load_to_sql(df_clean)
