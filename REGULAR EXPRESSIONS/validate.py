import re

email = input("Whats your email? ").strip()

if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
    print("Valid email")
    print(email)
else:  
    print("Invalid email")