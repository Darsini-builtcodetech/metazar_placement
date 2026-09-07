def print_numbers(n):
    if n == 0:
        return

    print(n) #current value print

    print_numbers(n - 1)   # Function-a again call panrom

print_numbers(5)    