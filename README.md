# Credit-Risk-ETL-Pipeline
    End-to-end ETL pipeline with data validation for credit risk data using Pandas, Pandera, and SQLAlchemy.
    
    ## Tech Stack
    Python | Pandas | Pandera | SQLAlchemy | Git
    
    ## How to Run
    ```bash
    pip install -r requirements.txt
    python extract.py
    python transform_load.py

    ## What it does
- **Extract**: Reads loan data from CSV
- **Transform**: Validates data with Pandera schemas, handles type coercion
- **Load**: Stores clean data in SQLite database using SQLAlchemy

## Key Learning
Implemented data validation in an ETL pipeline to catch data quality issues before loading to warehouse.
