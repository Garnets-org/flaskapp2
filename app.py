from flask import Flask, request, render_template, redirect

app = Flask(__name__)
users = []

@app.route('/')
def index():
    return render_template("index.html", users=users)

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    
    # Simple in-memory storage
    users.append({"username": username, "password": password})
    
    return redirect('/')

@app.route('/users', methods=['GET'])
def show_users():
    return {"users": [u['username'] for u in users]}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

