from src.utils.input_handlers import add_car_flow, get_field_dimensions, get_main_choice, run_simulation, print_car_list
from src.services.simulator import Simulator

def main():
    print("Welcome to Auto Driving Car Simulation!")
    width, height = get_field_dimensions()
    simulator: Simulator = Simulator(width, height)
    
    while True:
        choice = get_main_choice()
        if choice == 1:        
            car = add_car_flow(width, height)
            simulator.add_car(car)
            print_car_list(simulator.cars)

        elif choice == 2:
            simulator.run_simulation()
            break

if __name__ == "__main__":
    main()