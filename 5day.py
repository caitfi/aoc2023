def evaluateSeedLocations(seeds, mappingList):
    minLocation = 99999999999999999999

    # evaluate each seed against maps
    for seed in seeds:
        seedStages = [seed]    
        # each map is in stages, first being the initial seed
        for stage in mappingList:
            # last value we worked out
            lastStageValue = seedStages[-1]
            valueMapped = False
            newMapValue = -1

            for map in stage:
                # [dest start, src start, range length]
                if map[1] <= lastStageValue < map[1] + map[2]:
                    # mapping applies
                    valueMapped = True
                    newMapValue = map[0] + (lastStageValue - map[1])
                    break


            if not valueMapped:
                newMapValue = lastStageValue
            
            seedStages.append(newMapValue)
        
        # seed has reached the end location
        if (seedStages[-1] < minLocation):
            minLocation = seedStages[-1]
    
    return minLocation

def reverseSeedFromLocation(location, mappingList):
    locationStages = [location]

    for stage in reversed(mappingList):
        lastStageLocation = locationStages[-1]
        valueMapped = False
        newMapValue = -1

        for map in stage:
            # [src start, dest start, range length]
            if map[0] <= lastStageLocation < map[0] + map[2]:
                # mapping applies
                valueMapped = True
                newMapValue = map[1] + (lastStageLocation - map[0])
                break
            
        if not valueMapped:
            newMapValue = lastStageLocation
        
        locationStages.append(newMapValue)
            

    return locationStages[-1]


f = open("input/5.txt", "r")

sections = [x for x in f.read().split("\n\n") if x]

# get seed numbers
seedsPart1 = [int(x) for x in sections[0].strip().split() if x.isdigit()]

# parse maps
mappingList = []

for mapInstruction in sections[1:]:
    individualMap = []
    # split into lines, ignoring title
    lines = mapInstruction.split("\n")[1:]
    for line in lines:
        # break into values for map
        mapValues = [int(x) for x in line.split(" ") if x.isdigit()]
        individualMap.append(mapValues)
    
    mappingList.append(individualMap)

# part 1
locationValue = evaluateSeedLocations(seedsPart1, mappingList)
print(locationValue)

# build ranges for part 2
seedsPart2Ranges = []
for i in range(0, len(seedsPart1), 2):
    seedsPart2Ranges.append([seedsPart1[i], seedsPart1[i] + seedsPart1[i + 1]])

location = 0
seedFound = False

while not seedFound:
    seed = reverseSeedFromLocation(location, mappingList)

    for range in seedsPart2Ranges:
        if range[0] <= seed < range[1]:
            seedFound = True
            print(location)
            break

    if not seedFound:
        location += 1


# part 2 - reverse lookup?
