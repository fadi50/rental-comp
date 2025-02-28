class Vehicle:
    def __init__(self, brand, model, year, rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.__rental_price_per_day = rental_price_per_day
#i have added a new method to the class Vehicle and it a private method it take the brand,model,year...etc
        