with open("test.text", 'r') as in_file:
    my_dict = {}
    temp_value_lst = []
    final_dict = {}
    for line in in_file.readlines():
        line = line.split(';')
        key = line[0].strip()
        for i in range(1,len(line)):
            value = line[i].strip()
            if key in my_dict:
                my_dict[key].append(value)
            else:
                my_dict[key] = [value]

# temp_value_lst = my_dict.get('sdfsdfefsdf')
# print(my_dict)
# print(temp_value_lst[0])

def avr_point(lst): # Среднее значение элементов в списке
    sum = 0
    for i in range(len(lst)):
        sum = sum + int(lst[i])
    avr = sum // len(lst)
    return avr

def avr_les(item_dict): # Среднее значение элементов по предметам
    sum_of = 0
    for key in item_dict:
        temp = item_dict.get(key)
        for i in range(len(temp)):
            sum_of = sum_of + int(temp[i])
    return sum_of

for key in my_dict:
    temp_value_lst = my_dict.get(key)
    final_dict[key] = avr_point(temp_value_lst)
print(f'Словарь со средними оценками каждого ученика:\n\t{final_dict}')

print(f'Результат avr_les:\n\t{avr_les(my_dict)}')