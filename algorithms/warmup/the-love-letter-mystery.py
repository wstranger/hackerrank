def calc_polindrom_complexity(letter):
    preff = letter[0:len(letter)/2]
    aff = letter[-1 * (len(letter) / 2):]

    combination_count = 0
    for i in range(len(preff)):
        combination_count += abs(ord(aff[i]) - ord(preff[-1 * (i + 1)]))

    return combination_count

num_testcases = input()
letters = []
for i in range(num_testcases):
    letters.append(raw_input())

for letter in letters:
    print calc_polindrom_complexity(letter)
