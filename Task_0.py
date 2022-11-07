GCstring = input()
modstr = GCstring.upper()
modstr2 = modstr.lower()
num = 0
for i in range(len(GCstring)):
    if modstr2[i] == "g" or modstr2[i] == "c":
        num+=1
    else:
        i+=1
print((num / len(GCstring)) * 100)

#acggtgttat