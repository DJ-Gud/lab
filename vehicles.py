from typing import Generic, List, TypeVar

from lab4.people import Human, Fireman, Policeman

T = TypeVar('T')


class Vehicle(Generic[T]):
    
    total_seats: int
    passengers: List[T]

    def place_passenger(self, passenger: T) -> None:
        generic = self._get_generic_type()
        if not isinstance(passenger, generic):
            raise Exception('This vehicle is not intended for such passenger')
        if not self.free_seats:
            raise Exception('No free seats available')
        self.passengers.append(passenger)
        
    def kick_passenger(self, passenger: T) -> None:
        if passenger not in self.passengers:
            raise Exception('The passenger is not sitting in this vehicle')
        self.passengers.remove(passenger)

    @property
    def occupied_seats(self) -> int:
        return len(self.passengers)

    @property
    def free_seats(self) -> int:
        return self.total_seats - self.occupied_seats

    def _check_generic(self) -> None:
        generic = self._get_generic_type()
        if not issubclass(generic, Human):
            raise Exception('No dogs allowed')

    def _get_generic_type(self) -> object:
        try:
            return self.__orig_class__.__args__[0]
        except AttributeError:
            # better fallback handling?
            return object


class Bus(Vehicle, Generic[T]):
    
    def __init__(self) -> None:
        self._check_generic()
        self.total_seats: int = 50
        self.passengers: List[T] = []


class Car(Vehicle, Generic[T]):
    
    def __init__(self) -> None:
        self._check_generic()
        self.total_seats: int = 5
        self.passengers: List[T] = []


class Taxi(Car, Generic[T]):

    def __init__(self) -> None:
        self._check_generic()
        self.total_seats: int = 4
        self.passengers: List[T] = []


class PoliceCar(Car, Generic[T]):

    def __init__(self) -> None:
        self._check_generic()
        self.total_seats: int = 3
        self.passengers: List[T] = []

    def _check_generic(self) -> None:
        generic = self._get_generic_type()
        if generic is not Policeman:
            raise Exception('Only policemen allowed')


class FireTruck(Car, Generic[T]):

    def __init__(self) -> None:
        self._check_generic()
        self.total_seats: int = 2
        self.passengers: List[T]

    def _check_generic(self) -> None:
        generic = self._get_generic_type()
        if generic is not Fireman:
            raise Exception('Only firemen allowed')
