#s = 'aaaabbсaa' преобразуется в 'a4b2с1a2'

GCstring = input()
count = 0
for i in range(len(GCstring)):
    if i + 1 == len(GCstring):
        print(f'{GCstring[-1]}{count + 1}')
        break
    if GCstring[i] == GCstring[i+1]:
        count += 1  
    if GCstring[i] != GCstring[i+1]:
        print(f'{GCstring[i]}{count + 1}', end='')
        count = 0
    