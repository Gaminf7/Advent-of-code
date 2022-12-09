import string

sack = r'day3.txt'
sack_list = []

with open(sack, 'r+') as sack:
    lines = sack.readlines()
    for i in range(0, len(lines)):
        sack_list.append(lines[i].strip('\n'))

total_sum = 0
values = dict()
for index, letter in enumerate(string.ascii_letters):
    values[letter] = index + 1

for items in sack_list:
    first, second = items[:len(items) // 2], items[len(items) // 2:]
    highest_point = 0
    for i in first:
        if i in second and values[i] > highest_point:
            highest_point = values[i]
    total_sum += highest_point
print(total_sum)



def split(list_a, chunk_size):
    for item in range(0, len(list_a), chunk_size):
        yield sack_list[item:item + chunk_size]

        
three_sacks = list(split(sack_list, 3))
total_three_sacks = 0
for sack in three_sacks:
    highest_point = 0
    for item in sack[0]:
        if item in sack[1] :
            if item in sack[2]:
                if values[item] > highest_point:
                    highest_point = values[item]
    total_three_sacks += highest_point
print(total_three_sacks)
