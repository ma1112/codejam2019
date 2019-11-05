import sys
import math
import string

def factorizeEvenPrimeCode(code):
    result = []
    divisor = 3
    while len(result) == 0:
        if code % divisor ==0:
            result.append(divisor)
            result.append(int(code / divisor))
        divisor = divisor +2
    return result



def calculateFactors (code):
    factors = {}
    evens = list(filter(lambda x: x % 2 == 0, code))
    for even in evens:
        factors[even] = [2,int(even/2)]
    if len(evens) == 0:
        easiestCode = min(code)
        factors[easiestCode] = factorizeEvenPrimeCode(easiestCode)

    # at this point we factorized at least one code element.
    #print("at this point we factorized at least one code element." ,factors)

    startIndex = code.index(min(factors))
    for i in range(startIndex+1, len(code)):
        if code[i] not in factors:
            previousFactors = factors[code[i-1]]
            if  code[i] % previousFactors[0]  ==0:
                thisFactors = [previousFactors[0], int(code[i] / previousFactors[0])]
            else:
                thisFactors = [previousFactors[1], int(code[i] / previousFactors[1])]
            thisFactors.sort()
            factors[code[i]] = thisFactors


    for i in range(startIndex-1,-1,-1):
        if code[i] not in factors:
            previousFactors = factors[code[i + 1]]
            if code[i] % previousFactors[0]  == 0:
                thisFactors = [previousFactors[0], int(code[i] / previousFactors[0])]
            else:
                thisFactors = [previousFactors[1], int(code[i] / previousFactors[1])]
            thisFactors.sort()
            factors[code[i]] = thisFactors

    # a tthis point all code elements are factorized.

    if len(list(filter(lambda x: x not in factors, code)))>0:
        raise Exception("Not all code parts are factorized.")
    return factors

def getMessage(code, factors):
    message = [0 for i in range(len(code)+1)]

    ## finding the first code part of two different consec. elements

    for startIndex in range(len(code)):
        if code[startIndex] != code[startIndex+1]:
            break


    for i in range(startIndex, len(code)-1):
        possibleValues = set(factors[code[i]]).intersection(set(factors[code[i+1]]))
        if len(possibleValues) == 1:
            value = list(possibleValues)[0]
        elif len(possibleValues) ==0:
            raise Exception("No possible value at index " , i)
        else:
            value = list(possibleValues.difference({message[i]}))[0]

        message[i+1] = value

    lastFactors = factors[code[-1]]
    lastCalculatedMessage = message[-2]
    if lastFactors[0] == lastCalculatedMessage:
        message[-1] = lastFactors[1]
    else:
        message[-1] = lastFactors[0]

    for i in range(startIndex - 1 ,-1 ,-1):
        possibleValues = set(factors[code[i]]).intersection(set(factors[code[i + 1]]))
        if len(possibleValues) == 1:
            value = list(possibleValues)[0]
        elif len(possibleValues) == 0:
            raise Exception("No possible value at index ", i)
        else:
            value = list(possibleValues.difference({message[i + 2]}))[0]
        message[i + 1] = value

    firstFactors = factors[code[0]]
    firstCalculatedMessage = message[1]
    if firstFactors[0] == firstCalculatedMessage:
        message[0] = firstFactors[1]
    else:
        message[0] = firstFactors[0]

    letters = list(string.ascii_uppercase)
    primesOrdered = list(sorted(set(message)))


    primeToLetter = {}
    for i in range(len(letters)):
        primeToLetter[primesOrdered[i]] = letters[i]



    return "".join((map(lambda x: primeToLetter[x], message)))















line = sys.stdin.readline()
T = int(line)
for t in range(T):
    N = int(sys.stdin.readline().split()[0])
    code = [int(i) for i in sys.stdin.readline().split()]
    factors = calculateFactors(code)
    message = getMessage(code, factors)







    print("Case #" + str(t+1)+ ": " + message)