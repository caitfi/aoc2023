def findWinningNumbers(line):
    halves = line.strip().split("|")

    # first half: winning numbers
    winningNumberSet = {int(x) for x in halves[0].split(" ")[2:] if x.isdigit()}
    
    # second half: our numbers 
    ourNumberSet = {int(x) for x in halves[1].split(" ") if x.isdigit()}
    
    ourWinningNumbers = winningNumberSet & ourNumberSet
    return len(ourWinningNumbers)

f = open("input/4.txt", "r").readlines()

# part 1
cardValueSum = 0

for line in f:
    winningNumberCount = findWinningNumbers(line)

    # card value is 1, 2, 4, 8 ....
    cardValue = 0
    if (winningNumberCount > 0):
        cardValue = pow(2, winningNumberCount - 1)

    cardValueSum += cardValue

print(cardValueSum)

# part 2
cardInstances = [1 for x in range(len(f))]

for index, line in enumerate(f):
    winningNumberCount = findWinningNumbers(line)

    if (winningNumberCount > 0):
        for i in range(1, winningNumberCount+1):
            cardInstances[index + i] += cardInstances[index]


print(sum(cardInstances))