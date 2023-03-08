class CoffeeShop:

    def __init__(self, name, till, Drinks, all_drinks): 
        self.name = name
        self.till = till
        self.drink = Drinks
        self.all_drinks = all_drinks

    def increase_till(self, amount):
        self.till += amount
    
    def check_age(self, customer):
        print(customer.__dict__)
        if customer.age >= 16:
            return True
        else:
            return False

    def check_energy(self, customer):
        if customer.energy_level >= 5:
            return True
        else:
            return False
        
    def sell_food(self, customer, food):
        if customer.wallet >= food.price:
            customer.wallet -= food.price
            self.till += food.price
            customer.decrease_energy_level(food)

    def get_drink_names(self, drink):
        self.all_drinks = []
        available_drinks = []
        for drink in self.all_drinks:
            if drink.availability == True:
                available_drinks.append(drink)
                print(available_drinks)

    def drinks_customer_can_afford(self, drink, customer):
        self.all_drinks = []
        affordable_drinks = []
        for drink in self.all_drinks:
            if drink.price <= customer.wallet:
                affordable_drinks.append(drink)
