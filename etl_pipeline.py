
import pandas as pd
import sqlite3
from datetime import datetime
from config import DATA_FILES, DB_PATH, COLUMN_MAPPING, TARGET_COLUMNS
from logger import get_logger
from db_setup import create_table


logger = get_logger("ETL_Pipeline")

def load_data(file_path, source_name):
	"""Loads CSV data into a DataFrame and adds source information."""
	try:
		df = pd.read_csv(file_path)
		df['source'] = source_name
		df['etl_timestamp'] = datetime.now().isoformat()
		logger.info(f"Loaded data from {file_path}")
		return df
	except Exception as e:
		logger.error(f"Error loading data from {file_path}: {e}")
		return pd.DataFrame()


def split_name(full_name):
	"""Splits full name into first and last name."""
	if pd.isnull(full_name) or not full_name.strip():
		return "", ""  # Handle empty or null names
	parts = full_name.strip().split()
	if len(parts) == 1:
		return parts[0], ""
	elif len(parts) == 2:
		return parts[0], parts[1]
	else:
		return parts[0], " ".join(parts[1:])  # First part as first_name, remaining as last_name

	
def transform_data(df):
	"""Transforms data by standardizing, deduplicating, and mapping columns."""
	
	# Apply column mapping to handle multiple source columns for the same target column
	for target_col, source_cols in COLUMN_MAPPING.items():
		for source_col in source_cols:
			if source_col in df.columns:
				#print(source_col, df.columns)
				df[target_col] = df[source_col]
				break
		df = df.drop(columns=source_cols, errors='ignore')

		# Add Y/N field for accepts_financial_aid based on whether it is populated
		if 'accepts_financial_aid' in df.columns:
			df['accepts_financial_aid_flag'] = df['accepts_financial_aid'].apply(lambda x: 'Y' if pd.notnull(x) and str(x).strip() else 'N')
		else:
			df['accepts_financial_aid_flag'] = 'N'  # Set to 'N' if the column is missing
		
	# Deduplicate records based on phone or address if they exist
	dedup_columns = [col for col in ['phone', 'address1'] if col in df.columns]
	if dedup_columns:
		df['is_duplicate'] = df.duplicated(subset=dedup_columns, keep='first')
	else:
		df['is_duplicate'] = False  # Default to no duplicates if columns are missing
	
	# Standardize text columns to lowercase
	text_columns = ['city', 'county', 'state', 'language', 'title']
	for col in text_columns:
		if col in df.columns:
			df[col] = df[col].str.lower()

	# Split full_name into first_name and last_name
	if 'licensee_name' in df.columns:
		df[['first_name', 'last_name']] = df['licensee_name'].apply(
			lambda x: pd.Series(split_name(x))
		)
		
	# Ensure all target columns are present in the DataFrame
	for col in TARGET_COLUMNS:
		if col not in df.columns:
			df[col] = None  # Fill missing columns with None
	
	# Filter to keep only columns in the target schema
	df = df[TARGET_COLUMNS]

	logger.info("Data transformation completed")
	return df


def load_to_db(df):
	"""Loads transformed data into the SQLite database."""
	try:
		conn = sqlite3.connect(DB_PATH)
		df.to_sql('leads', conn, if_exists='append', index=False)
		conn.close()
		logger.info("Data loaded into SQLite database")
	except Exception as e:
		logger.error(f"Error loading data into database: {e}")

def etl_pipeline():
	"""Runs the full ETL process: extract, transform, load."""
	# Step 1: Setup database
	create_table()

	# Step 2: Process each data file
	for file_path in DATA_FILES:
		source_name = file_path.split('/')[-1]
		# Extract
		df = load_data(file_path, source_name)

		if not df.empty:
			# Transform
			df = transform_data(df)
			
			# Load
			load_to_db(df)
	
	logger.info("ETL process completed")

if __name__ == "__main__":
	etl_pipeline()