from src.models.car import Car
from src.utils.directions import Direction
import pytest

class TestCar:
    
    @pytest.mark.parametrize("initial_direction, expected_direction", [
        (Direction.EAST, Direction.NORTH),
        (Direction.NORTH, Direction.WEST),
        (Direction.WEST, Direction.SOUTH),
        (Direction.SOUTH, Direction.EAST)
    ])
    def test_rotate_left(self, initial_direction, expected_direction):
        car = Car(name="TestCar", x=0, y=0, direction=initial_direction, commands="")
        car.rotate_left()
        assert car.direction == expected_direction
        
    @pytest.mark.parametrize("initial_direction, expected_direction", [
        (Direction.NORTH, Direction.EAST),
        (Direction.EAST, Direction.SOUTH),
        (Direction.SOUTH, Direction.WEST),
        (Direction.WEST, Direction.NORTH)
    ])
    def test_rotate_right(self, initial_direction, expected_direction):
        car = Car(name="TestCar", x=0, y=0, direction=initial_direction, commands="")
        car.rotate_right()
        assert car.direction == expected_direction

    @pytest.mark.parametrize("initial_x, initial_y, direction, max_x, max_y, expected_x, expected_y", [
    (0, 0, Direction.EAST, 5, 5, 1, 0),  # Normal move
    (5, 0, Direction.EAST, 5, 5, 5, 0),  # At boundary
    
    (5, 0, Direction.WEST, 5, 5, 4, 0),  # Normal move
    (0, 0, Direction.WEST, 5, 5, 0, 0),  # At boundary
    
    (0, 0, Direction.NORTH, 5, 5, 0, 1),  # Normal move
    (0, 5, Direction.NORTH, 5, 5, 0, 5),  # At boundary
    
    (0, 5, Direction.SOUTH, 5, 5, 0, 4),  # Normal move
    (0, 0, Direction.SOUTH, 5, 5, 0, 0),  # At boundary
    ])
    def test_move_forward(self, initial_x, initial_y, direction, max_x, max_y, expected_x, expected_y):
        car = Car(name="TestCar", x=initial_x, y=initial_y, direction=direction, commands="")
        car.move_forward(max_x, max_y)
        assert car.x == expected_x
        assert car.y == expected_y