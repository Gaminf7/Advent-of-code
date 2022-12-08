sorted_elves = {}
elves = r'input.txt'
sum_calory = 0
elf_num = 0
elves_into_list = []
with open(elves, 'r+') as elf:
    lines = elf.readlines()
    for i in range(0, len(lines)):
        if lines[i] != '\n':
            elves_into_list.append(lines[i].strip('\n'))
        elif lines[i] == '\n':
            elves_into_list.append(' ')

for calory in elves_into_list:
    if not calory.isspace():
        calory = int(calory)
        sum_calory += calory
    else:
        elf_num += 1
        sorted_elves[str(elf_num)] = sum_calory
        sum_calory = 0

def find_most():
    elf_number = ''
    highest_value = 0
    for keys in sorted_elves:
        if sorted_elves[keys] > highest_value:
            highest_value = sorted_elves[keys]
            elf_number = keys
    return elf_number, highest_value


print(find_most())
