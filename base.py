def  print_numbers(n):  #print_numbers() nu oru function create painnurom|n=number
    #Base case
    if n == 0:  #n = 0 aana function stop
        return

    #Recursive call 

    print_numbers(n-1)  #Current number-a vida 1 kammi panni function-a call pannudhu.
    print(n)

print_numbers(5)    