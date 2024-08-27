from collections.abc import Iterable, Iterator

# Clase Ride (Viaje)
class Ride:
    def __init__(self, ride_id, driver, passenger, origin, destination, status):
        self.ride_id = ride_id
        self.driver = driver
        self.passenger = passenger
        self.origin = origin
        self.destination = destination
        self.status = status

    def __str__(self):
        return f"Ride {self.ride_id}: {self.driver} driving {self.passenger} from {self.origin} to {self.destination}. Status: {self.status}"

# Iterador concreto
class RideIterator(Iterator):
    def __init__(self, rides):
        self._rides = rides
        self._index = 0

    def __next__(self):
        try:
            ride = self._rides[self._index]
        except IndexError:
            raise StopIteration()
        self._index += 1
        return ride

# Colección concreta que es iterable
class RideHistory(Iterable):
    def __init__(self):
        self._rides = []

    def add_ride(self, ride):
        self._rides.append(ride)

    def __iter__(self):
        return RideIterator(self._rides)

# Ejemplo de uso:
ride1 = Ride(1, "Carlos", "Ana", "Zona 1", "Zona 10", "completed")
ride2 = Ride(2, "Luis", "Juan", "Zona 4", "Zona 12", "completed")
ride3 = Ride(3, "Pedro", "Marta", "Zona 3", "Zona 9", "cancelled")

# Historial de viajes
ride_history = RideHistory()
ride_history.add_ride(ride1)
ride_history.add_ride(ride2)
ride_history.add_ride(ride3)

# Recorrer el historial de viajes
for ride in ride_history:
    print(ride)
