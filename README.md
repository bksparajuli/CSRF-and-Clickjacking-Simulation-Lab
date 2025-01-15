# Cybersecurity Simulation Project
Created for coursework of Security Auditing and Penetration testing (Masters at Islington College)
## **Overview**
This project simulates two critical cybersecurity attacks:
1. **Clickjacking + CSRF Attack**
2. **Reverse Shell Attack**

The project focuses on demonstrating application-level vulnerabilities and social engineering tactics, providing a framework for understanding security gaps and implementing mitigations.

## **Components**

### **1. app.py**
- **Purpose**:
  - The main Flask application handles the simulation's core functionality.
  - Provides endpoints for login, dashboards, profile management, and file uploads/downloads.
- **Features**:
  - Developer and CEO roles for simulating email communication.
  - A vulnerable endpoint for testing CSRF and Clickjacking attacks.

### **2. Templates**
- **login.html**:
  - Provides a login interface for developers and the CEO.
- **dashboard.html**:
  - Developer’s dashboard for sending emails and uploading files.
- **dashboard_ceo.html**:
  - CEO’s dashboard for viewing and downloading files.
- **profile.html**:
  - A profile management page with a vulnerable "Change Password" feature to simulate CSRF.

### **3. clickjack.html**
- **Purpose**:
  - Simulates a malicious webpage for demonstrating a Clickjacking attack.
- **Features**:
  - Embeds a hidden iframe to exploit the `Change Password` vulnerability in the application.
  - Contains a visible "Download" button to lure the user into clicking it.

## **Setup and Usage**

### **1. Prerequisites**
- Python 3.x
- Flask (`pip install flask`)

### **2. Running the Application**
1. Navigate to the project directory:
   ```bash
   cd project
Run the Flask application: <br>
bash <br>
python app.py<br>
Access the application in your browser:<br>
http://127.0.0.1:5000<br>
3. Simulating Clickjacking<br>
Host clickjack.html on a web server or access it locally.<br>
Navigate to the malicious webpage.<br>
Click the visible "Download" button to trigger the CSRF request.<br>
