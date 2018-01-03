def isPalindrome(x):
    dig = list(int(n) for n in str(x))
    while len(dig)!=0:
        if dig[0]==dig[-1]:
            dig = dig[1:-1]
        else:
            return False
    return True

def maxPalindromeProduct():
    res = 0
    for a in range(100, 1000):
        for b in range(100, 1000):
            if isPalindrome(a*b) and a*b > res:
                res = a*b
    return res
    
print maxPalindromeProduct()
