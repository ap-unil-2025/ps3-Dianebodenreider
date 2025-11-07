import string
from collections import Counter


def create_sample_file(filename="sample.txt"):
    """
    Create a sample text file for testing.
    """
    content = """Python is a powerful programming language.
It is widely used in web development, data science, and automation.
Python's simple syntax makes it great for beginners.
Many companies use Python for their projects."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created {filename!r}")


def _read_text(filename):
    """Read file content as a single string (utf-8)."""
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def _tokenize_words(text):
    """
    Convert text to a list of 'words':
    - lowercase
    - remove punctuation
    - split on whitespace
    """
    # Remplacer la ponctuation par des espaces pour garder les mots collés propres
    trans = str.maketrans({ch: " " for ch in string.punctuation})
    clean = text.lower().translate(trans)
    return clean.split()


def count_words(filename):
    """
    Count total words in the file.
    """
    text = _read_text(filename)
    words = _tokenize_words(text)
    return len(words)


def count_lines(filename):
    """
    Count total lines in the file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)


def count_characters(filename, include_spaces=True):
    """
    Count characters in the file.
    If include_spaces is False, ignore whitespace (spaces, tabs, newlines).
    """
    text = _read_text(filename)
    if include_spaces:
        re
