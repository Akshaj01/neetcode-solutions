class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        timeStack = []
        cars = sorted(zip(position, speed), reverse=True)

        for pos, spd in cars:
            time = (target - pos) / spd
            #if not first time and time < top of timestack
            if timeStack and time <= timeStack[-1]:
                continue
            timeStack.append(time)
        
        return len(timeStack)
            
        

    