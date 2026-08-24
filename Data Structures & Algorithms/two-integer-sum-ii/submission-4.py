class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # pointers at opposite end of the number - if start + end is less, decrement the top pointer, if more, increment the bottom pointer - continue while the end >= start

        start = 0
        end = len(numbers) - 1
        while numbers[start] + numbers[end] != target:
            if numbers[start] + numbers[end] < target:
                start += 1
            if numbers[start] + numbers[end] > target:
                end -= 1
        
        return [start + 1, end + 1]