import random
from datetime import datetime, timedelta
from Event import Event
from Visitor import Visitor
from Employee import Employee
from Museum import Museum
from Artwork import Artwork
from Ticket import Ticket
from Location import Location
from Ticket import VisitorCategory

def create_visitor():
    try:
        # Prompt user to enter their name
        name = input("Please enter your name: ")
        # Check if the name is empty
        if not name:
            print("Name cannot be empty. Please try again.")
            # Prompt user again to enter their name
            name = input("Please enter your name: ")
            # Check if the name is still empty
            if not name:
                print("Invalid input. Exiting.")
                return None

        try:
            # Prompt user to enter their age
            age = int(input("Please enter your age: "))
            # Check if the age is within a valid range
            if age < 0 or age > 120:
                raise ValueError
        except ValueError:
            print("Invalid age. Age must be between 0 and 120. Please try again.")
            try:
                # Prompt user again to enter their age
                age = int(input("Please enter your age: "))
                # Check if the age is within a valid range
                if age < 0 or age > 120:
                    raise ValueError
            except ValueError:
                print("Invalid input. Exiting.")
                return None


        # Prompt user to enter their national ID
        national_id = input("Please enter your national ID: ")
        # Check if the national ID has the correct format
        if len(national_id) != 9 or not national_id.isdigit():
            print("National ID must be 9 digits. Please try again.")
            # Prompt user again to enter their national ID
            national_id = input("Please enter your national ID: ")
            # Check if the national ID has the correct format
            if len(national_id) != 9 or not national_id.isdigit():
                print("Invalid input. Exiting.")
                return None

        # Return a Visitor object with the provided information
        visitor = Visitor(name, age, national_id)  # Assuming Visitor instantiation is correct.

        # Add this line to print the visitor details
        print(f"\nVisitor Created: Name: {name}, Age: {age}, National ID: {national_id}")

        return visitor
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def create_employee():
    try:
        # Prompt employee to enter their name
        name = input("\nPlease enter your name: ")
        # Check if the name is empty
        if not name:
            print("Name cannot be empty. Please try again.")
            # Prompt employee again to enter their name
            name = input("Please enter your name: ")
            # Check if the name is still empty
            if not name:
                print("Invalid input. Exiting.")
                return None

        try:
            # Prompt employee to enter their age
            age = int(input("Please enter your age: "))
            # Check if the age is within a valid range
            if age < 0 or age > 120:
                raise ValueError
        except ValueError:
            print("Invalid age. Age must be between 0 and 120. Please try again.")
            try:
                # Prompt employee again to enter their age
                age = int(input("Please enter your age: "))
                # Check if the age is within a valid range
                if age < 0 or age > 120:
                    raise ValueError
            except ValueError:
                print("Invalid input. Exiting.")
                return None

        # Prompt employee to enter their national ID
        national_id = input("Please enter your national ID: ")
        # Check if the national ID has the correct format
        if len(national_id) != 9 or not national_id.isdigit():
            print("National ID must be 9 digits. Please try again.")
            # Prompt employee again to enter their national ID
            national_id = input("Please enter your national ID: ")
            # Check if the national ID has the correct format
            if len(national_id) != 9 or not national_id.isdigit():
                print("Invalid input. Exiting.")
                return None

        # Prompt employee to enter their employee ID
        employee_id = input("Please enter your employee ID: ")
        # Check if the employee ID is empty
        if not employee_id:
            print("Employee ID cannot be empty. Please try again.")
            # Prompt employee again to enter their employee ID
            employee_id = input("Please enter your employee ID: ")
            # Check if the employee ID is still empty
            if not employee_id:
                print("Invalid input. Exiting.")
                return None

        employee = Employee(name, age, national_id, employee_id)  # Assuming Employee instantiation is correct.

        # Add this line to print the employee details
        print(f"\nEmployee Created: Name: {name}, Age: {age}, National ID: {national_id}, Employee ID: {employee_id}")

        return employee
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def create_artwork():
    try:
        # Prompt user to enter the artwork title
        title = input("\nEnter artwork title: ")
        # Prompt user to enter the artist's name
        artist = input("Enter artist name: ")
        # Prompt user to enter the year of creation
        year = input("Enter year of creation: ")

        # Create a new Artwork object with the collected information
        artwork = Artwork(title, artist, year)

        # Print statement confirming the addition of the artwork
        print(f"You added the artwork '{title}' by {artist}, created in {year}.")

        # Return the successfully created Artwork object
        return artwork
    except ValueError:
        # Inform the user of the error and prompt for correct input
        print("Invalid input. Please enter valid details for the artwork.")
        return None


