# Largest prime factor of 600851475143

n = 600851475143
i = 3
k = 2

while i < 600851475143:
    for j in range (2,i):
        if (i % j) == 0:
            i = i + 2
        else:
            k = i
            i = i + 2
print (k)