from datetime import time

from find_conflicts import Flight, FlightType, Conflict, find_conflicts


class TestFindConflicts:
    def test_no_conflicts_under_capacity(self):
        flights = [
            Flight(1, time(14, 0), FlightType.ARRIVAL),
            Flight(2, time(14, 30), FlightType.ARRIVAL),
        ]
        assert find_conflicts(flights, 3) == []

    def test_no_conflicts_at_capacity(self):
        flights = [
            Flight(1, time(14, 0), FlightType.ARRIVAL),
            Flight(2, time(14, 30), FlightType.ARRIVAL),
            Flight(3, time(15, 0), FlightType.ARRIVAL),
        ]
        assert find_conflicts(flights, 3) == []

    def test_single_conflict(self):
        flights = [
            Flight(1, time(14, 0), FlightType.ARRIVAL),
            Flight(2, time(14, 30), FlightType.ARRIVAL),
            Flight(3, time(15, 0), FlightType.ARRIVAL),
            Flight(4, time(15, 30), FlightType.ARRIVAL),
        ]
        result = find_conflicts(flights, 3)
        assert len(result) == 1
        assert result[0].count == 4
        assert result[0].start == time(15, 30)

    def test_multiple_conflicts(self):
        flights = [
            Flight(1, time(14, 0), FlightType.ARRIVAL),
            Flight(2, time(14, 30), FlightType.ARRIVAL),
            Flight(3, time(15, 0), FlightType.ARRIVAL),
            Flight(4, time(15, 30), FlightType.ARRIVAL),
            Flight(5, time(16, 0), FlightType.ARRIVAL),
        ]
        result = find_conflicts(flights, 3)
        assert len(result) == 2
        assert result[0].count == 4
        assert result[1].count == 5

    def test_departure_resolves_conflict(self):
        flights = [
            Flight(1, time(14, 0), FlightType.ARRIVAL),
            Flight(2, time(14, 30), FlightType.ARRIVAL),
            Flight(3, time(15, 0), FlightType.ARRIVAL),
            Flight(4, time(15, 30), FlightType.ARRIVAL),
            Flight(1, time(16, 0), FlightType.DEPARTURE),
            Flight(2, time(16, 30), FlightType.DEPARTURE),
            Flight(5, time(17, 0), FlightType.ARRIVAL),
        ]
        result = find_conflicts(flights, 3)
        assert len(result) == 1
        assert result[0].count == 4
        assert result[0].start == time(15, 30)

    def test_empty_flights(self):
        assert find_conflicts([], 3) == []

    def test_capacity_of_one(self):
        flights = [
            Flight(1, time(14, 0), FlightType.ARRIVAL),
            Flight(2, time(14, 30), FlightType.ARRIVAL),
        ]
        result = find_conflicts(flights, 1)
        assert len(result) == 1
        assert result[0].count == 2

    def test_all_departures(self):
        flights = [
            Flight(1, time(14, 0), FlightType.DEPARTURE),
            Flight(2, time(14, 30), FlightType.DEPARTURE),
        ]
        assert find_conflicts(flights, 3) == []

    def test_conflict_after_departure_and_arrivals(self):
        flights = [
            Flight(1, time(14, 0), FlightType.ARRIVAL),
            Flight(2, time(14, 30), FlightType.ARRIVAL),
            Flight(1, time(15, 0), FlightType.DEPARTURE),
            Flight(2, time(15, 30), FlightType.DEPARTURE),
            Flight(3, time(16, 0), FlightType.ARRIVAL),
            Flight(4, time(16, 30), FlightType.ARRIVAL),
            Flight(5, time(17, 0), FlightType.ARRIVAL),
            Flight(6, time(17, 30), FlightType.ARRIVAL),
        ]
        result = find_conflicts(flights, 3)
        assert len(result) == 1
        assert result[0].count == 4
        assert result[0].start == time(17, 30)
