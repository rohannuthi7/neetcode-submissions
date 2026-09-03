class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        for char in s:
            if char in {'(', '{', '['}:
                stack.append(char)
            elif stack:
                if char == '}':
                    if stack.pop() != '{':
                        return False
                elif char == ')':
                    if stack.pop() != '(':
                        return False
                elif char == ']':
                    if stack.pop() != '[':
                        return False
            else:
                return False

        if stack:
            return False
        else:
            return True