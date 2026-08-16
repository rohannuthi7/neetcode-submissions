class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False

        firstWord = {}

        for char in s:
            firstWord[char] = firstWord.get(char, 0) + 1

        for char in t:
            if char not in firstWord or firstWord[char] == 0:
                return False

            firstWord[char] -= 1
        
        return True