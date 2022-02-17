
file_name = 'DATA/alt.txt'

a_words = []
b_words = []

with open(file_name) as file_in:
    for line in file_in:
        if line.startswith('a'):
            a_words.append(line)
        elif line.startswith('b'):
            b_words.append(line)

def save_file(file_name, word_list, sort_reverse):
    with open(file_name, 'w') as file_out:
        for line in sorted(word_list, reverse=sort_reverse):
            file_out.write(line.upper())

save_file('a_sorted.txt', a_words, False)
save_file('b_sorted.txt', b_words, True)


