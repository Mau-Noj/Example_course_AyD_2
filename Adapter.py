from abc import ABC, abstractmethod
# Servicio externo para calcular tarifas (no se puede modificar)
class ExternalFareCalculator:
    def __init__(self):
        pass

    def get_fare(self, distance, traffic_condition):
        # Calcula la tarifa basada en la distancia y las condiciones del tráfico
        if traffic_condition == "high":
            return distance * 2.5
        elif traffic_condition == "medium":
            return distance * 2.0
        else:
            return distance * 1.5

# Interfaz estándar que usa la aplicación para calcular tarifas
class Ride(ABC):
    def __init__(self, driver, passenger, origin, destination, distance):
        self.driver = driver
        self.passenger = passenger
        self.origin = origin
        self.destination = destination
        self.distance = distance

    @abstractmethod
    def calculate_fare(self):
        pass

# Implementación de Adapter para usar el servicio externo
class ExternalFareAdapter(Ride):
    def __init__(self, driver, passenger, origin, destination, distance, traffic_condition):
        super().__init__(driver, passenger, origin, destination, distance)
        self._external_fare_calculator = ExternalFareCalculator()
        self.traffic_condition = traffic_condition

    def calculate_fare(self):
        # Adaptamos el método `get_fare` del servicio externo para que funcione con la interfaz de Ride
        return self._external_fare_calculator.get_fare(self.distance, self.traffic_condition)

# Ejemplo de uso:
def book_ride(driver, passenger, origin, destination, distance, traffic_condition):
    ride = ExternalFareAdapter(driver, passenger, origin, destination, distance, traffic_condition)
    fare = ride.calculate_fare()
    print(f"Ride booked with {ride.driver} from {ride.origin} to {ride.destination}. Fare: ${fare}")

# Reservar un viaje usando el adaptador
book_ride("Carlos", "Ana", "Zona 1", "Zona 10", 10, "high")  # Output: Tarifa basada en el cálculo del servicio externo
book_ride("Luis", "Juan", "Zona 1", "Zona 15", 15, "medium")
