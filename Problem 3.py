import math

factor = 600851475143  

largest_factor = 0
for i in range(2,int(math.sqrt(factor)+1)):
    if(factor%i == 0):
        largest_factor = i
        factor //= i

print(largest_factor)
