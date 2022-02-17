import re

s1 = "Please pat the dog"
s2 = "A lovely postern"

for s in s1, s2:
    if re.search('p.t', s):
        print(s, "matches")
    else:
        print(s, "does not match")
