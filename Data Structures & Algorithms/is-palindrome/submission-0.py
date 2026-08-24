class Solution:
    def isPalindrome(self, s: str) -> bool:
        #remove spaces and lowercase everything
        # set one pointer at the start and one at the end and increment each other - if they ever cross or equal each other return true. Before that, return false if the values at the pointers are different from one another, otherwise, increment start and decrement end.

        simpleString = ""
        for char in s:
            if char.isalnum():
                simpleString += char
        
        simpleString = simpleString.lower()
        print(simpleString)
        start = 0
        end = len(simpleString) - 1
        while end >= start:
            if simpleString[start] != simpleString[end]:
                return False
            start += 1
            end -= 1
        
        return True