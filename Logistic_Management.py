class Package:
    def __init__(self, package_id, destination, weight):
        self.package_id = package_id
        self.destination = destination
        self.weight = weight
        self.status = "pending"

    def deliver(self):
        self.status = "delivered"


class Vehicle:
    def __init__(self, vehicle_id, capacity):
        self.vehicle_id = vehicle_id
        self.capacity = capacity
        self.current_packages = []

    def load_package(self, package):
        total = sum(p.weight for p in self.current_packages) + package.weight
        if total <= self.capacity:
            self.current_packages.append(package)

    def deliver_packages(self):
        for p in self.current_packages:
            p.deliver()


class Truck(Vehicle):
    def __init__(self, vehicle_id):
        super().__init__(vehicle_id, 1000)

    def deliver_packages(self):
        super().deliver_packages()
        print(f"Truck {self.vehicle_id} delivered {len(self.current_packages)} packages.")


class Drone(Vehicle):
    def __init__(self, vehicle_id):
        super().__init__(vehicle_id, 10)

    def load_package(self, package):
        if package.weight <= 5:
            super().load_package(package)

    def deliver_packages(self):
        super().deliver_packages()
        print(f"Drone {self.vehicle_id} delivered {len(self.current_packages)} packages.")


class DeliverySystem:
    def assign_vehicle(self, vehicle, packages):
        for p in packages:
            vehicle.load_package(p)

    def dispatch(self, vehicles):
        for v in vehicles:
            yield v


p1 = Package("P101", "New York", 4)
p2 = Package("P102", "Boston", 7)
p3 = Package("P103", "Chicago", 3)
p4 = Package("P104", "LA", 2)
p5 = Package("P105", "Houston", 6)

truck = Truck("T1")
drone = Drone("D1")

system = DeliverySystem()
system.assign_vehicle(truck, [p1, p2, p3])
system.assign_vehicle(drone, [p4, p5])

for vehicle in system.dispatch([truck, drone]):
    vehicle.deliver_packages()

for p in [p1, p2, p3, p4, p5]:
    print(p.package_id, p.status)
