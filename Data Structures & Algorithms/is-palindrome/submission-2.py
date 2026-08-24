class Solution:
    def isPalindrome(self, s: str) -> bool:

        simpleString = ""
        for char in s:
            if char.isalnum():
                simpleString += char
        
        simpleString = simpleString.lower()

        start = 0
        end = len(simpleString) - 1
        while end >= start:
            if simpleString[start] != simpleString[end]:
                return False
            start += 1
            end -= 1
        
        return True