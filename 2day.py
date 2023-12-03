import re

f = open("input/2.txt", "r")

idealCubeVals = {"red" : 12, "green" : 13, "blue" : 14}
sumValidGames = 0
sumCubePower = 0


for index, line in enumerate(f):
    # Game X: X blue, X red; X red, X green, X blue; X green
    sections = line.strip().split(" ")

    # Game IDs are 1 - 100
    gameId = index + 1

    gameInvalid = False

    minCubeNums = {"red":0, "green":0, "blue":0}

    i = 2
    for i in range(0, len(sections), 2):
        if i == 0:
            continue

        # first is number
        numberOfCubes = int(sections[i])
        cubeInfo = sections[i+1]
        
        if (cubeInfo[-1] == "," or cubeInfo[-1] == ";"):
            cubeInfo = cubeInfo[:-1]

        # part 1
        if numberOfCubes > idealCubeVals[cubeInfo]:
            gameInvalid = True

        # part 2
        if numberOfCubes > minCubeNums[cubeInfo]:
            minCubeNums[cubeInfo] = numberOfCubes
    

    if (not gameInvalid):
        sumValidGames += gameId
    
    # get cube power
    gamePower = minCubeNums["red"] * minCubeNums["green"] * minCubeNums["blue"]
    sumCubePower += gamePower


print(sumValidGames)
print(sumCubePower)

        
