def fibonacci(n): #fibonacci → function name.
#n → namma entha Fibonacci position/number calculate pannanum nu represent pannudhu.
    if n <= 1:
        return n 

    return fibonacci(n -1) + fibonacci(n - 2)

print(fibonacci(5))