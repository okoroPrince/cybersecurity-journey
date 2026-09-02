# week 2
## What is SQL injection
SQL injection is when a mallicious query is inserted into the field of a form that will affect the functionallity if the backend and change what the SQL query in the back is meant to do

## How the exploit works:
Your vulnerable query:

``` python
python

cursor.execute(f"SELECT * FROM user WHERE user_name = '{username}' AND password = '{password}'")
```

When you type `admin' or '1'='1' --` in username field, it becomes:

```sql
sql

SELECT * FROM user WHERE user_name = 'admin' or '1'='1' -- AND password = 'whatever'
```

The or `'1'='1'` makes the condition always true. The `--` comments out the password check.

Result: Authentication bypassed.

I intentionally made a Flask app that has an exploitable backend and i uses the `1'='1' --` command in the frontend to makke sure the condition for login is always true enabling an unautorised login.

I tested two payloads to trigget the access they are:
- `1'='1'--` in the user field
- `admin' or '1'='1`
- `'='1'` in the user and password field

They both worked because they amde the WHERE condition in the SQL query always true

In the reworld attacters can use this to gain unauthorised access to applications that are meant to be protected by a password.