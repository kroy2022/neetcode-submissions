class Solution:
    """
    target = 10, position = [6,8], speed = [3,2]
    pair = [(8,2), (6,3)]
    fleets = 1
    prevTime = 1
    i = 1
    currCar = (6,3)
    currTime = 1

    4->6->8->10
    1->4->7->10
    """
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        fleets = 1
        prevTime = (target - pair[0][0]) / pair[0][1]
        for i in range(1, len(position)):
            currCar = pair[i]
            currTime = (target - pair[i][0]) / pair[i][1]

            if currTime > prevTime:
                fleets += 1
                prevTime = currTime
        
        return fleets


            






