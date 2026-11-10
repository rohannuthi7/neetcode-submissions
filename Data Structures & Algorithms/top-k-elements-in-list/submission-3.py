class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for num in nums:
            if num not in frequency:
                frequency[num] = 0;
            else:
                frequency[num] += 1
        
        top = sorted(frequency, key=frequency.get, reverse = True)
        
        return top[0:k]