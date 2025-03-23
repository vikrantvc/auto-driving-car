from src.utils.input_handlers import add_car_flow, get_field_dimensions, get_main_choice, print_before_simulation, get_termination_choice
from src.services.simulator import Simulator
# from src.utils.

def main():
    while True:
        print("Welcome to Auto Driving Car Simulation!")
        width, height = get_field_dimensions()
        simulator: Simulator = Simulator(width, height)
        
        while True:
            choice = get_main_choice()
            if choice == 1:        
                car = add_car_flow(width, height)
                simulator.add_car(car)
                print_before_simulation(simulator.cars)

            elif choice == 2:
                simulator.run_simulation()
                break
        
        termination_choice = get_termination_choice()
        if termination_choice:
            break

if __name__ == "__main__":
    main()