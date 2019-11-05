# Although this code gets all the marks on the problem, I could not debug it in time and I received 0 points for this assignment.

import sys
import math

def getInitialRings210(value):
    # first 3 rings are modulo'ed out, determining the number of last 3.
    powers = [math.floor(210 / i) for i in range(1, 7)] [-3:]
    result = []
    for power in powers:
        coeff = int(math.pow(2, power))
        mod = int(math.floor(int(value) / int(coeff)))
        result.append(mod)
        value = value - mod * coeff
    return  result



def getInitialRings56(value, result252):
    powers52 = [math.floor(56 / i) for i in range(1,7) ] [:-3]
    powers252 = [math.floor(56 / i) for i in range(1, 7)][-3:]
    result = []

    for i in range(len(powers252)):
        value -= int(math.pow(2,powers252[i]) * result252[i])


    for power in powers52:
        coeff = int(math.pow(2,power))
        mod =  int(math.floor(int(value) / int(coeff)))
        result.append(mod)
        value = value - mod * coeff

    result.extend(result252)
    return result




line = sys.stdin.readline().split()
T = int(line[0])
W = int(line[1])

for t in range(T):
    print("210")
    sys.stdout.flush()
    value = int(sys.stdin.readline())
    if value < 0:
        sys.exit()
    result252 = getInitialRings210(value)
    print("56")
    sys.stdout.flush()
    value = int(sys.stdin.readline())
    if value < 0:
        sys.exit()
    result = getInitialRings56(value, result252)

    print(" ".join(map(str,result)))
    sys.stdout.flush()
    isOk = int(sys.stdin.readline())
    if isOk < 0:
        sys.exit()




