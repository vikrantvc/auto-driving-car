from src.cli import add_car_flow, get_field_dimensions, get_main_choice, run
from src.models.car import Car

def main():
    print("Welcome to Auto Driving Car Simulation!")
    width, height = get_field_dimensions()
    car: Car = None
    
    while True:
        choice = get_main_choice()
        if choice == 1:        
            car = add_car_flow(width, height)
        elif choice == 2:
            run(car, width, height)
            break


if __name__ == "__main__":
    main()