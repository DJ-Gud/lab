from lab4.people import Human, Fireman, Policeman
from lab4.road import Road
from lab4.vehicles import *


if __name__ == '__main__':
    prospekt_pobedy = Road()

    car = Car[Human]()
    taxi = Taxi[Human]()
    undercover_taxi = Taxi[Policeman]()
    bus = Bus[Human]()

    police_car = PoliceCar[Policeman]()
    fire_truck = FireTruck[Fireman]()

    dimon = Human()
    taxi.place_passenger(dimon)

    prospekt_pobedy.add_car_to_road(taxi)
    prospekt_pobedy.add_car_to_road(bus)
    prospekt_pobedy.add_car_to_road(police_car)

    print(f'Passengers on the road: {prospekt_pobedy.humans_count}')
    print('Dimon is God\'s lonely man...')
