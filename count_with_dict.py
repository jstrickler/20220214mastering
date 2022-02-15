

counts = {}

with open('DATA/words.txt') as words_in:
    for word in words_in:
        first_letter = word[0]
        if first_letter in counts:
            counts[first_letter] = counts[first_letter] + 1
        else:
            counts[first_letter] = 1

print(counts)
