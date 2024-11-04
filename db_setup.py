# db_setup.py

import sqlite3
import os
from config import DB_PATH

def create_table():
    # Ensure the directory exists
    db_directory = os.path.dirname(DB_PATH)
    if not os.path.exists(db_directory):
        os.makedirs(db_directory)
    
    # Connect to the SQLite database
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS leads (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        accepts_financial_aid TEXT,
        accepts_financial_aid_flag TEXT,
        ages_served TEXT,
        capacity INTEGER,
        certificate_expiration_date DATE,
        city TEXT,
        address1 TEXT,
        address2 TEXT,
        company TEXT,
        phone TEXT,
        phone2 TEXT,
        county TEXT,
        curriculum_type TEXT,
        email TEXT,
        first_name TEXT,
        language TEXT,
        last_name TEXT,
        license_status TEXT,
        license_issued DATE,
        license_number INTEGER,
        license_renewed DATE,
        license_type TEXT,
        licensee_name TEXT,
        max_age INTEGER,
        min_age INTEGER,
        operator TEXT,
        provider_id TEXT,
        schedule TEXT,
        state TEXT,
        title TEXT,
        website_address TEXT,
        zip TEXT,
        facility_type TEXT,
        source TEXT,
        etl_timestamp DATE,
        is_duplicate BOOLEAN
    )
    ''')
    conn.commit()
    conn.close()