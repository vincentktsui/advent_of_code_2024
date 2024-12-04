from collections import defaultdict

file = open("day1.txt", "r")
lines = file.readlines()


first_list = []
second_list = []
for line in lines:
    cleaned = line.strip()
    first, second = cleaned.split()
    first_list.append(first)
    second_list.append(second)




def part1():
    sorted_first = sorted(first_list)
    sorted_second = sorted(second_list)


    zipped = zip(sorted_first, sorted_second)


    difference = 0
    for a, b in zipped:
        difference += abs(int(a) - int(b))

    return difference

print(part1())

def part2():
    counts = defaultdict(int)
    for i in second_list:
        counts[i] += 1

    score = 0
    for i in first_list:
        score += int(i) * counts[i]
    return score
print(part2())