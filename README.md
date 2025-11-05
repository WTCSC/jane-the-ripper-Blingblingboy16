[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/d_w3ds2H)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=21388702)
# Password Cracker
## Savannah Finn

This project is a simple MD5 hash password cracker written in Python.  
It takes two input files:

1. A file containing **MD5 password hashes** (one per line).
2. A **wordlist** containing plaintext password guesses (one per line).

The program hashes each word in the wordlist and checks if it matches any hash in the hash file. If a match is found, it prints and records the cracked password.

This type of password cracking is known as a **dictionary attack**, and is commonly used to demonstrate the weakness of unsalted hashing.
## How to Run the Program

Make sure you have **Python 3** installed.

Run the program using:

```bash
python gramy.py
