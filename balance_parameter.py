def check_sequence(actions):    #check_sequence nu function create painnurom|action=namma action list
    stack = []       # why emptuy list na open action-a temporary-aa store panna

    for action in actions:  #list-la irukkura action-a one by one edukkum
        # Check if  the action os "open"
        if action == "OPEN":

            #if yes, store/push the action into the stack
            stack.append(action)
        else:
            #chek if the stack is empty when  a CLOSE action appears
            if len(stack) == 0:

                # if the stack is empty, there is no corresponding OPEN, so return Faise
             return False
            stack.pop()

            #Check if the stack os empty at the end of the return True if balance, else False
    return len(stack) == 0

        #Test the function with a sample list of actions and print the result
actions = ["OPEN", "OPEN", "CLOSE", "CLOSE"]
print(check_sequence(actions))
            

    

