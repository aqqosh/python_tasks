def isValid(s: str) -> bool:
    
    stack = []
    
    brackets = {
        "(" : ")",
        "{" : "}",
        "[" : "]"
    }
    
    openers = set(brackets.keys())
    closers = set(brackets.values())
    
    for symb in s:
        if symb in openers:
            stack.append(symb)
        else:
            if (symb not in closers) or (len(stack) == 0):
                return False
            
            last_opener = stack.pop()
            
            if symb != brackets[last_opener]:
                return False
            
    if len(stack) == 0:
        return True     
       
    return False


isValid("]")
