import sys
import string
# you can write to stdout for debugging purposes, e.g.
# print ""this is a debug message""
def solution(S,T):

    d = {chr(y): y-64 for y in range(65,91)}   #dict_variable = {key:value for (key,value) in dictonary.items()}
    print(d.items())
    ST = 1
    TT = 1
    for i in S:
        ST = ST*d[i]
    for j in T:
        TT = TT*d[j]

    if(ST%47 == TT%47):
        print("CHOSEN")
    else:
        print("NOT CHOSEN")
    return

# Following is the part of the program and is provided as an assistance to read the input.
# S = sys.stdin.readline().strip()
# T = sys.stdin.readline().strip()

S = str(input("Enter Student's Name: "))
T = str(input("Enter Teacher's Name: "))
solution(S,T)
