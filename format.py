import re

name = input("What is your name? ").rstrip()

if matches := re.search(r"^(.+), *(.+)$",name):
    name = matches.group(2) + " " + matches.group(1)
print(f"Hello, {name}")