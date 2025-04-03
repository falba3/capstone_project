

def match_donor_patient(patients, donors):
    matches = []
    for patient in patients:
        for donor in donors:
            if patient["blood_type"] == donor["blood_type"] and patient["organ_needed"] == donor["organ_donated"]:
                matches.append((patient["name"], donor["name"]))
    return matches

# Example Patient & Donor Data
patients = [{"name": "Alice", "blood_type": "A+", "organ_needed": "Liver"}]
donors = [{"name": "Bob", "blood_type": "A+", "organ_donated": "Liver"}]

matches = match_donor_patient(patients, donors)
print("Matches found:", matches)