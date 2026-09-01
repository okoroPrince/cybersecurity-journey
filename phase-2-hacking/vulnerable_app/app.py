from flask import Flask, request,render_template
import sqlite3

app = Flask(__name__)
with sqlite3.connect("vulnerable.db") as db:
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS user(" \
    "user_name TEXT," \
    "password TEXT)")

    cursor.execute("INSERT OR IGNORE INTO user('user_name', 'password') VALUES('Ebube', 'ebube1234')")
    db.commit()
                       
@app.route("/")
def home():
    return "===Welcome==="

@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        with sqlite3.connect("vulnerable.db") as db:
            cursor = db.cursor()
            query = (username, password)
            cursor.execute(f"SELECT * FROM user WHERE user_name = '{username}' AND password = '{password}'")
            exists = cursor.fetchall()

            if exists:
                return "You loged in successfully"
            else:
                return "Login failed"

    return render_template('login.html')
if __name__ == "__main__":
    app.run(debug=True)