def create_event():
    try:
        # Predefined list of potential event names
        event_names = ['Night at the Museum', 'Historical Treasures', 'Art & Wine Night', 'Ancient Civilizations',
                       'Modern Art Madness']
        # Convert Location enum to a list for random selection
        locations = list(Location)

        # Set the current time as the start date and add a random number of days to define the end date
        start_date = datetime.now()
        end_date = start_date + timedelta(days=random.randint(1, 5))

        # Randomly choose one of the predefined event names
        name = random.choice(event_names)
        # Randomly select a location for the event
        location = random.choice(locations)

        # Create and return the new Event object with the randomly selected details
        return Event(name, start_date, end_date, location)
    except ValueError:
        # Print error message if an issue is found
        print("Invalid input. Please enter valid details for the event.")
        return None


def purchase_tickets(selected_event, visitor):
    num_adults = int(input("How many adults are with you? "))
    num_kids = int(input("How many kids are with you? "))
    num_elders = int(input("How many elders are with you? "))
    num_students = int(input("How many students are with you? "))

    # Calculate ticket prices for each category
    adult_tickets = Ticket(selected_event, visitor.get_age(), num_adults, VisitorCategory.ADULT)
    kid_tickets = Ticket(selected_event, 12, num_kids, VisitorCategory.KID)  # Assuming age 12 for kids
    elder_tickets = Ticket(selected_event, 65, num_elders, VisitorCategory.ELDER)  # Assuming age 65 for elders
    student_tickets = Ticket(selected_event, visitor.get_age(), num_students, VisitorCategory.STUDENT)

    # Sum up the total price
    total_price = adult_tickets.get_price() + kid_tickets.get_price() + elder_tickets.get_price() + student_tickets.get_price()

    print(f"\nTotal price for the tickets is: {total_price:.2f} AED")
    print("Thank you for your purchase. Enjoy your visit and the wonders our museum has to offer!")




def run_test_case():
    try:
        museum = Museum("The Grand Museum") #Initializes
        print("Welcome to The Grand Museum Management System")

        # Prompt user to select visitor or employee
        user_type = input("Are you a visitor or an employee? (v/e): ").lower()

        if user_type == "v":  # Visitor selected
            visitor = create_visitor()  # Create a visitor object
            if visitor is None:
                return

            # Welcome message for the visitor
            print(f"\nWelcome, {visitor.get_name()}! What would you like to do today?")
            action = input("1: Purchase tickets\n2: Exit\nChoose an option: ")

            if action == "1":  # Purchase tickets selected
                # Create Event objects for the events
                events = [create_event() for _ in range(3)]
                print("\nHere are the upcoming events and their locations:")
                for i, event in enumerate(events, start=1):
                    print(f"{i}. {event.get_name()} - Location: {event.get_location().name}")

                event_choice = int(input("\nWhich event would you like to attend? Please enter the number: ")) - 1
                selected_event = events[event_choice]

                purchase_tickets(selected_event, visitor)  # Proceed to ticket purchase

            elif action == "2":  # Exit option selected
                print("\nThank you for visiting. Goodbye!")

        elif user_type == "e":  # Employee selected
            employee = create_employee()
            if employee is None:
                return

            # Welcome message for the employee
            print(f"\nWelcome, {employee.get_name()}!")
            while True:  # Keep asking for actions until user exits
                action = input(
                    "\n1: Add artwork to an exhibition\n2: Remove artwork from an exhibition\n3: Exit\nChoose an option: ")

                if action == "1":  # Add artwork to exhibition option selected
                    artwork = create_artwork()  # Creates the artwork and adds it
                    if artwork is not None:  # Check if artwork is not None
                        museum.add_artwork(artwork.get_title(), artwork.get_artist(), artwork.get_year())
                        print(f"\nArtwork '{artwork.get_title()}' by {artwork.get_artist()} added successfully.")
                        print(f"Historical Significance: {artwork.get_historical_significance()}")
                        print(f"Location: {artwork.get_location().name}")

                elif action == "2":  # Removes the artwork from exhibition
                    title = input("\nEnter the title of the artwork to remove: ")
                    museum.remove_artwork(title)
                    print(f"\nArtwork '{title}' removed successfully.")

                elif action == "3":  # Exit option selected
                    print("\nThank you for your service. Goodbye!")
                    break  # Exit the loop

                else:
                    print("\nInvalid option. Please try again.")

    except Exception as e:  # Catch any e
        # exceptions
        print(f"An error occurred: {str(e)}")

# Running the test case
run_test_case()
