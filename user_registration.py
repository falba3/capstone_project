import streamlit as st
import pandas as pd
import datetime
import pyodbc

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
    organs = st.multiselect("Organs willing to donate", ["Heart", "Kidneys", "Liver", "Lungs", "Pancreas", "Intestines"])
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

        # In a real app, here is where you'd insert the data into Azure SQL Database
        # Example:
        # conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=your_server;DATABASE=your_db;UID=user;PWD=password')
        # cursor = conn.cursor()
        # cursor.execute("INSERT INTO Users (...) VALUES (?, ?, ...)", (...))
        # conn.commit()
        # conn.close()