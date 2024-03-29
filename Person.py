class Person:
    ''' A class representing a person '''

    def __init__(self, name, age, national_id):
        self._name = name
        self._age = age
        self._national_id = national_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def get_national_id(self):
        return self._national_id

    def set_national_id(self, national_id):
        self._national_id = national_id
