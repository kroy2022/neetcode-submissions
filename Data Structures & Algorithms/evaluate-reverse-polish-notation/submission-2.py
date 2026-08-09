class Solution:
    """
    tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    stack = [17, 5]

    """
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+", "-", "*", "/"}
        for t in tokens:
            if t in operations:
                numTwo = int(stack.pop())
                numOne = int(stack.pop())

                if t == "+":
                    stack.append(numOne + numTwo)
                elif t == "-":
                    stack.append(numOne - numTwo)
                elif t == "*":
                    stack.append(numOne * numTwo)
                else:
                    stack.append(numOne / numTwo)
            else:
                stack.append(t)

        return int(stack[-1])
