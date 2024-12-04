import re

file = open("day3.txt", "r")
lines = file.readlines()

regex = 'mul\((\d+,\d+)\)'
regex2 = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"

def part1():
    sum = 0
    for line in lines:
        found = re.findall(regex, line.strip())
        for multiply in found:
            num1, num2 = multiply.split(",")
            sum += int(num1) * int(num2)
    return sum

print(part1())


def part2():
    enabled = True
    sum = 0
    for line in lines:
        tokens = re.findall(regex2, line.strip())
        for token in tokens:
            if token == "do()":
                enabled = True
            elif token == "don't()":
                enabled = False
            elif token.startswith("mul"):
                if not enabled: 
                    continue
                found = re.findall(regex, token)
                for multiply in found:
                    num1, num2 = multiply.split(",")
                    sum += int(num1) * int(num2)
    return sum
print(part2())