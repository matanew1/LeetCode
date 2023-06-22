parentheses = {')': '(', '}': '{', ']': '['}
open = ['(', '[', '{']
close = [')', ']', '}']

def valid_parentheses(string: str):
    #define empty stack
    stack = []

    for char in string:
        # if char is open parentheses
        if char in open:
            # push the char to the stack
            stack.append(char)

        # if char is close parentheses
        elif char in close:
            # if stack is empty or the open is not type of the close one
            if not stack or stack.pop() != parentheses[char]:
                return False
    # return true if the stack is empty
    return len(stack) == 0


assert valid_parentheses("[(])") == False
assert valid_parentheses("[])") == False
assert valid_parentheses("[]()") == True
assert valid_parentheses("(())") == True
assert valid_parentheses("(){}") == True
assert valid_parentheses("[(){})") == False
assert valid_parentheses("((){})") == True
