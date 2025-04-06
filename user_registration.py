import streamlit as st
import pandas as pd
import datetime
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Retrieve the database connection details from environment variables
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
server = os.getenv("DB_SERVER")
database = os.getenv("DB_DATABASE")

# Title
st.title("Organ Donor and Patient Registration")

# Role selection
role = st.selectbox("Registering as:", ["Donor", "Patient"])

# Basic Information
st.header("Personal Information")
name = st.text_input("Full Name")
date_of_birth = st.date_input("Date of Birth")
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
email = st.text_input("Email")
phone = st.text_input("Phone Number")

# Physical Attributes
st.header("Physical Information")
height = st.number_input("Height (cm)", min_value=0)
weight = st.number_input("Weight (kg)", min_value=0)
blood_type = st.selectbox("Blood Type", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])

# Medical History
st.header("Medical History")
conditions = st.text_area("Pre-existing Conditions")
infections = st.text_area("Infectious Diseases (if any)")

# Organ Preferences
st.header("Organ Preferences")
if role == "Donor":
    organs = st.multiselect("Organs willing to donate",
                            ["Heart", "Kidneys", "Liver", "Lungs", "Pancreas", "Intestines"])
else:
    organs = st.multiselect("Organs required", ["Heart", "Kidneys", "Liver", "Lungs", "Pancreas", "Intestines"])

# Consent
st.header("Legal Consent")
consent = st.checkbox("I agree to the terms and consent to share my data for organ donation/transplantation purposes.")

# Submit
if st.button("Submit"):
    if not all([name, email, phone, organs]) or not consent:
        st.warning("Please complete all required fields and give consent.")
    else:
        st.success(f"{role} registered successfully!")

        # Display data
        st.write("### Summary")
        st.json({
            "Role": role,
            "Name": name,
            "DOB": str(date_of_birth),
            "Gender": gender,
            "Email": email,
            "Phone": phone,
            "Height (cm)": height,
            "Weight (kg)": weight,
            "Blood Type": blood_type,
            "Medical Conditions": conditions,
            "Infectious Diseases": infections,
            "Organs": organs
        })

        # # Set up SQLAlchemy engine and connection string
        # username = 'your_username'  # Your database username
        # password = 'your_password'  # Your database password
        # server = 'your_server.database.windows.net'  # Your SQL server name
        # database = 'your_database'  # Your database name
        #
        # # Create the connection string for SQLAlchemy
        # connection_string = f"mssql+pymssql://{username}:{password}@{server}/{database}"
        #
        # # Create SQLAlchemy engine
        # engine = create_engine(connection_string)
        #
        # # Insert data into the SQL Server database
        # with engine.connect() as connection:
        #     # Define the SQL INSERT query
        #     insert_query = """
        #         INSERT INTO organ_registration (
        #             role, name, date_of_birth, gender, email, phone, height, weight, blood_type,
        #             conditions, infections, organs
        #         )
        #         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        #     """
        #
        #     # Prepare data to insert into the query
        #     data = (
        #         role, name, str(date_of_birth), gender, email, phone, height, weight,
        #         blood_type, conditions, infections, ", ".join(organs)
        #     )
        #
        #     # Execute the insert query
        #     connection.execute(insert_query, data)

        st.success("Data inserted into the database successfully!")
