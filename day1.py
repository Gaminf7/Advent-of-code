sorted_elves = []
elves = r'C:\Users\Aisyah\Desktop\input.txt'
sum_calory = 0
elf_num = 0
elves_into_list = []
top_tree_calory = 0
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
        sorted_elves.append(sum_calory)
        sum_calory = 0

sorted_elves = sorted(sorted_elves, reverse=True)
for i in range (0,3):
    top_tree_calory += sorted_elves[i]
    
   
print(f"Highest Elf Calory: {sorted_elves[0]}")
print(f"Highest Top Three Calories: {top_tree_calory}")
