class Solution:
    """
    temperatures = [30,38,30,36,35,40,28]
    result = [1,4,1,2,1,0,0]
    stack = [5,6]
    i =  6
    prev_day = 1
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_day = stack.pop()
                result[prev_day] = i - prev_day

            stack.append(i) 
        
        return result