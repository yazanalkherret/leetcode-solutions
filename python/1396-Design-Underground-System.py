class UndergroundSystem:

    def __init__(self):
        self.start_station_time = {}
        self.trip_times = defaultdict(int) 
        self.trip_count = defaultdict(int)

    def checkIn(self, id: int, start_station: str, t: int) -> None:
        self.start_station_time[id] = (start_station, t)

    def checkOut(self, id: int, end_station: str, t: int) -> None:
        start_station, start_time = self.start_station_time[id]

        self.trip_times[(start_station, end_station)] += t - start_time
        self.trip_count[(start_station, end_station)] += 1

        del self.start_station_time[id]
        
    def getAverageTime(self, start_station: str, end_station: str) -> float:
        return self.trip_times[(start_station, end_station)] / self.trip_count[(start_station, end_station)]
