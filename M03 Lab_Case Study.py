"""
Author: Brittany Fox
Date Written: 9/6/2024
Program: M03 Lab_CaseStudy.py

This Python program creates a super class called Vehicle containing the attribute for vehicle type. A second class
called Automobile is created which inherits the attributes from Vehicle and also contains its own attributes:
    (year, make, model, doors , and roof)

The program then accepts user input for the vehicle type and other attributes and stores that data which
is then output in an easy-to-read and understandable format.
"""


#Define the vehicle class with attribute of vehicle_type
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type  #Constructor will takes the vehicle_type as a parameter

#Define the automobile class that inherits from the vehicle class

class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):     #Create additional attributes
        super().__init__("car")
        self.year = year
        self.make = make                    #Constructor will takes the year, make, model, doors, and roof as parameters
        self.model = model                  #Then call the parent class's constructor with its attribute of vehicle_type
        self.doors = doors
        self.roof = roof
        
        
 #Define the main function by asking and accepting
 #User input for each attribute and store that input into the attributes created:       
def main():      
    year = input("Enter the year: ")
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sun roof): ")

    # Create an Automobile object using the input from the user:
    car = Automobile(year, make, model, doors, roof)

    # Display the information provided by the user that was stored
    # in a readable format using (f)
    print("\nVehicle Information:")
    print(f"Vehicle type: {car.vehicle_type}")
    print(f"Year: {car.year}")
    print(f"Make: {car.make}")
    print(f"Model: {car.model}")
    print(f"Number of doors: {car.doors}")
    print(f"Type of roof: {car.roof}")

if __name__ == "__main__":
    main()
        
        