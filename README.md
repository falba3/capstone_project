# CapstoneProject
IE University Thesis - Organ Donation in the Cloud

## Overview
- This repository contains the user_registration.py script for a streamlit application.
The application is an interface for user registration of a organ donation platform. 
The streamlit application interacts with Azure Cloud resources in matching and notifying eligble patient-donor pairs.

## Azure Resources
   1. Azure SQL Database 
   2. Azure Logic Apps
      1. One for API interactions to the database
      2. One for the Patients
      3. One for the Donors
   3. Azure Communications Service
      1. Sends out email notifications

## Streamlit Cloud App
- The streamlit cloud app is hosted at this link:
- https://alba-organdonation.streamlit.app