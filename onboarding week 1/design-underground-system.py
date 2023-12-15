class UndergroundSystem:

    def __init__(self):
        self.my_dict={}
        self.outmap=defaultdict(list)
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.my_dict[id] = (stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.my_dict.pop(id)
        diff= t-startTime
        self.outmap[(startStation, stationName)].append(diff)

        #self.outmap[startStation, stationName][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total= sum(self.outmap[(startStation,endStation )])
        return total/len(self.outmap[(startStation,endStation )])
     


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)