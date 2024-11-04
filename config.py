
import os

# Database configuration
DB_PATH = os.path.join("db", "leads.db")

# Data files
DATA_FILES = [
    "data/source1.csv",
    "data/source2.csv",
    "data/source3.csv"
]

# Mapping of source-specific column names to standardized schema names

COLUMN_MAPPING = {
    'licensee_name': ['Primary Contact Name'],
    'company': ['Company'],
    'license_type': ['Credential Type', 'Type License'],
    'license_number': ['Credential Number', 'Subsidy Contract Number', 'Facility ID', 'Agency Number'],
    'license_status': ['Status'],
    'certificate_expiration_date': ['Expiration Date'],
    'license_issued': ['First Issue Date', 'Issue Date', 'License Monitoring Since'],
    'address1': ['Address', 'Address1'],
    'address2': ['Address2'],
    'city': ['City'],
    'state': ['State'],
    'zip': ['Zip'],
    'county': ['County'],
    'phone': ['Phone'],
    'email': ['Email', 'Email Address'],
    'facility_type': ['Type'],
    'accepts_financial_aid': ['Accepts Subsidy', 'Subsidy Contract Number'],
    'capacity': ['Total Cap', 'Capacity'],
    'ages_served': ['Ages Accepted 1', 'AA2', 'AA3', 'AA4'],
    'operator': ['Primary Caregiver'],
    'schedule': ['Mon', 'Tues', 'Wed', 'Thurs', 'Friday', 'Saturday', 'Sunday'],
    'website_address': ['Website'],
    'provider_id': ['Operation'],
    }

# Target columns for the database schema
TARGET_COLUMNS = [
    'accepts_financial_aid', 'accepts_financial_aid_flag','ages_served', 'capacity', 'certificate_expiration_date', 'city', 'address1',
    'address2', 'company', 'phone', 'phone2', 'county', 'curriculum_type', 'email', 'first_name', 'language',
    'last_name', 'license_status', 'license_issued', 'license_number', 'license_renewed', 'license_type',
    'licensee_name', 'max_age', 'min_age', 'operator', 'provider_id', 'schedule', 'state', 'title',
    'website_address', 'zip', 'facility_type', 'source', 'etl_timestamp', 'is_duplicate'
]

# Logging configuration
LOG_FILE = os.path.join("logs", "etl_pipeline.log")