import pytest

from lab4.people import Human, Fireman, Policeman
from lab4.vehicles import *


def test_init_vehicles():
    Car[Human]()
    Car[Fireman]()
    Taxi[Policeman]()
    Bus[Human]()
    PoliceCar[Policeman]()
    FireTruck[Fireman]()

    with pytest.raises(Exception):
        PoliceCar[Fireman]()
        PoliceCar[Human]()
        FireTruck[Policeman]()
        FireTruck[Human]()


def test_place_passenger():
    taxi = Taxi[Human]()
    passenger = Policeman()
    taxi.place_passenger(passenger)
    
    bus = Bus[Human]()
    for _ in range(50):
        bus.place_passenger(Human())

    with pytest.raises(Exception):
        bus.place_passenger(Human())

        truck = FireTruck[Fireman]()
        truck.place_passenger(Human())
        truck.place_passenger(Policeman())


def test_kick_passenger():
    car = Car[Human]()
    passenger = Human()
    car.place_passenger(passenger)
    car.kick_passenger(passenger)

    with pytest.raises(Exception):
        car.kick_passenger(Human())


def test_properties():
    police_car = PoliceCar[Policeman]()
    assert police_car.free_seats == 3
    assert police_car.occupied_seats == 0

    police_car.place_passenger(Policeman())
    police_car.place_passenger(Policeman())
    assert police_car.free_seats == 1
    assert police_car.occupied_seats == 2
