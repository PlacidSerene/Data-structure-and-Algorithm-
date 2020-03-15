def factorial(n):
    if n==1:
        return 1
    f = n*factorial(n-1)
    return f 
print(factorial(3))

