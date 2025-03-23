from src.models.car import Car
from src.utils.directions import Direction

def get_field_dimensions():
    while True:
        try:
            width, height  = input("Please enter the width and height of the simulation field in x y format:").split()
            width, height = map(int,(width, height))
            if height <= 0 or width <= 0:
                raise ValueError
            return width, height
        except Exception as e:
            print("Invalid values. Please enter two positive integers separated by space.")


def get_main_choice():
    while True:
        try:
            choice = int(input("Please choose from the following options:\n1. Add a car to field\n2. Run simulation\n"))
            if choice not in (1,2):
                raise ValueError
            return choice
        except Exception as e:
            print("Invalid choice. Please enter 1 or 2.")


def add_car_flow(width, height):
    name = get_car_name()
    x, y, direction = get_initial_position(name, width, height)
    commands = get_commands(name)
    return Car(name, x, y, Direction(direction), commands)


def get_car_name():
    while True:
        name = input("\nPlease enter the name of the car:\n").strip()
        if not name:
            print("Name cannot be empty.")
            continue
        return name


def get_initial_position(name, max_x, max_y):
    while True:
        try:
            values = input(
                f"Please enter initial position of car {name} in x y Direction format:\n"
            ).upper().split()
            if len(values) != 3:
                raise ValueError
            x, y, direction = int(values[0]), int(values[1]), values[2]
            if direction not in {'N', 'S', 'W', 'E'}:
                raise ValueError
            if not (0 <= x < max_x and 0 <= y < max_y):
                raise ValueError
            return x, y, direction
        except (ValueError, IndexError):
            print("Invalid input. Please use format: x y Direction (N/S/W/E)")


def get_commands(name):
    while True:
        commands = input(f"Please enter the commands for car {name}:\n").upper()
        if all(c in {'L', 'R', 'F'} for c in commands):
            return commands
        print("Invalid commands. Only L, R, F are allowed.")

def run(car: Car, width: str, height: str):
    print("Your current list of cars are:")
    print(f"- {car.name}, ({car.x},{car.y}) {car.direction}, {car.commands}")

    for command in car.commands:
        if command == 'L':
            car.rotate_left()
        elif command == 'R':
            car.rotate_right()
        elif command == 'F':
            car.move_forward(width, height)

    print("After simulation, the result is:")
    print(f"- {car.name}, ({car.x},{car.y}) {car.direction}")
