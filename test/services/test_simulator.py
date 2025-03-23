from unittest.mock import MagicMock
from src.services.simulator import Simulator
from src.models.car import Car
from src.utils.directions import Direction

class TestSimulator:
    
    def test_add_car(self):
        simulator = Simulator(10, 10)
        ferrari = Car("Ferrari", 5, 4, Direction.NORTH, "FFLFR")
        
        simulator.add_car(ferrari)

        assert len(simulator.cars) == 1
        assert simulator.cars[0] == ferrari
        assert simulator.max_step == 5

    def test_add_multiple_cars(self):
        simulator = Simulator(10, 10)
        ferrari = Car("Ferrari", 5, 4, Direction.NORTH, "FFLFRR")
        jaguar = Car("jaguar", 2, 3, Direction.EAST, "FFR")

        simulator.add_car(ferrari)
        simulator.add_car(jaguar)

        assert len(simulator.cars) == 2
        assert simulator.max_step == 6


    def test_process_step(self):
        ferrari = Car("Ferrari", 5, 4, Direction.NORTH, "FFLFR")
        jaguar = Car("jaguar", 2, 3, Direction.EAST, "FFRFL")
        simulator = Simulator(10, 10)
        simulator.cars.append(ferrari)
        simulator.cars.append(jaguar)
        positions = simulator._process_step(0)

        assert len(positions) == 2
        assert (5, 5) in positions
        assert (3, 3) in positions

    def test_execute_command_rotate_left(self):
        simulator = Simulator(10, 10)
        car = Car("Ferrari", 5, 4, Direction.NORTH, "FFLFR")
        simulator.cars.append(car)
        car.rotate_left = MagicMock() 

        simulator._execute_command(car, 'L')

        car.rotate_left.assert_called_once()

    def test_execute_command_rotate_right(self):
        simulator = Simulator(10, 10)
        car = Car("Ferrari", 5, 4, Direction.NORTH, "FFLFR")
        simulator.cars.append(car)
        car.rotate_right = MagicMock() 

        simulator._execute_command(car, 'R')

        car.rotate_right.assert_called_once()

    def test_execute_command_move_forward(self):
        simulator = Simulator(10, 10)
        car = Car("Ferrari", 5, 4, Direction.NORTH, "FFLFR")
        simulator.cars.append(car)
        car.move_forward = MagicMock() 

        simulator._execute_command(car, 'F')

        car.move_forward.assert_called_once()

    def test_handle_collisions(self):
        ferrari = Car("Ferrari", 5, 4, Direction.NORTH, "FFLFR")
        jaguar = Car("jaguar", 4, 5, Direction.EAST, "FFLFR")
        simulator = Simulator(10, 10)
        simulator.cars.append(ferrari)
        simulator.cars.append(jaguar)
        positions = {(5, 5): [ferrari, jaguar]}

        simulator._handle_collisions(positions)
        
        assert not ferrari.active
        assert not jaguar.active

    def test_run_simulation_single_car(self, mocker):  
        mock_print_before_simulation = mocker.patch("src.services.simulator.print_before_simulation")
        mock_print_after_simulation = mocker.patch("src.services.simulator.print_after_simulation")
        simulator = Simulator(10, 10)
        car = Car("Ferrari", 5, 4, Direction.NORTH, "FFLFR")
        simulator.add_car(car)
        
        simulator.run_simulation()

        mock_print_before_simulation.assert_called_once()
        mock_print_after_simulation.assert_called_once()
        assert simulator.cars[0].name == "Ferrari"
        assert simulator.cars[0].x == 4
        assert simulator.cars[0].y == 6
        assert simulator.cars[0].direction == Direction.NORTH
        assert simulator.cars[0].commands == "FFLFR"
        assert simulator.cars[0].active == True
        assert simulator.cars[0].steps_taken == 5
        
    def test_run_simulation_no_collision(self, mocker):
        mock_print_before_simulation = mocker.patch("src.services.simulator.print_before_simulation")
        mock_print_after_simulation = mocker.patch("src.services.simulator.print_after_simulation")
        ferrari = Car("Ferrari", 1, 1, Direction.NORTH, "FFLFR")
        jaguar = Car("jaguar", 4, 5, Direction.EAST, "FFLFR")
        simulator = Simulator(10, 10)
        simulator.add_car(ferrari)
        simulator.add_car(jaguar)
        
        simulator.run_simulation()

        assert simulator.cars[0].x == 0 and simulator.cars[0].y == 3
        assert simulator.cars[1].x == 6 and simulator.cars[1].y== 6
        assert simulator.cars[0].active and simulator.cars[1].active
        mock_print_before_simulation.assert_called_once()
        mock_print_after_simulation.assert_called_once()

    def test_run_simulation_with_collision(self, mocker):
        mock_print_before_simulation = mocker.patch("src.services.simulator.print_before_simulation")
        mock_print_after_simulation = mocker.patch("src.services.simulator.print_after_simulation")
        ferrari = Car("Ferrari", 5, 4, Direction.NORTH, "FFLFR")
        jaguar = Car("jaguar", 4, 5, Direction.EAST, "FFLFR")
        simulator = Simulator(10, 10)
        simulator.add_car(ferrari)
        simulator.add_car(jaguar)
        
        simulator.run_simulation()

        assert simulator.cars[0].x == 5 and simulator.cars[0].y == 5
        assert simulator.cars[1].x == 5 and simulator.cars[1].y== 5
        assert not simulator.cars[0].active and not simulator.cars[1].active
        mock_print_before_simulation.assert_called_once()
        mock_print_after_simulation.assert_called_once()
            
