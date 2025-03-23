from cli import add_car_flow, get_field_dimensions, get_main_choice

def main():
    print("Welcome to Auto Driving Car Simulation!")
    width, height = get_field_dimensions()

    while True:
        choice = get_main_choice()
        if choice == 1:        
            car_details = add_car_flow()
        elif choice == 2:
            pass
            break

if __name__ == "__main__":
    main()