

def isFactorial(n):
    if n==1:
     return 1
    else:
     return  n*factorial(n-1)

number = int(input("Enter the number: "))    
    
result = isFactorial(number)
# print the result of factorial
print(result)