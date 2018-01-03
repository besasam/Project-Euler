def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def sieve(n):
    res = list(range(2,n+1))
    i = 0
    while i < len(res):
        k = i + res[i]
        while k < len(res):
            if isPrime(res[k])==False:
                del res[k]
            k = k + res[i] - 1
        i = i + 1
    return res

def primeSum(n):
    primes = sieve(n)
    res = 0
    for i in range(0, len(primes)):
        res = res + primes[i]
    return res

print primeSum(2000000) # it works, but it's slow as fuck
