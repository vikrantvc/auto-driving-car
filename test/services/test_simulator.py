from src.services.simulator import Simulator
from src.models.car import Car
from src.utils.directions import Direction

class TestSimulator:

    def test_add_car(self):
        simulator = Simulator(10, 10)
        car = Car("Ferrari", 5, 4, Direction.NORTH, "FFLFR")
        simulator.add_car(car)

        assert len(simulator.cars) == 1
        assert simulator.cars[0] == car

    def test_run_simulation(self):    
        simulator = Simulator(10, 10)
        car = Car("Ferrari", 5, 4, Direction.NORTH, "FFLFR")
        simulator.add_car(car)
        
        simulator.run_simulation()

        assert simulator.cars[0].name == "Ferrari"
        assert simulator.cars[0].x == 4
        assert simulator.cars[0].y == 6
        assert simulator.cars[0].direction == Direction.NORTH
        assert simulator.cars[0].commands == "FFLFR"