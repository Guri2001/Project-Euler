def is_prime(num):
    total = 0
    for i in range(2,int(int(num**0.5)+1)):
        if(num%i == 0):
            return False
    return True

def sum_primes(n):
    total = 0
    start = 1
    while(start < n):
        start+=1
        if(is_prime(start)):
            total += start
    return total

    


print(sum_primes(2000000))