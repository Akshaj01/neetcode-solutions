class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = []
        for day in range(len(temperatures)):
            while stack and temperatures[day] > temperatures[stack[-1]]: 
                results[stack[-1]] = day - stack[-1] 
                stack.pop() 
            stack.append(day) 

        return results

                


        