'''
Problem: Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[', and ']',
determine if the input string is valid
'''
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)

parentheses = {'(': ')', '{': '}', '[': ']'}

def valid_parentheses(string: str):
    stack = Stack()
    for char in string:
        # if char is open parentheses push to the stack
        if char in parentheses.keys():
            stack.push(char)
        # if char is close parentheses pop the stack
        if char in parentheses.values():
            peek = stack.peek()
            if peek is None:
                return False
            if parentheses[peek] == char:
                stack.pop()
    if stack.is_empty():
        return True



print(valid_parentheses("(1,[2,l,l,u],{h: 1,v: 2})"))