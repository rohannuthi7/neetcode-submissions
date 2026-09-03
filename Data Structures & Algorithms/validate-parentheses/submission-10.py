class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in pairs:
                if not stack:
                    return False
                if stack.pop() != pairs[char]:
                    return False
            else:
                stack.append(char)
                

        if stack:
            return False
        else:
            return True