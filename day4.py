pair = r'day4.txt'
pair_into_list = []
with open(pair, 'r+') as pair:
    lines = pair.readlines()
    for item in range(0, len(lines)):
        pair_into_list.append(lines[item].strip('\n').split(','))

contained_set = 0
overlap = 0

for i in pair_into_list:
    first, second = i[0].split('-'), i[1].split('-')
    if int(second[0]) >= int(first[0]):
        if int(second[1]) <= int(first[1]):
            contained_set += 1
        elif int(first[0]) >= int(second[0]):
            if int(first[1]) <= int(second[1]):
                contained_set += 1
    elif int(first[0]) >= int(second[0]):
        if int(first[1]) <= int(second[1]):
            contained_set += 1
        elif int(second[0]) >= int(first[0]):
            if int(second[1]) <= int(first[1]):
                contained_set += 1


for i in pair_into_list:
    first, second = i[0].split('-'), i[1].split('-')
    if int(second[0]) <= int(first[1]) and (int(second[1]) >= int(first[0]) <= int(first[1]) ):
        overlap +=1
    elif int(first[0]) <= int(second[1]):
        if int(first[1]) >= int(second[0]):
            overlap += 1


print(contained_set)
print(overlap)
