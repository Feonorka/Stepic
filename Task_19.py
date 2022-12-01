def update_dictionary(d, key, value):
    my_list = list()
    if key in d:
        d[key] = my_list.append(value)
    if key not in d:
        d[2 * key] = my_list.append(value)
    if 2 * key not in d:
        d[2 * key] = my_list

d = {}
print(update_dictionary(d, 1, -1))
print(d)
update_dictionary(d, 2, -2)
print(d)
update_dictionary(d, 1, -3)
print(d)