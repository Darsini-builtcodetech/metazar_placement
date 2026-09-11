stack = []

def push(value):
    stack.append(value)
    print(value, "pushed into stack")

def pop():
    if len(stack) ==0:  #Idhu stack empty-ah irukka? nu check pannudhu.
        print("stack underflow")
    else:
        value = stack.pop()
        print(value, "popped from stack:")   

def peek():
    if len(stack) ==0:
        print("stack underflow")
    else:
        print("Top element:",  stack[-1]) 
#peek
push(10)
push(20)
push(30)

#pop
peek()
 #pop
pop()

#peek again
peek()

#pop
pop()
pop()

#stack is empty now
pop()
peek()