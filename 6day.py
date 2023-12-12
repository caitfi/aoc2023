f = open("input/6.txt", "r").readlines()

# part 1
times = [int(x) for x in f[0].strip().split(" ")[1:] if x.isdigit()]
distances = [int(x) for x in f[1].strip().split(" ")[1:] if x.isdigit()]

# part 2
time = int("".join(f[0].strip().split(" ")[1:]))
distance = int("".join(f[1].strip().split(" ")[1:]))

print(times)
print(distances)

productValidWins = 1

# part 1
for i in range(0, len(times)):
    raceLength = times[i]
    recordDistance = distances[i]

    validWins = [x for x in range(0, raceLength) if (x)*(raceLength-x) > recordDistance]
    productValidWins *= len(validWins)

print(productValidWins)

# part 2
# find lower bounds and upper bounds? rather than every single one?
lowerBound = 0
while True: 
    if (lowerBound)*(time-lowerBound) > distance:
        break

    lowerBound += 1

upperBound = time
while True:
    if (upperBound)*(time-upperBound) > distance:
        break
    
    upperBound -= 1

print(upperBound-lowerBound + 1)
