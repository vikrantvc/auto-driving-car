from src.models.car import Car
from src.utils.input_handlers import print_car_list

class Simulator:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.cars: list[Car] = []
        self.max_step = 0

    def add_car(self, car: Car):
        self.cars.append(car)
        self.max_step = max(self.max_step, len(car.commands))

    def run_simulation(self):
        print_car_list(self.cars)

        for step in range(self.max_step):
            for car in self.cars:
                if step >= len(car.commands):
                    continue

                command = car.commands[step]
                if command == 'L':
                    car.rotate_left()
                elif command == 'R':
                    car.rotate_right()
                elif command == 'F':
                    car.move_forward(self.width, self.height)

        print("After simulation, the result is:")
        
        for car in self.cars:
            print(f"- {car.name}, ({car.x},{car.y}) {car.direction}")


