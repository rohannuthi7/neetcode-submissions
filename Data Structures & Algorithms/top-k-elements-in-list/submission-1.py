class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        top = []

        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        pairs = sorted(frequency.items(), key=lambda pair: pair[1], reverse = True)

        for i in range(k):
            top.append(pairs[i][0])
        
        return top
