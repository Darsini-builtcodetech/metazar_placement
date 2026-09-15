stack = []
def Is_empty():           #“Stack empty-ah irukka illaya?”
#inside function
    return len(stack) == 0
def size():
    return len(stack)
stack.append(10)     #Ippo actual Stack-la values add pannuvom
stack.append(20)
stack.append(30)
print("stack:", stack)      #Stack-la currently enna values irukku-nu paakanum.

    #main part of the program
print("Is_empty:", Is_empty())        #Why is_empty() call panrom?

#|Namma Stack empty-ah irukka-nu check pannanum.
print("Size:", size())                #Why size() call panrom?
