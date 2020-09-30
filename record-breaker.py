def cond1(l1,i):
    if(i == 0):
        return cond2(l1,i)
    cur = l1[i];
    for j in range(i):
        if(cur <= l1[j]):
            return False
    return True

def cond2(l1,i):
    if(i == len(l1)-1):
        return cond1(l1,i)
    if(l1[i] <= l1[i+1]):
        return False
    return True

tc = int(input())
case = 1
while(tc):
    res = 0
    N = int(input())
    l1 = [int(x) for x in input().split(" ")]
    for i in range(len(l1)):
        if(cond1(l1,i) and cond2(l1,i)):
            res = res + 1
    print("Case #{0}: {1}".format(case,res))
    case = case + 1
    tc = tc - 1
