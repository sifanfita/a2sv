class Solution(object):
    def wateringPlants(self, plants, capacity):
        #Tracks the number of steps
        step = 0
        currCapacity = capacity
        for idx in range(len(plants)):
            step += 1
            currCapacity -= plants[idx]
            if idx <= (len(plants) -2) and currCapacity < plants[idx + 1]:
                step += 2 * (idx+1)
                currCapacity = capacity

        return step