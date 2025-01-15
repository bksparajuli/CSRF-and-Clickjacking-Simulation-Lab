from flask import Flask, request, render_template, redirect, url_for, session, send_from_directory
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Dummy user data
users = {
    "developer": {"password": "password123", "role": "Developer"},
    "ceo": {"password": "ceopassword", "role": "CEO"}
}

# In-memory message storage
messages = []

# File upload directory
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username in users and users[username]['password'] == password:
            session['username'] = username
            session['role'] = users[username]['role']
            return redirect(url_for('dashboard'))
        else:
            return "Invalid credentials! Try again."
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'username' not in session:
        return redirect(url_for('home'))

    # Developer's dashboard
    if session['role'] == "Developer":
        if request.method == 'POST':
            recipient = request.form.get('recipient')
            subject = request.form.get('subject')
            content = request.form.get('content')
            uploaded_file = request.files.get('file')

            if uploaded_file:
                # Save the file to the uploads directory
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
                uploaded_file.save(file_path)
                content += f'\n[File Attached: <a href="/download/{uploaded_file.filename}">{uploaded_file.filename}</a>]'

            # Add the message to in-memory storage
            messages.append({
                "from": session['username'],
                "to": recipient,
                "subject": subject,
                "content": content
            })
            return "Mail sent successfully!"
        return render_template('dashboard.html', username=session['username'])

    # CEO's dashboard
    elif session['role'] == "CEO":
        # Filter messages for the CEO
        inbox = [msg for msg in messages if msg['to'] == session['username']]
        return render_template('dashboard_ceo.html', username=session['username'], inbox=inbox)

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'username' not in session:
        return redirect(url_for('home'))

    if request.method == 'POST':
        new_password = request.form.get('new_password')
        if session['username'] in users:
            users[session['username']]['password'] = new_password
            return "Password updated successfully!"

    new_password = request.args.get('new_password')
    if new_password and session['username'] in users:
        users[session['username']]['password'] = new_password
        return "Password updated via GET request (CSRF vulnerability)!"

    return render_template('profile.html', username=session['username'])

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('role', None)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
