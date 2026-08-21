class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        newMap = {}
        for num in nums:
            newMap[num] = newMap.get(num, 0) + 1

        # pass 2 is to change from nums and keys to frequencies as the key
        inverseArray = [[] for _ in range(len(nums) + 1)]
        for number, frequency in newMap.items():
            inverseArray[frequency].append(number)

        result = []
        for frequency in range(len(inverseArray) - 1, 0, -1):
            for number in inverseArray[frequency]:
                result.append(number)
            
            if len(result) == k:
                return result
        
        return result
            # Start at the highest frequency and work backwards adding them to the list until the resulting array size is equal to k


        # pass 3 is take the inner buckets with numbers and add nums to array
        

        
        
        
