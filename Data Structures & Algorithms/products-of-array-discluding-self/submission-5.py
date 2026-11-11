class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefixArr = [1] * len(nums)
        suffixArr = [1] * len(nums)
        productArr = [1] * len(nums)

        for i in range(1, len(nums)):
            prefixArr[i] = prefixArr[i - 1] * nums[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            suffixArr[i] = suffixArr[i + 1] * nums[i + 1]

        for i in range(len(nums)):
            productArr[i] = suffixArr[i] * prefixArr[i]
        
        return productArr