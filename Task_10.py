spisok = [str(i) for i in input().split(" ")]
spisok.sort()
dictionary = {}
for i in range(len(spisok)):
    spisok[i] = spisok[i].lower()
    dictionary[spisok[i]] = spisok.count(spisok[i])
for key, value in dictionary.items():
    print(key, value)