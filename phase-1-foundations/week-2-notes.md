# Week 2: Linux Fundamentals

## Terminal & File System
Today I learned about the Linux terminal and how to navigate the file system using commands like `pwd`, `ls`, `cd`, and how files and directories work.

## Permissions (rwx)
Each file and directory has permissions in a specific format:
`[Type][Owner][Group][Other]`

The three permission types are:
- `r` (read) - can view file contents
- `w` (write) - can modify file
- `x` (execute) - can run file (or enter directory)

### Adding Permissions
To add permissions, use:
chmod (u,g,o)+(rwx) [filename]

### Removing Permissions
To remove permissions, use:
chmod (u,g,o)-(rwx) [filename]

- `u` = user (owner)
- `g` = group
- `o` = others

### Why Permissions Matter
Permissions control who has access to what files. This is crucial for security — you only give people the minimum access they need (principle of least privilege).

## Root User
Root is the superuser/admin account. It has all permissions on the system and can do anything. It's like "the god of the system" — it controls everything.