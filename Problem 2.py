MAX_FIB = 4000000

a=1
b = 2
total = 0
for i in range(100):
    a,b = b, a+b

    if(a < MAX_FIB and a%2 == 0):
    
        total +=a

answer =  4613732
if(answer == total):
    print("Passed")