with open("dataset_3363_3.txt","r") as in_file:
    for line in in_file:
        print(type(line))
        line.strip()
        print(line)
line = 'S4B 2h4 v5n 2o 1P 11S1 3 d d d d sss ss da as dsd awd sdasd Mama Mama Mama Mama Mama Mama Mama Mama Mama Mama adwdasd q q q q q q q q q q ww ww ww dw a s a a a a a a a a a S4 BSS4B B S4B S4B v S4B S4B S4B'
my_list = list(line.split(sep=None, maxsplit= -1))
my_list.sort()
my_dict = dict()
max_value = 0
max_pos = 0

for item in my_list:
    ipos = my_list.index(item)
    my_dict[ipos] = my_list.count(item)
    if my_dict.get(ipos) > max_value:
        max_value = my_dict.get(ipos)
        max_pos = ipos

print(f'Слово {my_list[max_pos]} встречается {max_value}')

