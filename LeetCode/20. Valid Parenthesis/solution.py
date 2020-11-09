class Solution:
    def isValid(self, s: str) -> bool:
        stack = ['x']
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif c == ')':
                curr = stack.pop()
                if curr != '(':
                    return False
            elif c == ']':
                curr = stack.pop()
                if curr != '[':
                    return False
            elif c == '}':
                curr = stack.pop()
                if curr != '{':
                    return False
        if len(stack) > 1:
            return False
        else:
            return True