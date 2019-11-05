import sys


def indexToCell(index, N):
    return (index % N, int(index / N))

def cellToIndex(col, row, N):
    return col + row * N

def getPossibleSteps(row,col, N, lydiaSteps, lidyaIndices):
    possibleSteps = ["S" , "E"]
    if col == N-1:
        possibleSteps.remove("E")
    if row == N-1:
        possibleSteps.remove("S")

    index = cellToIndex(col,row,N)
    if index in lidyaIndices:
        lydiaStep = lydiaSteps[lidyaIndices.index(index)]
        if lydiaStep in possibleSteps:
            possibleSteps.remove(lydiaStep)
    return possibleSteps


line = sys.stdin.readline()
T = int(line)
for t in range(T):
    N = int(sys.stdin.readline())
    lidyaSteps = sys.stdin.readline().strip()

    if lidyaSteps[-1] == "S": ## last step of Lydia is S so he was standing at the eastmost cell of the one-before-the-last row. I must enter te final cell from the west, meaning I have to go to south.
        preferEast = False
    else:
        preferEast = True

    lidyaIndices = list(lidyaSteps)
    lidyaIndices[0] = 0
    for i in range(1,len(lidyaIndices)):
        if lidyaSteps[i-1] == "S":
            lidyaIndices[i] = lidyaIndices[i-1] + N
        else:
            lidyaIndices[i] = lidyaIndices[i-1] + 1
    row = 0
    col = 0
    steps = []
    for i in range(2*N-2):
        index = cellToIndex(col, row, N)
        possibleSteps = getPossibleSteps(row,col,N,lidyaSteps,lidyaIndices)

        #print("step", i, "at RCI = ", row, col, "steps", steps)
        #print("possible steps" , possibleSteps)

        if len(possibleSteps) ==1:
            step = possibleSteps[0]
        elif len(possibleSteps) == 0:
            raise Exception("Cannot continue")
        elif preferEast:
            step = "E"
        else:
            step = "S"

        steps.append(step)
        if step =="S":
            row = row +1
        else:
            col = col + 1



    print("Case #" + str(t+1)+ ": " + str("".join(steps)) )