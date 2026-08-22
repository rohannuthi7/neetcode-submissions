class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + "#" + string
        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        
        i = 0
        while i < len(s):
            lengthString = ""
            while s[i] != "#":
                lengthString += s[i]
                i += 1
            
            length = int(lengthString)

            start = i + 1
            result.append(s[start : start + length])
            i = start + length
        
        return result