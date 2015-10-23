# Find the sum of all the multiples of 3 or 5 below 1000.

n = 0
i = 1
while i < 1000:
    if i % 3 == 0:
        n = n + i
    else:
        if i % 5 == 0:
            n = n + i
    i = i + 1
print n
