import pyodbc
from dotenv import load_dotenv
import os

load_dotenv()


def query_database(query):
    """
    Connects to the SQL Server database using pyodbc, executes the provided query, and returns the result.

    :param query: SQL query to be executed
    :return: Result of the query or error message
    """
    server = os.getenv("DB_SERVER")
    database = os.getenv("DB_NAME")
    username = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")

    try:
        # Create the connection string
        conn = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={server};'
            f'DATABASE={database};'
            f'UID={username};'
            f'PWD={password}'
        )
        print("Connection successful")

        # Create a cursor and execute the query
        cursor = conn.cursor()
        cursor.execute(query)

        # If the query is a SELECT statement, fetch and return the results
        if query.strip().upper().startswith("SELECT"):
            result = cursor.fetchall()
            return result
        else:
            # If not a SELECT query, commit changes (for INSERT, UPDATE, DELETE, etc.)
            conn.commit()
            return "Query executed successfully"

    except Exception as e:
        print(f"Error: {e}")
        return None

    finally:
        # Close the connection
        conn.close()



# Old SQL for creating the tables

# # SQL query to create the OrganDonors table
# create_donors_table_query = """
# CREATE TABLE OrganDonors (
#     id INT IDENTITY(1,1) PRIMARY KEY,
#     role VARCHAR(50) NOT NULL,
#     name VARCHAR(100) NOT NULL,
#     date_of_birth DATE NOT NULL,
#     gender VARCHAR(20) NOT NULL,
#     email VARCHAR(100) NOT NULL,
#     phone VARCHAR(20) NOT NULL,
#     height INT NOT NULL,
#     weight INT NOT NULL,
#     blood_type VARCHAR(5) NOT NULL,
#     conditions TEXT,
#     infections TEXT,
#     organs VARCHAR(255) NOT NULL,  -- A comma-separated list of organs willing to donate
#     registration_date DATETIME DEFAULT GETDATE()
# );
# """
#
# # SQL query to create the OrganPatients table (updated)
# create_patients_table_query = """
# CREATE TABLE OrganPatients (
#     id INT IDENTITY(1,1) PRIMARY KEY,
#     role VARCHAR(50) NOT NULL,
#     name VARCHAR(100) NOT NULL,
#     date_of_birth DATE NOT NULL,
#     gender VARCHAR(20) NOT NULL,
#     email VARCHAR(100) NOT NULL,
#     phone VARCHAR(20) NOT NULL,
#     height INT NOT NULL,
#     weight INT NOT NULL,
#     blood_type VARCHAR(5) NOT NULL,
#     conditions TEXT,
#     infections TEXT,
#     organs VARCHAR(255) NOT NULL,  -- A comma-separated list of organs required
#     registration_date DATETIME DEFAULT GETDATE()
# );
# """
#
# # Run the queries to create the tables
# print(query_database(create_donors_table_query))
# print(query_database(create_patients_table_query))