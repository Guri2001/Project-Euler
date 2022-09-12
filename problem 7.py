#check if n is prime
def isPrime(n):
    if(n == 1):
        return False
    for i in range(2,int(n**0.5)+1):
        if(n%i == 0):
            return False
    return True

#Generate n prime numbers. 
def generatePrimeNumber(n):
    prime = 0
    count = 0
    while(count < n):
        prime+=1
        if(isPrime(prime)):
            count+=1        

    return prime
        
print(generatePrimeNumber(100))