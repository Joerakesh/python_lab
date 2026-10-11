# String Manipulation
# Course: Python for Data Science | Loyola College, Chennai
# Student: Joe Rakesh A | Department No.: 26-PDS-002

# Exercise 03 — String Manipulation
import re
from collections import Counter

def is_palindrome(text):
    cleaned = re.sub(r"[^a-z0-9]", "", text.lower())
    return cleaned == cleaned[::-1]

def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])

def count_vowels(text):
    return sum(1 for ch in text.lower() if ch in "aeiou")

corpus = [
    "Data science combines statistics and programming.",
    "Machine learning is a subset of data science.",
    "Programming skills are essential for data science and machine learning.",
]
STOPWORDS = {"a", "is", "of", "and", "the", "are", "for", "in", "to"}

def tokenize(text):
    tokens = re.findall(r"[a-z]+", text.lower())
    return [token for token in tokens if token not in STOPWORDS]

all_tokens = []
for sentence in corpus:
    all_tokens.extend(tokenize(sentence))
bow = Counter(all_tokens)

print("Palindrome check for 'Never odd or even':", is_palindrome("Never odd or even"))
print("Reverse words:", reverse_words("Data science is useful"))
print("Vowel count in 'Python':", count_vowels("Python"))
print("\nCorpus:")
for sentence in corpus:
    print(" -", sentence)
print("\nBag-of-Words (word frequency):")
for word, frequency in bow.most_common():
    print(f" {word:12s}: {frequency}")
print("Vocabulary size:", len(bow))
print("Total tokens (after stopword removal):", sum(bow.values()))
