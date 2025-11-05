# gramy.py
import hashlib
import sys
from pathlib import Path

def read_hashes(hash_file_path):
    path = Path(hash_file_path)
    if not path.is_file():
        raise FileNotFoundError(f"Hash file not found: {hash_file_path}")
    with path.open("r", encoding="utf-8") as h_file:
        hashes = [line.strip() for line in h_file if line.strip()]
    return hashes

def read_passwords(wordlist_path):
    path = Path(wordlist_path)
    if not path.is_file():
        raise FileNotFoundError(f"Wordlist file not found: {wordlist_path}")
    with path.open("r", encoding="utf-8") as w_file:
        words = [line.rstrip("\n") for line in w_file if line.strip()]
    return words

def check_matches(words, hashes):
    """
    Check the candidate words against the list of MD5 hashes.
    Returns a list of (word, hashed_word) tuples for matches.
    """
    matches = []
    hash_set = set(hashes)  
    for word in words:
        hashed_word = hashlib.md5(word.encode("utf-8")).hexdigest()
        if hashed_word in hash_set:
            print(f"Match found: {word} --> {hashed_word}")
            matches.append((word, hashed_word))
    return matches

def crack_passwords(hash_file_path, wordlist_path):
    try:
        hashes = read_hashes(hash_file_path)
        words = read_passwords(wordlist_path)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return []
    matches = check_matches(words, hashes)
    if not matches:
        print("No matches found.")
    else:
        print(f"Total matches found: {len(matches)}")
    return matches

def main():
    hash_file = input("Path to hash file: ").strip()
    wordlist_file = input("Path to wordlist file: ").strip()

    print("\nAttempting to crack passwords, please be patient...\n")
    crack_passwords(hash_file, wordlist_file)
    print("\nFinished")

if __name__ == "__main__":
    main()
