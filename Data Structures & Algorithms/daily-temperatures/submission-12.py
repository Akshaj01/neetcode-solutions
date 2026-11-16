class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        #monotonic stack of decreasing temps
        stack = []
        # for day
        for day in range(len(temperatures)):
            while stack and temperatures[day] > temperatures[stack[-1]]: 
                # while todays temp is greater than stack top
                results[stack[-1]] = day - stack[-1] #that day's result is diff
                stack.pop() #pop top stack

            stack.append(day) # add todays day to stack

        return results

                


        