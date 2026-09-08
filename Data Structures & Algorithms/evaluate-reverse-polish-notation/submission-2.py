class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for item in tokens:
            if item == "+":
                second = stack.pop()
                first = stack.pop()
                
                stack.append(first + second)
            elif item == "-":
                second = stack.pop()
                first = stack.pop()
                
                stack.append(first - second)
            elif item == "*":
                second = stack.pop()
                first = stack.pop()
                
                stack.append(first * second)
            elif item == "/":
                second = stack.pop()
                first = stack.pop()
                
                stack.append(int(first / second))
            else:
                stack.append(int(item))

        return stack[0]
            