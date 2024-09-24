import pandas as pd
from sqlalchemy import create_engine

# Define the MySQL connection
host = "localhost"  # or "127.0.0.1" for the "Practice" connection
username = "root"
password = "jaipathak2005"
database = 'speechcare'
engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@{host}/{database}')

# Path to the .xlsx file
file_path = r"C:\Users\Dell\OneDrive\Desktop\speechcare_hub.xlsx"

# Load the Excel file
excel_data = pd.ExcelFile(file_path)

# Iterate over each sheet in the Excel file
for sheet_name in excel_data.sheet_names:
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    
    # Define the table name based on the sheet name
    table_name = sheet_name

    # Write data to MySQL table
    df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)
    
    print(f"Uploaded sheet '{sheet_name}' to table '{table_name}'")

print("All sheets have been processed.")
