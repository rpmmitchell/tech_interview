import math

def checkUni(checkMe):
    uniDict = {}
    for count, value in enumerate(checkMe):
        uniDict[value] = count;
    print(uniDict)
    if len(uniDict) != len(checkMe):
        print('I do not have all unique values')
    else:
        print('I have all unique values')

def sockMerchant(n, ar):
    # figure out the pairs in the array, given the length
    matcher = []
    counter = 0
    for sock in ar:
        if sock not in matcher:
            print(sock)
            matcher.append(sock)
        else:
            continue
    for match in matcher:
        counter += math.floor(ar.count(match)/2)
    print(counter)

def countingValleys(steps, path):
    altitude = 0
    valleyCount = 0
    for step in path:
        if altitude == 0:
            primer = True
        else:
            primer = False
        if step == 'D' and primer == True:
            altitude -= 1
            valleyCount += 1
        elif step == 'D' and primer == False:
            altitude -= 1
        else:
            altitude += 1
    print(valleyCount)

def jumpingOnClouds(c):
    step = 0
    location = 0
    endOfArray = False
    while endOfArray == False:
        if (location + 2) < len(c):
            if(c[location + 2] != 1):
                step += 1
                location += 2
            else:
                step += 1
                location += 1
        else:
            if (location + 1) < len(c):
                step +=1
                location += 1
            else:
                endOfArray = True

    print(step)

def repeatedString(s, n):
    repeatTimes = math.floor(n/len(s))
    repeatRemain = n - repeatTimes * len(s)
    repeatValue = 0
    repeatTotal = 0
    for value in s:
        if value == 'a':
            repeatValue += 1
    for i in range(0, int(repeatRemain)):
        if s[i] == 'a':
            repeatTotal += 1
        else:
            continue
    repeatTotal += repeatTimes * repeatValue
    print(repeatTotal)





#sockMerchant method
#sockMerchant(9, [10,20,20,10,10,30,50,10,20,10])

#uniCheck
#checkUni('hello')

#valley count code
#countingValleys(8,'UDDDUDUU')

#clouds
#jumpingOnClouds([0,0,0,1,0,0])
repeatedString('aba',100)

