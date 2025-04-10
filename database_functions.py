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
    conn = None
    try:
        # Fetch environment variables for the connection
        server = os.getenv("DB_SERVER")
        database = os.getenv("DB_NAME")
        username = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")

        # Create the connection string
        conn = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            # f"Driver={{SQL Server Native Client 11.0}};"
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
            conn.close()  # Close the connection after fetching the data
            return result
        else:
            # For non-SELECT queries, commit the changes and close the connection
            conn.commit()
            conn.close()  # Ensure connection is closed after committing changes
            return "Query executed successfully"

    except Exception as e:
        # Handle exceptions
        if conn:
            conn.close()  # Ensure connection is closed in case of an error
        print(f"Error: {e}")
        return None





# Old SQL for creating the tables

# # SQL query to create the OrganDonors table
# create_donors_table_query = """
# CREATE TABLE Donors (
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
#     registration_date DATETIME DEFAULT GETDATE(),
#     active BIT NOT NULL DEFAULT 1  -- Active field (1 for active, 0 for inactive)
# );
#
# """
#
# # SQL query to create the OrganPatients table (updated)
# create_patients_table_query = """
# CREATE TABLE Patients (
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
#     registration_date DATETIME DEFAULT GETDATE(),
#     active BIT NOT NULL DEFAULT 1  -- Active field (1 for active, 0 for inactive)
# );
# """

# # SQL query to create the OrganPatients table (updated)
# create_matches_table_query = """
# CREATE TABLE Matches (
#     id INT IDENTITY(1,1) PRIMARY KEY,  -- Primary Key for the Match record
#     donor_id INT NOT NULL,              -- Foreign Key referencing OrganDonors table (donor)
#     patient_id INT NOT NULL,            -- Foreign Key referencing Patients table (patient)
#     risk_score INT,                     -- Risk score (can be negative)
#     match_date DATETIME DEFAULT GETDATE(),  -- Timestamp for when the match was created
#     match_status BIT NOT NULL DEFAULT 0,  -- Boolean field for match status (0 for no match, 1 for match)
#     FOREIGN KEY (donor_id) REFERENCES Donors(id),  -- Linking to the OrganDonors table
#     FOREIGN KEY (patient_id) REFERENCES Patients(id)   -- Linking to the Patients table
# );
# """


# # Run the queries to create the tables
# print(query_database(create_donors_table_query))
# print(query_database(create_patients_table_query))
# print(query_database(create_matches_table_query))
print(query_database("SELECT * FROM Donors"))
