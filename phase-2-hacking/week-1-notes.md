# phase 2 week 1
Today i learnt flask 
Flask is a module in python that enables python to be able to host a website and send post and get requests to that site

## GET vs POST 
GET request is saying bring the data from the form on the server while POST is saying push this data to the server

## Creating a from in HTML
To create a form in html use this 
```HTML
<!DOCTYPE HTML>
<head>
    <title>Document</title>
</head>
<body>
    <form method = "post" action = "/login">
        <label>Name</label>
        <input type = "text" placeholder = "Name" name = "username" required>
        <br><br>
        <label>Password</label>
        <input type = "password" required placeholder = "Password" name = "password">
        <br><br>
        <input type = "submit">
    </form>
</body>
```

## what is SQLite
SQLite is a built in module in python that is used to create database and control it in python by adding updatin deleting etc the values in the table from python

## Difference between parameterized and vulnerable queries
Parameterized quries are queries done where the value it passes into a variable before passing it into the query of it also uses `?` as placeholders while vulnerable queries are queries where the values are passed directly into the query which is not good because it is subjectable to sql injection e.g:

**Parameterised query**
```python
import sqlite3
with sqlite3.connect("vulnerable.db") as db:
    cursor = db.cursor()
    query = (name,password)
    cursor.execute("SELECT * FROM user WHERE username = ? AND password = ?", query)
    cursor.fetchall()
```
**Vulnerable query**
```python
import sqlite3
with sqlite3.connect("vulnerable.db") as db:
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM user WHERE username = '{name}' AND password = '{password}'")
    cursor.fetchall()
```

## What i built in week one
I built a vulnerable login form with `FLASK` and `SQLite` for pentesting in week 2

This is my code:
```python
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

```