#!/usr/bin/python3

spam = [
    "Spam",
    "eggs  ",
    "   spam    ",
    "     spam spam     ",
    "SPAM	",
    "       SPAM and eggs    ",
    "Spam",
    "   Spam,    spam, spam,    spam, spam, eggs, and spam      ",
]

def cleanup(s):
    pass

for s in spam:
    clean = cleanup(s)
    print(f"BEFORE: |{s}| AFTER: |{clean}|")
