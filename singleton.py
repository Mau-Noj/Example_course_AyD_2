class RideManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RideManager, cls).__new__(cls)
            cls._instance.active_rides = {}
        return cls._instance

    def create_ride(self, ride_id, driver, passenger, origin, destination):
        if ride_id not in self.active_rides:
            self.active_rides[ride_id] = {
                "driver": driver,
                "passenger": passenger,
                "origin": origin,
                "destination": destination,
                "status": "active"
            }

    def get_ride(self, ride_id):
        return self.active_rides.get(ride_id, None)

    def complete_ride(self, ride_id):
        if ride_id in self.active_rides:
            self.active_rides[ride_id]["status"] = "completed"

    def cancel_ride(self, ride_id):
        if ride_id in self.active_rides:
            self.active_rides[ride_id]["status"] = "cancelled"

    def get_active_rides(self):
        return {ride_id: ride for ride_id, ride in self.active_rides.items() if ride["status"] == "active"}

# Ejemplo de uso:
ride_manager1 = RideManager()
ride_manager2 = RideManager()

# Crear un nuevo viaje
ride_manager1.create_ride(ride_id=1, driver="Carlos", passenger="Ana", origin="Zona 1", destination="Zona 10")

# Obtener información del viaje
print(ride_manager2.get_ride(1))  # Output: {'driver': 'Carlos', 'passenger': 'Ana', 'origin': 'Zona 1', 'destination': 'Zona 10', 'status': 'active'}

# Completar el viaje
ride_manager1.complete_ride(1)
print(ride_manager2.get_ride(1))  # Output: {'driver': 'Carlos', 'passenger': 'Ana', 'origin': 'Zona 1', 'destination': 'Zona 10', 'status': 'completed'}

print(ride_manager1 is ride_manager2)  # Output: True, ya que ambos objetos son la misma instancia
