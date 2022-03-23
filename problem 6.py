n = int(input("Enter number: "))

square_sum = (n*(n+1)*(2*n+1))/6
sum_square = n*(n+1)/2
square_it = sum_square**2
print(int(square_it - square_sum))


