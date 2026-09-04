from flask import Flask, request,render_template
import sqlite3

app = Flask(__name__)
with sqlite3.connect("vulnerable.db") as db:
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS user(" \
    "username TEXT," \
    "password TEXT)")

    cursor.execute("DELETE FROM user")  # Clear old data
    cursor.execute("INSERT INTO user VALUES('admin', 'password123')")
    cursor.execute("INSERT INTO user VALUES('ebube', 'ebube1234')")
    db.commit()
                       
@app.route("/")
def home():
    return "===Welcome==="

@app.route('/login', methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        with sqlite3.connect("vulnerable.db") as db:
            cursor = db.cursor()
            query = (username, password)
            cursor.execute(f"SELECT * FROM user WHERE username = '{username}' AND password = '{password}'")
            exists = cursor.fetchall()

            if exists:
                return f"You loged in successfully Data = {exists}"
            else:
                return "Login failed"

    return render_template('login.html')
if __name__ == "__main__":
    app.run(debug=True)
