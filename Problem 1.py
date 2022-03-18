MAX = 1000
total = 0
for i in range(MAX):
    if(i%3 == 0 or i%5 == 0):
        total += i
print(total)

#Another solution
ans = sum(i for i in range(1000) if(i%3 == 0 or i%5 == 0))
print(ans)
