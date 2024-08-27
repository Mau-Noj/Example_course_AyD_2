from abc import ABC, abstractmethod

# Interfaz de Command
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# Receptor (Receiver)
class Ride:
    def __init__(self, driver, passenger, origin, destination):
        self.driver = driver
        self.passenger = passenger
        self.origin = origin
        self.destination = destination
        self.status = "pending"

    def start_ride(self):
        self.status = "in progress"
        print(f"Ride started with {self.driver} for {self.passenger}. Status: {self.status}")

    def complete_ride(self):
        self.status = "completed"
        print(f"Ride completed with {self.driver} for {self.passenger}. Status: {self.status}")

    def cancel_ride(self):
        self.status = "cancelled"
        print(f"Ride cancelled with {self.driver} for {self.passenger}. Status: {self.status}")

# Comando concreto para iniciar un viaje
class StartRideCommand(Command):
    def __init__(self, ride):
        self.ride = ride

    def execute(self):
        self.ride.start_ride()

    def undo(self):
        self.ride.cancel_ride()

# Comando concreto para completar un viaje
class CompleteRideCommand(Command):
    def __init__(self, ride):
        self.ride = ride

    def execute(self):
        self.ride.complete_ride()

    def undo(self):
        print("Cannot undo the completion of a ride.")

# Comando concreto para cancelar un viaje
class CancelRideCommand(Command):
    def __init__(self, ride):
        self.ride = ride

    def execute(self):
        self.ride.cancel_ride()

    def undo(self):
        print("Cannot undo the cancellation of a ride.")

# Invocador (Invoker)
class RideInvoker:
    def __init__(self):
        self._history = []

    def execute_command(self, command: Command):
        command.execute()
        self._history.append(command)

    def undo_last_command(self):
        if self._history:
            last_command = self._history.pop()
            last_command.undo()
        else:
            print("No commands to undo.")

# Ejemplo de uso:
ride = Ride("Carlos", "Ana", "Zona 1", "Zona 10")

# Crear comandos
start_command = StartRideCommand(ride)
complete_command = CompleteRideCommand(ride)
cancel_command = CancelRideCommand(ride)

# Crear invocador
invoker = RideInvoker()

# Ejecutar comandos
invoker.execute_command(start_command)  # Inicia el viaje
invoker.undo_last_command()  # Deshacer la acción (cancelar el viaje)

invoker.execute_command(start_command)  # Iniciar de nuevo el viaje
invoker.execute_command(complete_command)  # Completar el viaje

# Intentar deshacer la finalización del viaje
invoker.undo_last_command()  # Intento de deshacer la finalización (no permitido)
