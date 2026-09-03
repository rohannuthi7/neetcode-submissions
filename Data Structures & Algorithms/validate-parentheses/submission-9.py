class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in {'(', '{', '['}:
                stack.append(char)
            elif not stack:
                return False
            else:
                if stack.pop() != pairs[char]:
                    return False

        if stack:
            return False
        else:
            return True