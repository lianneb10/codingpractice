farts=["Lianne","Willy","Willy","Lianne","Lianne","Willy","Nyla","Willy","Willy"]

def uniqueNames():
    seen = []
    for nameInstance in farts: 
        if nameInstance not in seen:
            seen.append(nameInstance)
    return seen

def fartCounter(targetName):
    tally = 0
    for nameInstance in farts:
        if nameInstance == targetName:
            tally=tally+1
    return tally

for nameInstance in uniqueNames():
    print(nameInstance, fartCounter(nameInstance)) 
