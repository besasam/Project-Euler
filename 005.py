# Smallest positive number that is divisible by all of the numbers from 1 to 20

n = 20
a = False
i = 1
while 1:
    for i <= 20:
        if n % i == 0:
            a = True
            i = i + 1
        else:
            a = False
            ???
    if a == True:
        print (n)
        break
    n = n + 1