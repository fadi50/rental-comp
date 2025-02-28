class Vehicle:
    def __init__(self, brand, model, year, rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.__rental_price_per_day = rental_price_per_day
#i have added a new method to the class Vehicle and it a private method it take the brand,model,year...etc
    def display_info(self):
        print(f"{self.brand} {self.model}, Year: {self.year}, Rental Price: ${self.__rental_price_per_day}/day")
    #i defined display_info method to display the brand,model,year and rental price of the vehicle
    def calculate_rental_cost(self, days):
        return self.__rental_price_per_day * days    
    #i defined calculate_rental_cost method to calculate the rental cost of the vehicle by multiplying the rental price per day by the number of days
    def get_rental_price_per_day(self):
        return self.__rental_price_per_day
    #i defined get_rental_price_per_day method to get the rental price per day of the vehicle
    def set_rental_price_per_day(self, new_price):
        if new_price > 0:
            self.__rental_price_per_day = new_price
        else:
            print("Rental price must be positive.")
    #i defined set_rental_price_per_day method to set the rental price per day of the vehicle    
class Car(Vehicle):
    def __init__(self, brand, model, year, rental_price_per_day, seating_capacity):
        super().__init__(brand, model, year, rental_price_per_day)
        self.seating_capacity = seating_capacity
    #i have added a new method to the class Car and it takes the brand,model,year,rental price per day and seating capacity
    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}, Seats: {self.seating_capacity}, Rental Price: ${self.get_rental_price_per_day()}/day")
    #i defined display_info method to display the brand,model,year,seating capacity and rental price of the car 
class Bike(Vehicle):
    def __init__(self, brand, model, year, rental_price_per_day, engine_capacity):
        super().__init__(brand, model, year, rental_price_per_day)
        self.engine_capacity = engine_capacity
    
    def display_info(self):
        print(f"Bike: {self.brand} {self.model}, Year: {self.year}, Engine: {self.engine_capacity}cc, Rental Price: ${self.get_rental_price_per_day()}/day")

def show_vehicle_info(vehicle):
    vehicle.display_info()    