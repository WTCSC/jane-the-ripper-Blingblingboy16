# test_gramy.py
import hashlib
from pathlib import Path
from gramy import read_hashes, read_passwords, check_matches, crack_passwords

def test_read_hashes(tmp_path):
    hash_file = tmp_path / "hashes.txt"
    # write two example hash strings (not actual md5s, just test content)
    hash_file.write_text("abc123\nxyz789\n")
    result = read_hashes(hash_file)
    assert result == ["abc123", "xyz789"]

def test_read_passwords(tmp_path):
    wordlist = tmp_path / "words.txt"
    wordlist.write_text("apple\nbanana\n")
    result = read_passwords(wordlist)
    assert result == ["apple", "banana"]

def test_check_matches(capsys):
    words = ["hello", "password123"]
    # produce the md5 hash for the known matching word
    target_hash = hashlib.md5("password123".encode("utf-8")).hexdigest()
    hashes = [target_hash]
    matches = check_matches(words, hashes)

    # check the returned matches list
    assert matches == [("password123", target_hash)]

    # also verify the function printed the match to stdout
    captured = capsys.readouterr()
    assert "Match found: password123" in captured.out

def test_crack_passwords(tmp_path, capsys):
    # create wordlist file
    wordlist_file = tmp_path / "wordlist.txt"
    wordlist_file.write_text("test\n1234\npassword\n")

    # create hash file containing md5("password")
    hash_file = tmp_path / "hashes.txt"
    pw_hash = hashlib.md5("password".encode("utf-8")).hexdigest()
    hash_file.write_text(pw_hash + "\n")

    # call the function (it accepts Path objects)
    matches = crack_passwords(hash_file, wordlist_file)

    # verify returned matches and printed output
    assert matches == [("password", pw_hash)]
    captured = capsys.readouterr()
    assert "Match found: password" in captured.out
