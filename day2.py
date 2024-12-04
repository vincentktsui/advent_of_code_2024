from grid import Grid

file = open("day2.txt", "r")
lines = file.readlines()


grid = Grid([line.strip().split() for line in lines])

def process_row(row):
    direction = None
    for i in range(len(row) - 1):
        current = int(row[i])
        following = int(row[i + 1])
        if following - current == 0:
            return False
        if abs(following - current) > 3:
            return False
        if direction is None:
            if following - current > 0:
                direction = "increasing"
            else:
                direction = "decreasing"
        if direction == "increasing" and following - current < 0:
            return False
        if direction == "decreasing" and following - current > 0:
            return False
    return True


def row_mistake(row):
    direction = None
    for i in range(len(row) - 1):
        current = int(row[i])
        following = int(row[i + 1])
        if following - current == 0:
            return i + 1
        if abs(following - current) > 3:
            return i + 1
        if direction is None:
            if following - current > 0:
                direction = "increasing"
            else:
                direction = "decreasing"
        if direction == "increasing" and following - current < 0:
            return i + 1
        if direction == "decreasing" and following - current > 0:
            return i + 1
    return None


def part1():
    count = 0
    for row in grid.get_rows():
        if process_row(row):
            count += 1
    return count            


print(part1())

def part2():
    count = 0
    for row in grid.get_rows():
        i = row_mistake(row)
        if i is None:
            count += 1
            continue
        else:
            # if problem is the increasing/decreasing direction of the first element, flipping the list will identify
            flipped = row[::-1]
            j = row_mistake(row[::-1])
            if process_row(row[:i] + row[i+1:]) or process_row(flipped[:j] + flipped[j+1:]):
                count += 1
    return count
        

print(part2())