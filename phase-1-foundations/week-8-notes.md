# Week 8: CSV Vulnerability Scanner

## What is CSV?

CSV (Comma-Separated Values) is a simple text format for storing structured data. Each line is a row, columns are separated by commas. It's readable, lightweight, and easy to parse.

## Reading CSV Files in Python

Python has a built-in `csv` module for reading and writing CSV files.

Basic workflow:
```python
import csv

with open("vulnerabilities.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Each row is a list
```

The `with` statement safely opens and closes the file. `csv.reader()` parses the file. You loop through rows and access columns by index: `row[0]`, `row[1]`, etc.


## Vulnerability Scanner Logic

My scanner:
1. Takes user input (service name)
2. Opens vulnerabilities.csv
3. Loops through each row
4. Compares service name (case-insensitive) to the first column
5. Prints matching vulnerabilities in readable format
6. If no matches found, displays "not in database"

## Real-World Application

Vulnerability research is step one of exploitation. Security professionals search databases like CVE/NVD to find known flaws in running services. Understanding how to search and parse vulnerability data is essential to both attacking and defending systems.

## Next Steps

This scanner uses local CSV data. Next week (Week 9): upgrade it to query real vulnerability APIs using JSON parsing.