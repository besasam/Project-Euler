# Find the sum of even-valued terms (whose value does not exceed four million) in the Fibonacci sequence.

a = 1
b = 1
c = 0
n = 0

while b <= 4000000:
    if b % 2 == 0:
        n = n + b
    c = a
    a = b
    b = c + b
print (n)