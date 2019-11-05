import sys


def updateDict(dict, values):
    for value in values:
        if value in dict:
            dict[value] = dict[value]+1
        else:
            dict[value] = 1
    return dict

def findMostProbableInDict(dict):
    mostProbableValue = 0
    mostProbableCounts = 0
    for value,count in dict.items():
        if mostProbableCounts < count or (mostProbableCounts == count and value < mostProbableValue):
            mostProbableCounts = count
            mostProbableValue = value
    return mostProbableValue


line = sys.stdin.readline()
T = int(line)
for t in range(T):
    line = sys.stdin.readline().split()
    P = int(line[0])
    Q = int(line[1])

    xs = {}
    ys = {}
    for i in range(P):
        line = sys.stdin.readline().split()
        xi = int(line[0])
        yi = int(line[1])
        diri = line[2]

        if diri == "S":
            ys = updateDict(ys, range(yi))
        elif diri =="N":
            ys = updateDict(ys, range(yi+1, Q+1))
        elif diri == "E":
            xs = updateDict(xs, range(xi+1, Q+1))
        else:
            xs = updateDict(xs, range(xi))




    print("Case #" + str(t+1)+ ": " + str(findMostProbableInDict(xs)) + " " + str(findMostProbableInDict(ys)))