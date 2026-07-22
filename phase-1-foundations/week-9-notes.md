# Week 9: APIs & JSON

## What is JSON?

JSON (JavaScript Object Notation) is a text format for transferring data over the web. It looks like a Python dictionary with key-value pairs. When you make an API request, servers send back JSON. In Python, you convert JSON to a readable dictionary using `.json()`:

```python
response = requests.get(url)
data = response.json()  # Convert JSON to Python dict
print(data["key"])
```

## How APIs Work

An API is a service that lets you request information from a server instead of building it yourself. The workflow is simple:

1. **Request** — You send an HTTP GET request to an endpoint (a URL like `https://official-joke-api.appspot.com/random_joke`)
2. **Response** — The server sends back JSON with the data you asked for

My joke fetcher does exactly this: requests a joke from the API, parses the JSON, extracts the setup and punchline, displays it.

## Why This Matters for Cybersecurity

APIs are critical in security work. Real vulnerability databases (like CVE databases) expose their data via APIs. In a real attack scenario:

1. Scan an IP for open ports and services
2. Use an API to query vulnerability databases
3. Find known CVEs for those services
4. Identify exploitable weaknesses

APIs are the bridge between reconnaissance and exploitation. Learning to work with them is learning to think like an attacker.