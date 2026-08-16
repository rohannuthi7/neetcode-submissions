class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        exists = {}
        for i, n in enumerate(nums):
            difference = target - n
            if difference in exists:
                return [exists[difference], i]

            exists[n] = i;