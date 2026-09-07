def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n-1)  #Same function-a, one smaller value-oda call panrom.

answer = factorial(5)

print(answer)