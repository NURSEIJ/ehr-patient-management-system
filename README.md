# EHR Patient Data Management System 
 
## Capstone Project - Healthcare Informatics 
 
A comprehensive Electronic Health Record (EHR) system designed to streamline patient data management and improve care coordination in healthcare facilities. 
 
## Features 
 
- **Electronic Health Records (EHR)** - Digital patient data management 
- **MySQL Database** - Secure patient data storage 
- **RESTful API** - Python Flask backend 
- **Patient Management** - Create and retrieve patient records 
- **Healthcare Data Standards** - Structured medical information 
 
## Technology Stack 
 
- **Backend**: Python Flask 
- **Database**: MySQL 
- **API**: RESTful JSON APIs 
 
## Installation 
 
### Prerequisites 
- Python 3.8+ 
- MySQL Server 8.0+ 
 
### Setup 
 
1. **Clone the repository** 
\`\`\`bash 
git clone https://github.com/NURSEIJ/ehr-patient-management-system.git 
cd ehr-patient-management-system 
\`\`\` 
 
2. **Install dependencies** 
\`\`\`bash 
pip install -r requirements.txt 
\`\`\` 
 
3. **Configure MySQL database** 
   - Update database credentials in \`app.py\` 
 
4. **Run the application** 
\`\`\`bash 
python app.py 
\`\`\` 
 
## Testing Instructions 
 
### Quick Verification 
 
After starting the server, run this command to verify the system: 
 
\`\`\`bash 
python -c "import requests; print('Server:', requests.get('http://localhost:5000/').json()['message']); p=requests.get('http://localhost:5000/api/patients').json(); print('Patients in database:', len(p))" 
\`\`\` 
 
### Browser Testing 
 
1. **Server Status**: http://localhost:5000/ 
2. **Patient API**: http://localhost:5000/api/patients 
 
### Automated Testing 
 
Create \`test_system.py\`: 
 
\`\`\`python 
import requests 
 
def test_ehr_system(): 
    print('Testing EHR System') 
    print('=' * 40) 
 
    # Test server status 
    response = requests.get('http://localhost:5000/') 
    print('Server Status:', response.json()['message']) 
 
    # Test patient API 
    patients = requests.get('http://localhost:5000/api/patients').json() 
    print(f'Patient Database: {len(patients)} records') 
 
    if patients: 
        print('Sample Patient:') 
        patient = patients[0] 
        print(f'  Name: {patient[\"first_name\"]} {patient[\"last_name\"]}') 
        print(f'  ID: {patient[\"patient_id\"]}') 
 
    print('=' * 40) 
    print('System Status: OPERATIONAL') 
 
test_ehr_system() 
\`\`\` 
 
Run with: \`python test_system.py\` 
 
## API Endpoints 
 
 
### Example Response 
 
\`\`\`json 
[ 
  { 
    \"patient_id\": 1, 
    \"first_name\": \"John\", 
    \"last_name\": \"Doe\", 
    \"date_of_birth\": \"1985-07-15\", 
    \"gender\": \"Male\", 
    \"blood_type\": \"O+\" 
  } 
] 
\`\`\` 
 
## Database 
 
MySQL database with patient management tables including: 
- \`patients\` - Patient demographics 
- \`medical_records\` - Health history 
- \`appointments\` - Scheduling 
- \`prescriptions\` - Medications 
 
## Project Structure 
 
\`\`\` 
ehr-patient-management-system/ 
ÃÄÄ app.py                 # Main Flask application 
ÃÄÄ requirements.txt       # Python dependencies 
ÃÄÄ README.md             # Project documentation 
ÀÄÄ test_system.py        # Testing script 
\`\`\` 
 
## Support 
 
For issues or questions, create an issue in the GitHub repository. 
 
## License 
 
Educational project for capstone requirements. 
