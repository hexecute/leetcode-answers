class UndergroundSystem(object):

    def __init__(self):
        self.trip_times = {}
        self.NSA = {}
        
        

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.NSA[id] = (stationName, t)
        
        

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        # Identify trip that took place
        orig_stationName, orig_time = self.NSA[id]
        if self.trip_times.get((orig_stationName, stationName)):
            self.trip_times[(orig_stationName, stationName)].append(t - orig_time)
        else:
            self.trip_times[(orig_stationName, stationName)] = [t - orig_time]

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        target = self.trip_times.get((startStation, endStation), [0])
        rv = 0
        for trip_time in target:
            rv += trip_time
        return rv/float(len(target))


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)