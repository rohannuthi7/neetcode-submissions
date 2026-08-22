class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # orig: 1, 2, 4, 6

        # pref: 1, 1, 2, 8 || # suff: 48, 24, 6, 1
        

        prefixArray = [1] * len(nums)
        
        for i in range(1, len(nums), 1):
            prefixArray[i] = prefixArray[i-1] * nums[i-1]

        suffixArray = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            suffixArray[i] = suffixArray[i + 1] * nums[i+1]

        resultArray = [0] * len(nums)
        for i in range(0, len(nums), 1):
            resultArray[i] = prefixArray[i] * suffixArray[i]

        return resultArray