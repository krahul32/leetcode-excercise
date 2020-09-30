tc = int(input())

def substring(l1):
    index = 0
    while index < len(l1) - 1:
        if((l1[index] == 0 and l1[index+1] == 1) or (l1[index] == 1 and l1[index+1] == 0)):
            del l1[index]
            del l1[index+1]
            return True
        else:
            index = index + 1
        if index == len(l1) - 1:
            return False
while tc:
    temp1 = int(input())
    temp2 = int(input())
    l1 = [int(x) for x in str(temp2)]
    person = 1 # John will start the game
    while substring(l1):
        person = person + 1
    if(person & 1):
        print("Joe")
    else:
        print("John")
    tc = tc-1
