def neighbours(grid, pos):
    x0, y0 = pos
    candidates = [(x0 - 1, y0), (x0 + 1, y0), (x0, y0 - 1), (x0, y0 + 1), (x0 - 1, y0 - 1), (x0 - 1, y0 + 1), (x0 + 1, y0 - 1), (x0 + 1, y0 + 1)]
    return [p for p in candidates if p in grid]

f = open("input/3.txt", "r")
specialChars = "!\"#$%&'()*+,-/:;<=>?@[\]^_`{|}~" # removed .

lines = f.readlines()
numRows = len(lines)
numCols = len(lines[0])

# dictionary of points
grid = {(x, y): val for x, line in enumerate(lines) for y, val in enumerate(line.strip())}

i = 0
j = 0
sum = 0

numberPositions = []
gearPositions = []

# parsing the grid in a terrible, terrible while loop
while i < numRows:
    while j < numCols:
        key = (i, j)
        currentNumber = []
        currentNumberCoords = []

        numberIsPart = False

        if key in grid and grid[key].isdigit():

            iterKey = (i, j)
            # check all digits' neighbours of this number
            while (grid[iterKey].isdigit()):
                currentNumber.append(grid[iterKey])
                currentNumberCoords.append(iterKey)

                # check if symbol is in neighbours
                neighboursPos = neighbours(grid, iterKey)

                for pos in neighboursPos:
                    if grid[pos] in specialChars:
                        # this is a part number
                        numberIsPart = True
                
                j += 1
                iterKey = (i, j)
                
                if j == numCols-1:
                    break
            
            wholeNumber = int(''.join(currentNumber))

            if (numberIsPart):
                sum += wholeNumber

            # save number and its coordinates
            numberPos = [wholeNumber, currentNumberCoords]
            numberPositions.append(numberPos)

        # save gear positions
        elif key in grid and grid[key] == "*":
            gearPositions.append(key)
            j += 1

        # reached the end of the row
        elif j == numCols-1:
            break

        else:
            j += 1

    j = 0
    i += 1

# part 1
print(sum)

gearRatioSum = 0

# part 2
for gearPos in gearPositions:
    gearNeighbours = set(neighbours(grid, gearPos))

    gearNumberCount = 0
    gearNumberList = []

    for numberEntry in numberPositions:
        numberSet = set(numberEntry[1])

        if (gearNeighbours & numberSet):
            # gear is touching this number
            gearNumberCount += 1
            gearNumberList.append(numberEntry[0])
    
    if gearNumberCount == 2:
        gearRatio = gearNumberList[0] * gearNumberList[1]
        gearRatioSum += gearRatio


print(gearRatioSum)


