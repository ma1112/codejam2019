import sys

line = sys.stdin.readline()
T = int(line)
for t in range(T):
    line = sys.stdin.readline().strip()
    num1 = list(line)
    num2 = list(line)
    for i in range(len(num1)):
        if num1[i] == "4":
            num1[i] = "2"
            num2[i] = "2"
        else:
            num2[i] = "0"
    print("Case #" + str(t+1)+ ": " + str(int("".join(num1))) +  " " + str(int("".join(num2))) )