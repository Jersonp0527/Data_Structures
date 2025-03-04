diccCant = {}
diccSet = {}

while(1):
    line = input()
    
    if(line == '#'):
        break
    
    eq, ag, pr = line.split()
    
    diccCant[eq] = diccCant.get(eq, 0) + 1
    diccSet[eq] = diccSet.get(eq, set())
    diccSet[eq].add(pr)
    
for eq, pres in diccSet.items():
    if(len(pres)>=3):
        print(eq, diccCant[eq])