class Solution:
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        for pos, spd in cars:
            time = (target - pos)*1.0 / spd
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)


# or

class Solution(object):
    def carFleet(self, target, position, speed):
        map = {}
        for i in range(len(speed)):
            map[position[i]]=speed[i]
        s=sorted(map.keys(),reverse=True)
        fleet = 0
        prev = 0
        for x in s:
            time = float(target - x) / map[x]
            if time > prev:
                fleet += 1
                prev = time
        return fleet
