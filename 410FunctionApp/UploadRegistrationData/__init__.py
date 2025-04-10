import logging
import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('UploadRegistrationData function triggered.')

    try:
        # Parse JSON body from request
        req_body = req.get_json()

        role = req_body.get("Role")
        name = req_body.get("Name")
        dob = req_body.get("DOB")
        gender = req_body.get("Gender")
        email = req_body.get("Email")
        phone = req_body.get("Phone")
        height = req_body.get("Height (cm)")
        weight = req_body.get("Weight (kg)")
        blood_type = req_body.get("Blood Type")
        conditions = req_body.get("Medical Conditions")
        infections = req_body.get("Infectious Diseases")
        organs = req_body.get("Organs")

        # Check required fields
        if not all([role, name, email, phone, organs]):
            return func.HttpResponse("Missing required fields.", status_code=400)

        # For now, just log the data and return a success response
        logging.info(f"{role} Registration Received: {name}, {email}, Organs: {organs}")

        return func.HttpResponse(
            f"{role} '{name}' with email '{email}' submitted successfully.",
            status_code=200
        )

    except Exception as e:
        logging.error(f"Error: {e}")
        return func.HttpResponse("Invalid request body.", status_code=400)
