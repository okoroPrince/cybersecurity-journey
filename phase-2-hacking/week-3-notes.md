# Week 3 notes
## What is UNION injection
UNION injection is a kind or sql injecttion  that uses thet union operation to append an extra sql query to the code base to perform malcious operations

## How does it work?
A UNION injection works by combining querie to achive a particular result

An example of this is:
`admin' UNION SELECT username, password FROM user --`

This is the original query:
``` sql
SELECT * FROM user WHERE username = 'admin' AND password = 'password123'
```
With UNION injection payload `admin' UNION SELECT username, password FROM user --`, it becomes:
``` sql
SELECT * FROM user WHERE username = 'admin' UNION SELECT username, password FROM user --' AND password = '...'
```
The UNION combines results from both queries. The `--` comments out the password check. Result: all usernames and passwords displayed.

In the real world this cn be really dangerous because it can be used to extract  whole database just from a login form to get the passwords and other confidential data form the database