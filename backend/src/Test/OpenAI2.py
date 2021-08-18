from datetime import datetime


class person:
    def __init__(self, first_name, last_name, birthdate):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
    def calculate(self):
        return (self.birthdate - datetime.datetime.now()) / (365.25 * 8)