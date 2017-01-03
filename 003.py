# Largest prime factor of 600851475143

# Hilfsfunktion to check if prime
def checkPrime(a):
    for b in range (2,a):
        if a % b == 0:
       	    return False
    else:    
        return True

n = 600851475143	# Number whose largest prime factor is to be determined
i = 3				# Possible highest prime factor getting checked in the function
k = 2				# Current highest prime factor

while i <= n:							# Do this as long as i is a possible prime factor
    if n % i == 0 and checkPrime(i):	# Is i a factor of n and a prime?
       	k = i							# Set current highest prime factor to i
       	n = n / i						# Divide n by found prime factor
    i = i + 2							# Increment i
print (k)								# Print the last saved value of i 



