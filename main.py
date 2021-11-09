def checkUni(checkMe):
    uniDict = {}
    for count, value in enumerate(checkMe):
        uniDict[value] = count;
    print(uniDict)
    if len(uniDict) != len(checkMe):
        print('I do not have all unique values')
    else:
        print('I have all unique values')


#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

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


#sockMerchant method
sockMerchant(9, [10,20,20,10,10,30,50,10,20,10])

checkUni('hello')