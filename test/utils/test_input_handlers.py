import pytest
from io import StringIO
import sys
from src.utils.input_handlers import *

@pytest.fixture
def capture_stdout(monkeypatch):
    captured_output = StringIO()
    monkeypatch.setattr(sys.stdout, 'write', captured_output.write)
    return captured_output

def test_get_field_dimensions_valid_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "10 20")
    result = get_field_dimensions()
    assert result == (10, 20)  # Note: The function should return (width, height)

def test_get_field_dimensions_invalid_input(monkeypatch, capture_stdout):
    inputs = iter(["invalid", "0 5", "-1 10", "10 20"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    result = get_field_dimensions()
    assert result == (10, 20)
    
    captured = capture_stdout.getvalue()
    assert "Invalid values. Please enter two positive integers separated by space." in captured
    assert captured.count("Invalid values.") == 3

def test_get_choice_valid_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "1")
    result = get_main_choice()
    assert result == 1

def test_get_choice_invalid_input(monkeypatch, capture_stdout):
    inputs = iter(["invalid", "3", "2"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    result = get_main_choice()
    assert result == 2

    captured = capture_stdout.getvalue()
    assert "Invalid choice. Please enter 1 or 2." in captured
    assert captured.count("Invalid choice.") == 2

def test_get_car_name_valid_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Jaguar")
    result = get_car_name()
    assert result == "Jaguar"

def test_get_car_name_invalid_input(monkeypatch, capture_stdout):
    inputs = iter(["", "Jaguar"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    result = get_car_name()
    assert result == "Jaguar"

    captured = capture_stdout.getvalue()
    assert "Name cannot be empty." in captured
    assert captured.count("Name cannot be empty.") == 1

def test_get_initial_position_valid_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "3 4 e")
    x, y, direction = get_initial_position("Jaguar", 10, 10)
    assert x == 3
    assert y == 4
    assert direction == "E"

def test_get_car_name_invalid_input(monkeypatch, capture_stdout):
    inputs = iter(["invalid", "-1 2 N", "2 -4 S", "3 5 X", "11 2 N", "3 23 N", "3 4 n"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    x, y, direction = get_initial_position("Jaguar", 10, 10)
    assert x == 3
    assert y == 4
    assert direction == "N"

    captured = capture_stdout.getvalue()
    assert "Invalid input. Please use format: x y Direction (N/S/W/E)" in captured
    assert captured.count("Invalid input.") == 6

def test_get_commands_valid_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "LRFRRFFL")
    commands = get_commands("Jaguar")
    assert commands == "LRFRRFFL"

def test_get_commands_invalid_input(monkeypatch, capture_stdout):
    inputs = iter(["Invalid", " ", "LYR", "LRFRRFFL"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    commands = get_commands("Jaguar")
    assert commands == "LRFRRFFL"

    captured = capture_stdout.getvalue()
    assert "Invalid commands. Only L, R, F are allowed." in captured
    assert captured.count("Invalid commands.") == 3

def test_add_car_flow_valid_input(monkeypatch):
    monkeypatch.setattr('src.utils.input_handlers.get_car_name', lambda : "Jaguar")
    monkeypatch.setattr('src.utils.input_handlers.get_initial_position', lambda *args: (2, 3, Direction.NORTH))
    monkeypatch.setattr('src.utils.input_handlers.get_commands', lambda *args: "LRFRRFFL")

    result = add_car_flow(10, 10)
    assert result.name == "Jaguar"
    assert result.x == 2
    assert result.y == 3
    assert result.direction == Direction.NORTH
    assert result.commands == "LRFRRFFL"

def test_print_before_simulation(capture_stdout):
    ferrari = Car("Ferrari", 5, 4, Direction.NORTH, "FFLFR")
    jaguar = Car("Jaguar", 2, 3, Direction.EAST, "RFFLR")
    cars = [ferrari, jaguar]

    print_before_simulation(cars)

    captured = capture_stdout.getvalue()
    assert "Your current list of cars are:" in captured
    assert "- Ferrari, (5,4) N, FFLFR" in captured
    assert "- Jaguar, (2,3) E, RFFLR" in captured


def test_print_after_simulation(capture_stdout):
    ferrari = Car("Ferrari", 5, 5, Direction.NORTH, "FFLFR")
    jaguar = Car("Jaguar", 5, 5, Direction.SOUTH, "FFLR")
    cars = [ferrari, jaguar]
    ferrari.active = False
    ferrari.steps_taken = 1
    jaguar.active = False
    jaguar.steps_taken = 1

    print_after_simulation(cars)

    captured = capture_stdout.getvalue()
    assert "After simulation, the result is:" in captured
    assert "- Ferrari, collides with Jaguar at (5,5) at step 1" in captured
    assert "- Jaguar, collides with Ferrari at (5,5) at step 1" in captured

@pytest.mark.parametrize("choice, result",[
    ("1", False),
    ("2", True)
])
def test_get_termination_choice_valid_input(monkeypatch, choice, result):
    monkeypatch.setattr('builtins.input', lambda _: choice)
    actual = get_termination_choice()
    assert actual == result

def test_get_termination_choice_invalid_input(monkeypatch, capture_stdout):
    inputs = iter(["invalid", "3", "2"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    result = get_termination_choice()
    assert result == True

    captured = capture_stdout.getvalue()
    assert "Invalid choice. Please enter 1 or 2." in captured
    assert captured.count("Invalid choice.") == 2
