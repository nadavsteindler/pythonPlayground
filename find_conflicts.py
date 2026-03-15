from datetime import datetime, time
from typing import List
from enum import Enum


class FlightType(Enum):
    ARRIVAL=1
    DEPARTURE=2

class Flight:
    def __init__(self,number,time,event):
        self.number=number
        self.time=time
        self.event=event

class Conflict:
    def __init__(self,count,start):
        self.count=count
        self.start=start

    def __repr__(self):
        return f"Conflict({self.count}, {self.start})"

# flight is ordered list of fights
def find_conflicts(flights: List[Flight], capacity: int)->List[Conflict]:
    occupancy=0
    conflicts=[]
    for f in flights:
        if f.event == FlightType.ARRIVAL:
            occupancy+=1
        elif f.event== FlightType.DEPARTURE:
            occupancy-=1

        if occupancy>capacity:
            c = Conflict(occupancy, f.time)
            conflicts.append(c)
    return conflicts

if __name__ == "__main__":
    flights= [Flight(1, time(14, 30, 0), FlightType.ARRIVAL),
              Flight(2, time(14, 40, 0), FlightType.ARRIVAL),
              Flight(3, time(14, 50, 0), FlightType.ARRIVAL),
              Flight(4, time(15, 00, 0) , FlightType.ARRIVAL),
              Flight(2, time(15, 30, 0), FlightType.DEPARTURE),
              Flight(1, time(16, 00, 0), FlightType.DEPARTURE),
              Flight(5, time(16, 00, 0), FlightType.ARRIVAL)]
    print(find_conflicts(flights,3))

