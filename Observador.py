from abc import ABC, abstractmethod

# Interfaz de Observer (Observador)
class RideObserver(ABC):
    @abstractmethod
    def update(self, ride_status):
        pass

# Clase Subject (Sujeto) que se observa
class Ride:
    def __init__(self, driver, passenger, origin, destination):
        self.driver = driver
        self.passenger = passenger
        self.origin = origin
        self.destination = destination
        self.status = "pending"
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self.status)

    def start_ride(self):
        self.status = "in progress"
        self.notify_observers()

    def complete_ride(self):
        self.status = "completed"
        self.notify_observers()

    def cancel_ride(self):
        self.status = "cancelled"
        self.notify_observers()

# Implementaciones de Observer concretos
class Passenger(RideObserver):
    def __init__(self, name):
        self.name = name

    def update(self, ride_status):
        print(f"{self.name} notified: Ride is now {ride_status}")

class Driver(RideObserver):
    def __init__(self, name):
        self.name = name

    def update(self, ride_status):
        print(f"{self.name} notified: Ride is now {ride_status}")

# Ejemplo de uso:
driver = Driver("Carlos")
passenger = Passenger("Ana")

ride = Ride(driver, passenger, "Zona 1", "Zona 10")
ride.add_observer(driver)
ride.add_observer(passenger)

# Cambiar el estado del viaje
ride.start_ride()  # Notifica a ambos observadores que el viaje ha comenzado
ride.complete_ride()  # Notifica a ambos observadores que el viaje ha sido completado

# Cancelar un viaje y notificar a los observadores
ride.cancel_ride()  # Notifica a ambos observadores que el viaje ha sido cancelado
