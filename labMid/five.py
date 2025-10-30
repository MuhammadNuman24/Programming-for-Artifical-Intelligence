class Person:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    def calculate_age(self, current_year=2025):
        return current_year - self.date_of_birth

name = input("Enter Your Name here = ")
dateofbirth = int(input("Enter your year of birth = "))
person = Person(name, dateofbirth)
print( "Your name is ",person.name , " and age is ",person.calculate_age() )
