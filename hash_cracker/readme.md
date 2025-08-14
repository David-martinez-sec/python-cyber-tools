# 🔐 Hash Cracker (MD5 Dictionary Attack)

This is a simple Python-based hash cracker that uses a dictionary attack to reverse MD5 hashes. Built as part of my cybersecurity learning journey, the project helped reinforce key Python skills while introducing core security concepts like hashing, password cracking, and file handling.

---

## 🚀 What It Does

- Prompts the user to input an MD5 hash
- Reads a local wordlist file (`wordlist.txt`)
- Hashes each word in the list using `hashlib.md5()`
- Compares each hash to the input
- If a match is found, prints the matching password

---

## 🧠 Concepts and Skills Covered

### 🔸 Python Language Skills
- `input()` for user interaction
- `with open(...)` for safe file reading
- String methods like `.strip()`
- Conditional logic and loop control
- Error handling (syntax debugging)

### 🔸 Hashing with `hashlib`
- Learned that **hash functions** convert data into fixed-length digests
- Used `hashlib.md5()` to hash a password word
- Applied `.encode()` to convert strings into bytes before hashing
- Used `.hexdigest()` to convert the hashed byte result into a readable string

### 🔸 Dictionary Attacks
- Simulated a real-world cracking scenario using a list of common passwords
- Understood that hashes are **one-way** — they can't be decrypted, only brute-forced or matched via lookup
- Highlighted the importance of password complexity and proper storage

### 🔸 Terminal-Based Workflow
- Used `nano` to write and update the script
- Ran and debugged the script entirely from the terminal
- Understood and resolved real Python errors (e.g., `EOL while scanning string literal`, typos in variable names)
- Created a custom `wordlist.txt` for testing

### 🔸 Git & GitHub Skills
- Used `git init`, `add`, `commit`, and `push`
- Handled GitHub's switch from password auth to **personal access tokens (PATs)**
- Set up **SSH authentication** with a new `ed25519` key
- Understood the purpose of SSH fingerprints and GitHub trust prompts
- Learned how to store SSH public keys in GitHub for seamless secure access

---

## 🗂 Example Directory Structure

