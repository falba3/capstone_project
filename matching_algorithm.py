def match_donor_patient(patients, donors):
    """
    Matches donors and patients based on blood type and organ requirements.
    This version adds rule-based filtering based on additional fields like conditions and infections.

    :param patients: List of dictionaries, where each dictionary represents a patient.
    :param donors: List of dictionaries, where each dictionary represents a donor.
    :return: List of matched pairs.
    """
    matches = []

    for patient in patients:
        for donor in donors:
            # Check if the blood types match and if the organ needed matches the organ donated
            if (patient["blood_type"] == donor["blood_type"] and
                    patient["organ_needed"] == donor["organ_donated"]):

                # Additional rule-based filtering (optional, you can adjust these as needed)
                if not patient["conditions"] and not donor["conditions"]:  # No pre-existing conditions for both
                    if patient["infections"] != donor["infections"]:  # Ensure infections don't match
                        # Add to matches if conditions and infections allow
                        matches.append((patient["name"], donor["name"]))
    return matches


# Example Patient & Donor Data (adjusting for new fields from your form)
patients = [{
    "name": "Alice",
    "blood_type": "A+",
    "organ_needed": "Liver",
    "conditions": "",  # No pre-existing conditions
    "infections": "None"  # No infections
}]
donors = [{
    "name": "Bob",
    "blood_type": "A+",
    "organ_donated": "Liver",
    "conditions": "",  # No pre-existing conditions
    "infections": "None"  # No infections
}]

# Call the match function
matches = match_donor_patient(patients, donors)
print("Matches found:", matches)
