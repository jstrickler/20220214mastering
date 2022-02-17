import re

def doit(match):
    return "**" + match.group(0) + "**"

with open('DATA/parrot.txt') as parrot_in:
    with open('bigwords.txt', 'w') as big_out:
        for line in parrot_in:
            new_line = re.sub("[a-z]{8,}", doit, line)
            big_out.write(new_line)
