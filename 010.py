def sieve(n):
    res = list(range(2,n+1))
    for i in range (0, len(res)):
        for k in range(i+1,len(res)):
            if i<len(res) and k<len(res):
                if res[k]%res[i]==0:
                    del res[k]
    return res

def primeSum(n):
    primes = sieve(n)
    res = 0
    for i in range(0, len(primes)):
        res = res + primes[i]
    return res

print primeSum(2000000)
