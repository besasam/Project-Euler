# Smallest positive number that is divisible by all of the numbers from 1 to 20

def smallestMultiple(x):
    res = 0
    i = x
    while res==0:
        flag = True
        for k in range(1, x+1):
            if i%k!=0:
                flag = False
        if flag==True:
            res = i
        i = i + x
    return res

print smallestMultiple(20)
