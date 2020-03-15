#  Given a number N return the index value of the Fibonacci sequence, where the sequence is:

#  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...
#  the pattern of the sequence is that each value is the sum of the 2 previous values, that means that for N=5 → 2+3

# For example: fibonacciRecursive(6) should return 8

def fibonacciRecursive(n):
    if n < 2:
        return n
    return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)

def FibonacciIterative(n):
    fibList = []
    for i in range(n+1):
        if i == 0:
            fibList.append(0)
        elif i == 1:
            fibList.append(1)
        else:
            fibList.append(fibList[i-1]+fibList[i-2])
    return fibList[n]

print(FibonacciIterative(7))
print(fibonacciRecursive(6))
    


