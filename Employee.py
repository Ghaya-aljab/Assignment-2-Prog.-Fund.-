from Person import Person

class Employee(Person):
    ''' A class representing an employee at the museum, inheriting attributes from the Person class '''

    # Constructor method for initializing an Employee object with employee-specific attributes and inheritance from Person
    def __init__(self, name, age, national_id, employee_id):
        # inherits attributes from person class (the parent class)
        super().__init__(name, age, national_id)
        self._employee_id = employee_id

    # Setter and getter functions for employee attributes
    def get_employee_id(self):
        return self._employee_id

    def set_employee_id(self, employee_id):
        self._employee_id = employee_id
