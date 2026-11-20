class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prevProduct = [1] * length
        postProduct = 1
        productArr = [nums[-1]] * length

        for i in range(1, length):
            prevProduct[i] = nums[i - 1] * prevProduct[i - 1]
        
        for i in range(length - 1, -1, -1):
            productArr[i] = prevProduct[i] * postProduct
            postProduct *= nums[i]
        
        return productArr
        