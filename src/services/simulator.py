from src.models.car import Car
from src.utils.input_handlers import print_before_simulation, print_after_simulation

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
        print_before_simulation(self.cars)

        for step in range(self.max_step):
            positions = self._process_step(step)
            self._handle_collisions(positions)

        print_after_simulation(self.cars)

    def _process_step(self, step: int) -> dict[tuple[int, int], list[Car]]:
        positions: dict[tuple[int, int], list[Car]] = {}
        active_cars = [car for car in self.cars if car.active]

        for car in active_cars:
            if step < len(car.commands):
                self._execute_command(car, car.commands[step])
                car.steps_taken += 1

                position = (car.x, car.y)
                if position in positions:
                    positions[position].append(car)
                else:
                    positions[position] = [car]

        return positions

    def _execute_command(self, car: Car, command: str):
        if command == 'L':
            car.rotate_left()
        elif command == 'R':
            car.rotate_right()
        elif command == 'F':
            car.move_forward(self.width - 1, self.height - 1)

    def _handle_collisions(self, positions: dict[tuple[int, int], list[Car]]):
        for cars in positions.values():
            if len(cars) > 1:
                for car in cars:
                    car.active = False
