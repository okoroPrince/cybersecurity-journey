# Week 7: File I/O & Logging Scan Results

## What is File I/O?

File I/O (input/output) is reading from and writing to files using Python. Instead of just printing to screen, you save data permanently.

Basic syntax:
```python
with open(filename, 'w') as file:
    file.write("Text to write to the file")
```

## The `with open()` Pattern

Using `with` is best practice because it automatically closes the file after you're done. This prevents resource leaks (files staying open in memory).

Without `with`, you'd need to manually call `file.close()` — `with` handles it for you.

## Write ('w') vs Append ('a')

- **'w'** — Write mode. Overwrites everything in the file (clears it first)
- **'a'** — Append mode. Adds to the end of existing content
- **'r'** — Read mode. Opens file for reading only

## The Newline Character (\n)

`\n` creates line breaks. Without it, all your data runs together and becomes unreadable. Always end entries with `\n`:

```python
file.write(f"Port {port} is open\n")
```

## Scanner Enhancement

My port scanner now logs results to a file instead of just printing them. This means I can:
- Run scans unattended
- Analyse results later
- Build a database of findings
- Track changes over time

**Example:** Scanned 8.8.8.8 (ports 50-60), found port 53 (DNS) open, logged to `results.txt`.

## Why This Matters

Logging is critical in security. You need audit trails, records of what was found and when. A scanner that just prints to screen is useless for real work.