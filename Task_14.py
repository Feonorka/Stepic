with open('dataset_3363_2.txt') as file_in:
    for line in file_in:
        line = line.strip()

#line = 'S4B2h4v5n2o1P11S13'

my_list = list(line) # Конвертация строки в список
num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
my_dict = dict()
temp_list = []
i = 0
k= 0
end_str = ''
for item in range(len(my_list)):
    if my_list[i] in num_list:
        if my_list[i - 1] not in num_list: 
            k = 0
            while my_list[k + i] in num_list:
                temp_list.append(my_list[k + i])
                k += 1 # Наработка временного листа
                if k + i < len(my_list):
                    continue
                else:
                    break
            temp_str = "".join(temp_list)
            my_dict[my_list[i - 1]] = int(temp_str)
            end_str = end_str + my_list[i -1] * int(temp_str)
            i += 1
            temp_list.clear()
        else:
            i += 1
    else:
        i += 1
new_list = [key * val for key, val in my_dict.items()]
k = 0
for k in range(len(new_list)):
    print(new_list[k], end="")
print()
print(end_str)
with open("out.txt", 'w') as file_out:
    file_out.write(end_str)