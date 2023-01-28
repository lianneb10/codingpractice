nylafood = ["can", "fresh", "kibble", "can", "fresh", "can", "kibble", "kibble", "kibble", "kibble"]

# avgFood = sum(nylafood)/len(nylafood)
# print(avgFood)

def uniqueNum():
    seen = []
    for number in nylafood: 
        if number not in seen:
            seen.append(number)
    return seen

def foodCount(targetNum):
    tally = 0
    for number in nylafood:
        if number == targetNum:
            tally=tally+1
    return tally

def modeFood():
    maxFood = 0
    bestCount = 0
    for number in uniqueNum():
        currentCount = foodCount(number)
        print (number, currentCount)
        if currentCount > bestCount:
            bestCount = currentCount
            maxFood = number
            print(bestCount, maxFood)
    return maxFood
    

print(modeFood())