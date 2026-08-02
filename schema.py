from pandera import DataFrameSchema, Column, Check
import pandas as pd

loan_schema = DataFrameSchema(
    {
        "loan_id": Column(int, nullable=False),
        "income": Column(float, Check.ge(0), coerce=True),  # coerce=True fixes it
        "loan_amount": Column(float, Check.ge(0), coerce=True),
        "credit_score": Column(int, Check.in_range(300, 850)),
        "employment_years": Column(float, Check.ge(0), coerce=True),
        "debt_to_income": Column(float, Check.in_range(0, 1))
    },
    strict=True
)