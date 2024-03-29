import random
from datetime import datetime, timedelta
from Event import Event
from Visitor import Visitor
from Employee import Employee
from Museum import Museum
from Artwork import Artwork
from Ticket import Ticket
from Location import Location


def create_visitor():
    try:
        name = input("Please enter your name: ")
        age = int(input("Please enter your age: "))
        if age < 0 or age > 120:  # Basic validation for age
            raise ValueError("Invalid age. Age must be between 0 and 120.")
        national_id = input("Please enter your national ID: ")
        if len(national_id) != 9 or not national_id.isdigit():  # Basic check for national ID format
            raise ValueError("Invalid national ID. Must be 9 digits.")
        visitor = Visitor(name, age, national_id)
        return visitor
    except ValueError as e:
        print(e)
        return None



def create_employee():
    try:
        name = input("\nPlease enter your name: ")
        age = int(input("Please enter your age: "))
        if age < 0 or age > 120:  # Basic validation for age
            raise ValueError("Invalid age. Age must be between 0 and 120.")
        national_id = input("Please enter your national ID: ")
        if len(national_id) != 9 or not national_id.isdigit():  # Basic check for national ID format
            raise ValueError("Invalid national ID. Must be 9 digits.")
        employee_id = input("Please enter your employee ID: ")
        employee = Employee(name, age, national_id, employee_id)
        return employee
    except ValueError as e:
        print(e)
        return None



def create_artwork():
    try:
        title = input("\nEnter artwork title: ")
        artist = input("Enter artist name: ")
        year = input("Enter year of creation: ")
        artwork = Artwork(title, artist, year)  # Now passing three arguments
        return artwork
    except ValueError:
        print("Invalid input. Please enter valid details for the artwork.")
        return None


def create_event():
    try:
        event_names = ['Night at the Museum', 'Historical Treasures', 'Art & Wine Night', 'Ancient Civilizations',
                       'Modern Art Madness']
        locations = list(Location)
        start_date = datetime.now()
        end_date = start_date + timedelta(days=random.randint(1, 5))
        name = random.choice(event_names)
        location = random.choice(locations)
        is_tour = random.choice([True, False])
        guide_name = 'John Doe' if is_tour else None
        group_size = random.randint(15, 40) if is_tour else None

        return Event(name, start_date, end_date, location, is_tour, guide_name, group_size)
    except ValueError:
        print("Invalid input. Please enter valid details for the event.")
        return None

def purchase_tickets(selected_event, visitor):
    num_adults = int(input("How many adults are with you? "))
    num_kids = int(input("How many kids are with you? "))
    num_elders = int(input("How many elders are with you? "))

    # Creating and calculating ticket price
    total_price = 0
    total_price += Ticket(selected_event, visitor.get_age(), num_adults).get_price()
    total_price += Ticket(selected_event, 12, num_kids).get_price()  # Assuming age 12 for kids
    total_price += Ticket(selected_event, 65, num_elders).get_price()  # Assuming age 65 for elders

    print(f"\nTotal price for the tickets is: {total_price:.2f} AED")
    print("Thank you for your purchase. Enjoy your visit and the wonders our museum has to offer!")


def run_test_case():
    try:
        museum = Museum("The Grand Museum")
        print("Welcome to The Grand Museum Management System")

        user_type = input("Are you a visitor or an employee? (v/e): ").lower()

        if user_type == "v":
            visitor = create_visitor()
            if visitor is None:
                return

            print(f"\nWelcome, {visitor.get_name()}! What would you like to do today?")
            action = input("1: Purchase tickets\n2: Exit\nChoose an option: ")

            if action == "1":
                # Create Event objects for the events
                events = [create_event() for _ in range(3)]
                print("\nHere are the upcoming events and their locations:")
                for i, event in enumerate(events, start=1):
                    print(f"{i}. {event.get_name()} - Location: {event.get_location().name}")

                event_choice = int(input("\nWhich event would you like to attend? Please enter the number: ")) - 1
                selected_event = events[event_choice]

                purchase_tickets(selected_event, visitor)

            elif action == "2":
                print("\nThank you for visiting. Goodbye!")

        elif user_type == "e":
            employee = create_employee()
            if employee is None:
                return

            print(f"\nWelcome, {employee.get_name()}!")
            while True:  # Keep asking for actions
                action = input(
                    "\n1: Add artwork to an exhibition\n2: Remove artwork from an exhibition\n3: Exit\nChoose an option: ")

                if action == "1":
                    artwork = create_artwork()
                    if artwork is not None:  # Check if artwork is not None
                        museum.add_artwork(artwork.get_title(), artwork.get_artist(), artwork.get_year())
                        print(f"\nArtwork '{artwork.get_title()}' by {artwork.get_artist()} added successfully.")
                        print(f"Historical Significance: {artwork.get_historical_significance()}")
                        print(f"Location: {artwork.get_location().name}")


                elif action == "2":
                    title = input("\nEnter the title of the artwork to remove: ")
                    museum.remove_artwork(title)
                    print(f"\nArtwork '{title}' removed successfully.")

                elif action == "3":
                    print("\nThank you for your service. Goodbye!")
                    break  # Exit the loop

                else:
                    print("\nInvalid option. Please try again.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

#Running the test case
run_test_case()
