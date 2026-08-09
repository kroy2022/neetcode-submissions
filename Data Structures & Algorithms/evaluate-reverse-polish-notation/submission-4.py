class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop(-2) + stack.pop())
            elif token == "-":
                numTwo = stack.pop()
                numOne = stack.pop()
                stack.append(numOne - numTwo)
            elif token == "*":
                stack.append(stack.pop(-2) * stack.pop())
            elif token == "/":
                numTwo = stack.pop()
                numOne = stack.pop()
                stack.append(int(numOne / numTwo))
            else:
                stack.append(int(token))

        return stack[0]