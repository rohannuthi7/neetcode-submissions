class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        tally = {}
        for char in s:
            if char in tally:
                tally[char] += 1
            else:
                tally[char] = 1
        
        for char in t:
            if char not in tally or tally[char] == 0:
                return False  
            tally[char] -= 1

        return True