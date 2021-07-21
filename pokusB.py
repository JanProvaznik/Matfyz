import sys
import math

def sumsquaresofvec(vec):
    global digits
    summ = 0
    for i in range(len(digits)):
        summ += vec[i] * digits[i]**2
    return summ

def checkRecursively(mindigitindex, currentvector, sumsquares):
    global dynarr, maxvec
    dynarr[sumsquares] = currentvector
    if currentvector ==maxvec:
        return
    for digit in range(mindigitindex, len(currentvector)):
        newvector = currentvector.copy()
        newvector[mindigitindex] -= 1
        while newvector[mindigitindex]==0:
            mindigitindex+=1
        newvector[digit] += 1
        newsum = sumsquaresofvec(newvector)
        #print(newvector)
        if dynarr[newsum]==0:
                checkRecursively(mindigitindex,newvector,newsum)

sys.setrecursionlimit(100000000)

n = int(input())
digits = list(sorted(list(map(int, input().split()))))
vecsize = len(digits)
maxvec =[0]*(vecsize-1) + [n]
dynarr = [0]*(n*max(digits)**2+100)
initvector =[n]+[0]*(vecsize-1)
checkRecursively(0,initvector, sumsquaresofvec(initvector))
print(dynarr)
for i in range(int(len(dynarr)**(1/3)+1)):
    if dynarr[i**3]!=0:
        x = dynarr[i**3]
        for j in range(len(digits)):
            print("".join([str(digits[j])]*x[j]),end="")
        break
