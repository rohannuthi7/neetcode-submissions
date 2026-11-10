class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + '#' + string
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            length = ''
            while s[i] != '#':
                length += s[i]
                i += 1
            
            length = int(length)
            decoded.append(s[i + 1:i + length + 1])
            i += length + 1

        return decoded

        