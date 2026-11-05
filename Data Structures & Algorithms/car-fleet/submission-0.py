class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        times = [(target - x)/y for x,y in sorted(zip(position, speed), reverse = True)]

        stack = []
        
        for time in times:
            if not stack or time > stack[-1]:
                stack.append(time)
            else:
                continue
        
        return len(stack)
        
        

        