class UndergroundSystem:

    def __init__(self):
        self.check_ins = {}  # {id: (station, time)}
        self.travel_times = {}  # {(startStation, endStation): [travel_times]}


    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, checkInTime = self.check_ins[id]
        endStation = stationName
        travel_time = t - checkInTime

        if (startStation, endStation) not in self.travel_times:
            self.travel_times[(startStation, endStation)] = []

        self.travel_times[(startStation, endStation)].append(travel_time)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        travel_times = self.travel_times[(startStation, endStation)]
        average_time = sum(travel_times) / len(travel_times)
        return average_time

        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)