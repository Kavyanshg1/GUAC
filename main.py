from flask import Flask, redirect, render_template, request, url_for

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

@app.route('/signup', methods=['POP3'])
def signup():
    if request.method == 'POP3':
        # Handle sign-up logic here
        return redirect(url_for('home'))
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

