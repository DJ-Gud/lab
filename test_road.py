import pytest

from lab4.people import Human
from lab4.road import Road
from lab4.vehicles import *


def test_add_cars():
    road = Road()

    road.add_car_to_road(Car[Human]())
    road.add_car_to_road(Bus[Human]())

    with pytest.raises(Exception):
        road.add_car_to_road(Human())


def test_humans_count():
    road = Road()
    assert road.humans_count == 0

    bus = Bus[Human]()
    for _ in range(35):
        bus.place_passenger(Human())

    assert road.humans_count == 0

    road.add_car_to_road(bus)
    assert road.humans_count == 35

    taxi = Taxi[Human]()
    passenger = Human()
    taxi.place_passenger(passenger)
    road.add_car_to_road(taxi)
    assert road.humans_count == 36

    taxi.kick_passenger(passenger)
    assert road.humans_count == 35
