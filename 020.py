def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def factorialSum(n):
    return (sum(map(int, str(factorial(n)))))

print (factorialSum(100))
