class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)

        for num in nums:
            frequency[num] += 1
        
        pairs = sorted(frequency.items(), key=lambda pair: pair[1], reverse = True)
        
        return [pairs[i][0] for i in range(k)]
