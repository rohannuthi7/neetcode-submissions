class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        notepad = set()

        for num in nums:
            if num in notepad:
                return True
            
            notepad.add(num)

        return False