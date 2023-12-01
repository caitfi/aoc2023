import re

f = open("input/1.txt", "r")

words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
wordnums = ["1","2","3","4","5","6","7","8","9"]
sum = 0

# part 1
for line in f:
    firstlast = 0
    digits = [x for x in line if x.isdigit()]
    if len(digits) > 0:
        firstlast = int(digits[0] + digits[-1])

    sum += firstlast

print(sum)

# part 2
sum = 0
f.seek(0)

for line in f:
    digits = []
    firstlast = 0

    # find first occurrence of a number
    for x, char in enumerate(line):
        # handle outright numbers 
        if char.isdigit():
            digits.append(char)

        else:
            # look for a 'number word' at this index
            for y, word in enumerate(words):
                occurrences = line.count(word)

                # only one occurrence of 'number word'
                found = line.find(word) == x

                # more than one occurrence of that 'number word' in the string
                if not found and occurrences >= 1:
                    found = False
                    startindex = line.find(word)
                    
                    while (startindex < x and startindex != -1):
                        startindex = line.find(word, startindex + 1)
                        if (startindex == x):
                            found = True
                            break
                    
                if(found):
                    digits.append(wordnums[y])
    
    if len(digits) > 0:
        firstlast = int(digits[0] + digits[-1]) 
    else:
        print("WARNING!!! no digits this line")

    sum += firstlast

print(sum)


