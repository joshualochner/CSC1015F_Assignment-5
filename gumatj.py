from math import log
def gumatj_to_decimal(a):
    numToReturn = 0
    pos = 0
    for i in str(a)[::-1]:
        numToReturn += 5**pos * int(i)
        pos+=1
    return numToReturn

def decimal_to_gumatj(a):
    currentNum = a
    getStarting = 0
    toReturn = ""
    
    while (5**(getStarting+1))<=a:
        getStarting+=1
    
    for i in range(getStarting,-1,-1):
        q = currentNum//(5**i)
        currentNum-=(5**i)*q
        toReturn+=str(q)
    return(int(toReturn))

def gumatj_add(a,b):
    return decimal_to_gumatj(gumatj_to_decimal(a)+gumatj_to_decimal(b))

def gumatj_multiply(a,b):
    return decimal_to_gumatj(gumatj_to_decimal(a)*gumatj_to_decimal(b))