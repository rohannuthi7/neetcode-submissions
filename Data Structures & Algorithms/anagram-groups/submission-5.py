class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for str in strs:
            frequency = [0] * 26
            for char in str:
                frequency[ord(char) - ord('a')] += 1
            
            anagrams[tuple(frequency)].append(str)
        
        return list(anagrams.values())
        