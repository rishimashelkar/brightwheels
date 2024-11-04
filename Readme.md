# ETL Pipeline

This project is an ETL pipeline designed to process lead data from multiple sources, transform it, and load it into an SQLite database for querying and analysis.

## Requirements

- Python 3.x
- pandas
- sqlite3

Expected dir structure:
etl_pipeline/
├── etl_pipeline.py       # Main ETL pipeline script
├── config.py             # Configuration settings
├── data/
│   ├── source1.csv       # Data source files
│   ├── source2.csv
│   └── source3.csv
├── db/
│   └── leads.db          # SQLite database
├── logs/
│   └── etl_pipeline.log  # Log file for ETL process
├── README.md             # Documentation
└── requirements.txt      # Dependencies


To install dependencies, use:
pip install -r requirements.txt

1. Set up your environment:
python db_setup.py  # Creates the SQLite database and schema

2. Run the ETL Pipeline:
python etl_pipeline.py

3. Logs are saved in the `logs/etl_pipeline.log` file for review.

## ETL Process

	1. **Extract**: Loads CSV files into Pandas DataFrames, including metadata.
	2. **Transform**: Standardizes data formats, deduplicates, and cleans data.
	3. **Load**: Inserts transformed data into the SQLite database.

## Future Improvements

For scalability:
- Transition to a cloud database like AWS RDS or Redshift for larger datasets.
- Use an orchestration tool like Apache Airflow for managing regular ETL runs.
- Implement QA checks and data validation steps.