import re
url = input("URL: ").rstrip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)",url,re.IGNORECASE):

#username = re.sub(r"^(https?://)?(www\.|)?twitter\.com/", "", url)
#username = url.removeprefix("https://twitter.com/")
    print(f"Username: ", matches.group(1))