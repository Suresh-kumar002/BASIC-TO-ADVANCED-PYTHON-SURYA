import re

text = "The email address is suresh@123.com."

pattern = r"\w+@\w+\.\w+"

match = re.search(pattern, text)

if match:
    email = match.group()
    print(email)
