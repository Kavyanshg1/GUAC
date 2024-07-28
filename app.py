'''
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic here
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Handle sign-up logic here
        return redirect(url_for('home'))
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
'''

from flask import Flask, render_template, request, redirect, url_for, session
import poplib 

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong, unique key

# Simple in-memory database for users
users = {
    'admin': 'password',  # Example user
    'user1': 'test1234'  # Another example user
}

@app.route('/')
def home():
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    return render_template('login.html')
@app.route('/fetch_emails', methods=['POST'])
def fetch_emails():
    # Retrieve email server details (from a config file or environment variables)
    pop3_server = ...
    pop3_port = ...
    email_address = ...
    email_password = ...

    try:
        pop_conn = poplib.POP3_SSL(pop3_server, pop3_port)
        pop_conn.user(email_address)
        pop_conn.pass_(email_password)

        # ... (Your POP3 email retrieval and processing logic) ...

        pop_conn.quit()

        # Return a response (e.g., a success message, email data, etc.)
        return "Emails fetched successfully!" 
    except Exception as e:
        # Handle errors gracefully
        return f"Error fetching emails: {e}"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            error = 'Invalid credentials'
            return render_template('login.html', error=error)
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)