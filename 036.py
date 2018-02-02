def decToBin(n):
    return int(bin(n)[2:])

def getDigits(n):
    return [int(x) for x in str(n)]

def isPalindromic(n):
    if(len(n) == 0 or len(n) == 1):
        return True
    elif(n[0] == n[-1]):
        return isPalindromic(n[1:-1])
    else:
        return False

res = 0
i = 1
while(i < 1000000):
    if(isPalindromic(getDigits(i))):
        if(isPalindromic(getDigits(decToBin(i)))):
            res = res + i
    i += 1
print(res)
