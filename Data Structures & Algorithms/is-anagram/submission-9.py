class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False

        mapS = defaultdict(int)
        mapT = defaultdict(int)

        for char in s:
            mapS[char] += 1
        
        for char in t:
            mapT[char] += 1

        return mapS == mapT
        