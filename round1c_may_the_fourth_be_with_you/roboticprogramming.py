import sys
from collections import Counter


class Robot:
    def __init__(self, program):
        self.program = program
        self.cursor = 0
        self.beaten = False
        self._prev = None

    def next(self):
        if self.beaten is True: return None
        result =  self.program[self.cursor]
        self.cursor = (self.cursor + 1) % len(self.program)
        self._prev = result
        return result

    def prev(self):
        return self._prev

    def setBeaten(self):
        self.beaten = True

    def isBeaten(self):
        return self.beaten


def nextStep(others):
    if len(others) == 3:
        return (None,None)
    elif len(others) == 2:
        if "R" in others and "S" in others:
            return ("R","S")
        if "R" in others and "P" in others:
            return("P","R")
        if("S" in others and "P" in others):
            return ("S","P")
    elif len(others) == 1:
        if "S" in others: return ("R", "S")
        if "R" in others: return ("P", "R")
        else: return ("S", "P")
    else: raise Exception("empty input")

line = sys.stdin.readline()
T = int(line)
for t in range(T):
    N = int(sys.stdin.readline().split()[0])
    robots = []
    for n in range(N):
          program = sys.stdin.readline().split()[0]
          robots.append(Robot(program))
    solution = []
    for i in range(500):
        c = Counter([robot.next() for robot in robots if robot.isBeaten() == False])
        others = {i:j for (i,j) in c.items()}
        if len(others.keys()) == 0:
            break
        (nexts, kills) = nextStep(others.keys())
        #print("Next step for others " , others.keys(), " is " , nexts, " killing" , kills)
        if nexts is None:
            solution = ["I","M","P","O","S","S","I","B","L","E"]
            break
        else:
            solution.append(nexts)
            for robot in robots:
                if robot.isBeaten() == False and robot.prev() == kills: robot.setBeaten()

    if(any(robot.isBeaten() is False for robot in robots)):
        solution = ["I", "M", "P", "O", "S", "S", "I", "B", "L", "E"]




    print("Case #" + str(t+1)+ ": " + "".join(solution))