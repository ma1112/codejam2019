## Unfortunately I misunderstood this problem. or/and had no time to finish the code so it uses a recursion.

import sys
import copy

class Map:
    def __init__(self, C, R, map):
        self.C = C
        self.R = R
        self.size = R*C
        self.map = [m for m in map]
        self.free = self._initFree()


    def getMap(self):
        return "".join(self.map)

    def getFree(self):
        return self.free.copy()

    def RCToIndex(self, r,c):
        return r * self.C + c

    def indexToRC(self, index):
        r = int(index / self.C)
        c = index % self.C
        return (r,c)

    def _initFree(self):
        return [i for i in range(self.R * self.C) if self.map[i] =="."]

    def isValidStep(self, index, bacType):
        if bacType == "H" : return self._isValidH(index)
        else: return self._isValidV(index)


    def step(self, index, bacType):
        #print("stepping index " , index, "which is rc " , self.indexToRC(index))
        self.free.remove(index)
        if bacType == "H": self._stepH(index)
        else: self._stepV(index)

    def _stepH(self, index):

        (r,c) = self.indexToRC(index)

        for cc in range(c, self.C):
            ii = self.RCToIndex(r,cc)
            if self.map[ii] == ".":
                self.map[ii] = "B"
                if ii in self.free:
                    self.free.remove(ii)
            else: break

        for cc in range(c-1, -1,  -1):
            ii = self.RCToIndex(r, cc)
            if self.map[ii] == ".":
                if ii in self.free:
                    self.free.remove(ii)
                self.map[ii] = "B"
            else: break

    def _stepV(self, index):

        (r, c) = self.indexToRC(index)

        #print("cleaning from " , r ,c)

        for rr in range(r, self.R):
            ii = self.RCToIndex(rr, c)

            if self.map[ii] == ".":
                if ii in self.free:
                    self.free.remove(ii)
                self.map[ii] = "B"
            else:
                break

        for rr in range(r - 1, -1, - 1):
            ii = self.RCToIndex(rr, c)
            #print("cleaning index ", ii)
            if self.map[ii] == ".":
                if ii in self.free:
                    self.free.remove(ii)
                self.map[ii] = "B"
            else:
                break


    def getRow(self, r):
        return self.map[r * self.C : ((r+1) * self.C) ]

    def getCol(self, c):
        return [self.map[self.RCToIndex(r,c)] for r in range(self.R)]

    def _isValidH(self, index):
        (r,c) = self.indexToRC(index)
        row = self.getRow(r)
        #print("index " , index , "r" , r , "c" , c , "row" , row)
        if(row[c]) != "." : return False
        for cc in range(c+1,len(row)):
            if row[cc] == "#" : return False
            if row[cc] == "B": break

        for cc in range(c-1, -1, -1):
            if row[cc] == "#" : return False
            if row[cc] == "B": break
        return True

    def _isValidV(self, index):
        (r, c) = self.indexToRC(index)
        col = self.getCol(c)
        if (col[r]) != ".": return False
        for rr in range(r + 1, len(col)):
            if col[rr] == "#": return False
            if col[rr] == "B": break

        for rr in range(r - 1, -1, -1):
            if col[rr] == "#": return False
            if col[rr] == "B": break
        return True



def play(C,R, mapString):
    seenConfigurations = {}
    wins = 0
    startMapObj = Map(C,R,mapString)
    statIndices = copy.deepcopy(startMapObj.getFree())
    for startIndex in statIndices:
        for startBacType in ["H","V"]:
            if(startMapObj.isValidStep(startIndex, startBacType)):
                (winner, configs) = playSingleGame(C,R,mapString, startIndex, startBacType, seenConfigurations)
                #print("Winner is " , winner, "\n")
                if winner == 0:
                    wins += 1
                    #print("First player wins with first step " , startIndex, startBacType, seenConfigurations)
                for (config, value) in configs.items():
                    if value == winner:
                        seenConfigurations[config] = "W"
                    else:
                       seenConfigurations[config] = "L"
    return wins


def playSingleGame(C,R,mapString, startIndex, startBacType, seenConfigurations):
    seenConfigurationsThisGame = {}
    mapObj = Map(C,R,mapString)

    player = 0
    index = startIndex
    bacType = startBacType

    while (True):
        #print("starting game")
        if index is None or bacType is None:
            winner = (player+1)%2
            return (winner, seenConfigurations)
        #print("player " , player , " steps " , index, " type " , bacType)
        mapObj.step(index, bacType)
        player = (player+1) %2
        if mapObj.getMap() in seenConfigurations:
            winner = player if seenConfigurations[mapObj.getMap()] == "W" else (player+1)%2
            return (winner, seenConfigurations)
        seenConfigurationsThisGame[mapObj.getMap()] =  player

        index = None
        bacType = None
        #print("free cells: " , mapObj.getFree())
        for ii in mapObj.getFree():
             #print("ii " , ii)
            for tt in ["H", "V"]:
                if mapObj.isValidStep(ii, tt):
                    index = ii
                    bacType = tt
                    break










line = sys.stdin.readline()
T = int(line)
for t in range(T):
    line = sys.stdin.readline()
    R = int(line.split()[0])
    C = int(line.split()[1])
    mapString = "".join([sys.stdin.readline().split()[0] for r in range(R)])
    result = play(C,R,mapString)










    print("Case #" + str(t+1)+ ": " + str(result))