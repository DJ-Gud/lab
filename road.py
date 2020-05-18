from typing import List

from lab4.vehicles import Vehicle


class Road:

    cars_in_road: List[Vehicle]

    def __init__(self) -> None:
        self.cars_in_road: List[Vehicle] = []

    def add_car_to_road(self, car: Vehicle) -> None:
        if not isinstance(car, Vehicle):
            raise Exception('Only vehicles can enter the road')
        self.cars_in_road.append(car)

    @property
    def humans_count(self) -> None:
        return sum(car.occupied_seats for car in self.cars_in_road)
