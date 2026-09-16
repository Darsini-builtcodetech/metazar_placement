stack = []

while True:           #Idhu program-a continue-ah run pannum.
    print("\n-- Stack Menu --")
    print("1. push")
    print("2. pop")
    print("3. peek")
    print("4. Display")
    print("5. Exit")

    Choice = int(input("Enter your choice:"))

    if choice == 1:
        value = int(input("Enter value: "))
        stack.append(value)
        print(value, "pushed to stack")

    elif choice == 2:
        if len(stack) == 0:
            print("Stack underflow")
        else:
            value = stack.pop()
            print(value, "popped from stack")

    elif choice == 3:
        if len(stack) == 0:
            print("stack underflow")
        else:
            print("Top element:", stack[-1])

    elif choice == 4:
        if len(stack) == 0:
            print("stack is empty")
        else:
            print("Stack:", stack)

    elif choice == 5:
        print("Program ended")
        break

    else:
        print("Invalid choice")                                         