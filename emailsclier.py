import re

def solve(email):
   pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
   if re.match(pat,s):
    va =   email.split("@")
    username = va[0]
    domain = va[-1]
    return f"the username is {username} and domin is {domain}"
   return False

s = "popular_website15@comPany.com"
print(solve(s))