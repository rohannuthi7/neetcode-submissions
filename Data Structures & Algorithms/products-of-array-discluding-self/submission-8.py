class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)

        productArr = [1] * length

        preProduct = 1
        for i in range(length):
            productArr[i] *= preProduct
            preProduct *= nums[i]
        
        postProduct = 1
        for i in range(length - 1, -1, -1):
            productArr[i] *= postProduct
            postProduct *= nums[i]
        
        return productArr
        