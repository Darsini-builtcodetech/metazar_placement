def is_valid(s):    #is_valid() nu oru function create panrom. |s = input bracket string

    stack = []

    pairs = {
        ')':'(',
        '}':'{',
        ']':'['
    }

    for char in s:  #String-la irukkura each character-a one by one edukkum.
        if char in "([{":
            stack.append(char)

        else:
            if len(stack)==0:
                return False

            if stack[-1] != pairs[char]:
                return False
            stack.pop()
    return len(stack) == 0

print(is_valid("{[()]}"))

                