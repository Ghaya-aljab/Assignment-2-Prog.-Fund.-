from Person import Person

class Employee(Person):
    ''' A class representing an employee at the museum, inheriting attributes from the Person class '''

    def __init__(self, name, age, national_id, employee_id):
        super().__init__(name, age, national_id)
        self._employee_id = employee_id

    def get_employee_id(self):
        return self._employee_id

    def set_employee_id(self, employee_id):  # Add employee_id as a parameter
        self._employee_id = employee_id
