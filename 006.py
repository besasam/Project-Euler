def sumOfSquares(x):
    res = 0
    for i in range(1, x+1):
        res = res + i*i
    return res

def sumSquared(x):
    res = 0
    for i in range(1, x+1):
        res = res + i
    res = res*res
    return res

print (sumSquared(100) - sumOfSquares(100))
