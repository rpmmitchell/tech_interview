def checkUni(checkMe):
    uniDict = {}
    for count, value in enumerate(checkMe):
        uniDict[value] = count;
    print(uniDict)
    if len(uniDict) != len(checkMe):
        print('I do not have all unique values')
    else:
        print('I have all unique values')

checkUni('heloo')
