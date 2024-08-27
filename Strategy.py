from abc import ABC, abstractmethod

# Interfaz de Strategy
class FareStrategy(ABC):
    @abstractmethod
    def calculate_fare(self, distance):
        pass

# Estrategia concreta para la tarifa estándar
class StandardFareStrategy(FareStrategy):
    def calculate_fare(self, distance):
        return distance * 1.5

# Estrategia concreta para la tarifa premium
class PremiumFareStrategy(FareStrategy):
    def calculate_fare(self, distance):
        return distance * 3.0

# Estrategia concreta para la tarifa compartida
class SharedFareStrategy(FareStrategy):
    def calculate_fare(self, distance):
        return distance * 0.75

# Clase Ride (Viaje) que utiliza la estrategia
class Ride:
    def __init__(self, driver, passenger, origin, destination, distance, fare_strategy: FareStrategy):
        self.driver = driver
        self.passenger = passenger
        self.origin = origin
        self.destination = destination
        self.distance = distance
        self.fare_strategy = fare_strategy

    def calculate_fare(self):
        return self.fare_strategy.calculate_fare(self.distance)

    def get_ride_details(self):
        fare = self.calculate_fare()
        return f"Ride with {self.driver} for {self.passenger} from {self.origin} to {self.destination}. Fare: ${fare:.2f}"

# Ejemplo de uso:
# Crear viajes con diferentes estrategias de tarifa
ride1 = Ride("Carlos", "Ana", "Zona 1", "Zona 10", 10, StandardFareStrategy())
ride2 = Ride("Luis", "Juan", "Zona 1", "Zona 15", 15, PremiumFareStrategy())
ride3 = Ride("Pedro", "Marta", "Zona 3", "Zona 9", 5, SharedFareStrategy())

# Mostrar detalles de los viajes
print(ride1.get_ride_details())  # Viaje estándar
print(ride2.get_ride_details())  # Viaje premium
print(ride3.get_ride_details())  # Viaje compartido
