def selfPowers(n):
    res = 0
    for i in range(1,n+1):
        res += i**i
    return(res)

def getLastDigits(n,x):
    return(n % 10**x)

print(getLastDigits(selfPowers(1000),10))
