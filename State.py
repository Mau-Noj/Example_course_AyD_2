from abc import ABC, abstractmethod

# Clase de Estado
class RideState(ABC):
    @abstractmethod
    def handle(self, ride):
        pass

    @abstractmethod
    def __str__(self):
        pass

# Estado Concreto: Pendiente
class PendingState(RideState):
    def handle(self, ride):
        print("Starting the ride...")
        ride.state = InProgressState()

    def __str__(self):
        return "Pending"

# Estado Concreto: En Progreso
class InProgressState(RideState):
    def handle(self, ride):
        print("Completing the ride...")
        ride.state = CompletedState()

    def __str__(self):
        return "In Progress"

# Estado Concreto: Completado
class CompletedState(RideState):
    def handle(self, ride):
        print("The ride is already completed. No further action can be taken.")

    def __str__(self):
        return "Completed"

# Estado Concreto: Cancelado
class CancelledState(RideState):
    def handle(self, ride):
        print("The ride is cancelled. No further action can be taken.")

    def __str__(self):
        return "Cancelled"

# Contexto (Ride)
class Ride:
    def __init__(self, driver, passenger, origin, destination):
        self.driver = driver
        self.passenger = passenger
        self.origin = origin
        self.destination = destination
        self.state = PendingState()  # Estado inicial

    def request_action(self):
        self.state.handle(self)

    def cancel_ride(self):
        if not isinstance(self.state, CompletedState):
            print("Cancelling the ride...")
            self.state = CancelledState()
        else:
            print("Cannot cancel a completed ride.")

    def __str__(self):
        return f"Ride for {self.passenger} from {self.origin} to {self.destination}. Current status: {self.state}"

# Ejemplo de uso:
ride = Ride("Carlos", "Ana", "Zona 1", "Zona 10")

print(ride)  # Estado inicial (Pendiente)
ride.request_action()  # Cambia a "En Progreso"
print(ride)

ride.request_action()  # Cambia a "Completado"
print(ride)

ride.cancel_ride()  # Intento de cancelar un viaje completado (no permitido)
print(ride)
