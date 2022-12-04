# read input.txt file
with open('input.txt', 'r') as file:
    data = file.read().splitlines()

score = 0
# a x
# a y
# a z
# b x
# b y
# b z
# c x
# c y
# c z


# loop through each line
# part 1
for line in data:
    if line == 'A X':
        score += 4
    elif line == 'A Y':
        score += 8
    elif line == 'A Z':
        score += 3
    elif line == 'B X':
        score += 1
    elif line == 'B Y':
        score += 5
    elif line == 'B Z':
        score += 9
    elif line == 'C X':
        score += 7
    elif line == 'C Y':
        score += 2
    elif line == 'C Z':
        score += 6

score = 0

# part 2
for line in data:
    if line == 'A X':
        score += 3
    elif line == 'A Y':
        score += 4
    elif line == 'A Z':
        score += 8
    elif line == 'B X':
        score += 1
    elif line == 'B Y':
        score += 5
    elif line == 'B Z':
        score += 9
    elif line == 'C X':
        score += 2
    elif line == 'C Y':
        score += 6
    elif line == 'C Z':
        score += 7


print(score)
