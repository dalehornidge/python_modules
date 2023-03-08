class Customer:

    def __init__(self, name, wallet, age, energy_level):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.energy_level = energy_level

    def decrease_wallet(self, amount):
        self.wallet -= amount

    def increase_energy_level(self, drink):
        self.energy_level += drink.caffeine_level
    
    def decrease_energy_level(self, food):
        self.energy_level -= food.rejuvinate 

    def buy_drink(self, drink, coffee_shop):
        if (self.wallet >= drink.price) and (self.age >= 16) and (self.energy_level <= 5):
           self.wallet -= drink.price
           coffee_shop.till += drink.price
           self.increase_energy_level(drink)
        else:
            print("No coffee for you! Get out of my shop!")

   