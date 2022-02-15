
with open('DATA/alice.txt') as alice_in:
    count = 0
    for raw_line in alice_in:
        if 'Alice' in raw_line:
            print(raw_line.rstrip())
            count += 1
print()
print(f"'Alice' occured on {count} lines")

