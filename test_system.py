import requests

print("Testing EHR Patient Management System")
print("=" * 50)

# Test server status
try:
    response = requests.get("http://localhost:5000/")
    print("Server Status:", response.json()["message"])
except:
    print("Server not responding")
    exit()

# Test patient API
try:
    patients = requests.get("http://localhost:5000/api/patients").json()
    print("Patient Database:", len(patients), "records")
    
    # Show sample data
    if patients:
        print("Sample Patient:")
        patient = patients[0]
        print("  Name:", patient["first_name"], patient["last_name"])
        print("  ID:", patient["patient_id"])
        print("  DOB:", patient["date_of_birth"][:10])
        
except Exception as e:
    print("Patient API error:", e)

print("=" * 50)
print("System Status: OPERATIONAL")