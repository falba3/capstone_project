import streamlit as st
from database_functions import query_database
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()


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

        # Prepare the SQL INSERT query based on the role
        if role == "Donor":
            table_name = "OrganDonors"
        else:
            table_name = "OrganPatients"

        insert_query = f"""
                    INSERT INTO {table_name} (
                        role, name, date_of_birth, gender, email, phone, height, weight, blood_type,
                        conditions, infections, organs
                    )
                    VALUES ('{role}', '{name}', '{str(date_of_birth)}', '{gender}', '{email}', '{phone}', 
                            {height}, {weight}, '{blood_type}', '{conditions}', '{infections}', '{", ".join(organs)}')
                """

        # Call query_database to insert data
        result = query_database(insert_query)

        if result is None:
            st.error("There was an error inserting the data into the database.")
        else:
            st.success("Data inserted into the database successfully!")
