elves = r'day2.txt'

sorted_elves = []

with open(elves, 'r+') as elf:
    lines = elf.readlines()
    for i in range(0, len(lines)):
        sorted_elves.append((lines[i].strip(' ').split()))

sum_of_points = 0

# part 1
for row in sorted_elves:
    if row[0] == 'A':  # Rock
        if row[1] == 'X':  # Rock
            sum_of_points += (1 + 3)
        elif row[1] == 'Y':  # Paper
            sum_of_points += (2 + 6)
        elif row[1] == 'Z':  # Scissors
            sum_of_points += (3 + 0)
    elif row[0] == 'B':  # Paper
        if row[1] == 'X':  # Rock
            sum_of_points += (1 + 0)
        elif row[1] == 'Y':  # Paper
            sum_of_points += (2 + 3)
        elif row[1] == 'Z':  # Scissors
            sum_of_points += (3 + 6)
    elif row[0] == 'C':  # Scissors
        if row[1] == 'X':  # Rock
            sum_of_points += (1 + 6)
        elif row[1] == 'Y':  # Paper
            sum_of_points += (2 + 0)
        elif row[1] == 'Z':  # Scissors
            sum_of_points += (3 + 3)

print(f'Sum Of Total Points If Everything Goes According to plan: {sum_of_points}')

s2_points = 0
for row in sorted_elves:
    if row[0] == 'A':  # Rock
        if row[1] == 'X':  # Lose
            s2_points += (3 + 0)
        elif row[1] == 'Y':  # Draw
            s2_points += (1 + 3)
        elif row[1] == 'Z':  # Win
            s2_points += (2 + 6)
    elif row[0] == 'B':  # Paper
        if row[1] == 'X':  # Lose
            s2_points += (1 + 0)
        elif row[1] == 'Y':  # Draw
            s2_points += (2 + 3)
        elif row[1] == 'Z':  # Win
            s2_points += (3 + 6)
    elif row[0] == 'C':  # Scissors
        if row[1] == 'X':  # Lose
            s2_points += (2 + 0)
        elif row[1] == 'Y':  # Draw
            s2_points += (3 + 3)
        elif row[1] == 'Z':  # Win
            s2_points += (1 + 6)


print(f'Super Secret ELf Strategy: {s2_points}')
