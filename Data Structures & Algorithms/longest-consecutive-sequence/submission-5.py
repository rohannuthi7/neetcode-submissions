class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #create an identical set and an empty max length variable for an int set to 0. Then check through this set starting with the first number set to a variable called curr number, and check if a number one higher exists - if yes, then remove the current number from the set and set the new variable to the curr number and increment currLength. If the next highest does not exist, then check if currLength is greater than max length - assign if it is. If not, then reset currLength back to 0. Then, find the next highest number in the set and continue on the process from there with the comparion. Finally, return max length. The only problem is how to pick the lowest remaining number in a set consistently without sorting the set first

        sameSet = set(nums)
        maxLength = 0
        for num in sameSet:
            currLength = 1
            if num - 1 in sameSet:
                continue
            
            nextNum = num + 1
            while nextNum in sameSet:
                currLength += 1
                nextNum += 1
            
            if currLength > maxLength:
                maxLength = currLength
        
        return maxLength
            