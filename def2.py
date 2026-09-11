def countdown(n):   #countdown nu oru function create pannrom. |n = namma kudukkura number.

    if n == 0:    #n = 0 aana function-a stop pannu. |base case
        return

    print(n)

    countdown(n-1)

countdown(3)        