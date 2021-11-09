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





#sockMerchant method
#sockMerchant(9, [10,20,20,10,10,30,50,10,20,10])

#uniCheck
#checkUni('hello')

#valley count code
#countingValleys(8,'UDDDUDUU')


