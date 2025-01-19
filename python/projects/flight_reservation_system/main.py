# Add the project root directory to sys.path
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Task 2, 5, 9: Import modules here
from models.auth import CLIAuthenticator
from controllers.user_controller import UserController
from controllers.flight_controller import FlightController
from controllers.reservation_controller import ReservationController

# Task 2, 6, 10, 18: Redefine the main() function
def main():
    auth = CLIAuthenticator()  # Initialize authenticator
    user_controller = UserController()

    # Let the user log in
    while (user_controller.current_user==None):
        print("1. Login")
        print("2. Signup")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            user_controller.login()
        elif choice == "2":
            if (user_controller.signup()):
                if(user_controller.login()):
                    break

        elif choice == "3":
            return
        else:
            print("Invalid choice, try again.")

    # If login is successful, proceed with reservations
    if user_controller.current_user:
        flight_controller = FlightController()
        reservation_controller = ReservationController()

        while True:
            print("1. Search/Reserve Flights")
            print("2. View Reservations")
            print("3. Cancel Reservation")
            print("4. Add Flight (admin only)")
            print("5. Cancel Flight (admin only)")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                reservation_controller.search_flights(user_controller.current_user)
            elif choice == "2":
                reservation_controller.view_reservations(user_controller.current_user)
            elif choice == "3":
                reservation_controller.cancel_reservation(user_controller.current_user)
            elif choice == "4":
                flight_controller.add_flight(user_controller.current_user)
            elif choice == "5":
                flight_controller.cancel_flight(user_controller.current_user)
            elif choice == "6":
                break
            else:
                print("Invalid choice, try again.")
    return


if __name__ == "__main__":
    main()
