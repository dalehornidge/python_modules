# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(cc_pet_shop):
    return cc_pet_shop["name"]

def get_total_cash(cc_pet_shop):
    return cc_pet_shop["admin"]["total_cash"]

def add_or_remove_cash(cc_pet_shop, Any):
    original_amount = cc_pet_shop["admin"]["total_cash"]
    val_change = int(Any)
    add_money = original_amount + val_change
    sub_money = original_amount - val_change
    if val_change > 0:
              cc_pet_shop["admin"]["total_cash"] = add_money
    else:
         cc_pet_shop["admin"]["total_cash"] = add_money
 
def get_pets_sold(cc_pet_shop):
     return cc_pet_shop["admin"]["pets_sold"]

def increase_pets_sold(cc_pet_shop, Any):
    pets_sold = cc_pet_shop["admin"]["pets_sold"]
    increased = pets_sold + int(Any)
    if Any > 0:
         cc_pet_shop["admin"]["pets_sold"] = increased

def get_stock_count(cc_pet_shop):
     return len(cc_pet_shop["pets"])

def get_pets_by_breed(pet_shop, animal_breed):
    breeds_in_stock = []
    pets = pet_shop["pets"]
    for pet in pets:
        if pet["breed"] == animal_breed:
           breeds_in_stock.append(pet)
    return breeds_in_stock

def find_pet_by_name(pet_shop, name):
     for pet in pet_shop["pets"]:
          if pet["name"] == name:
               return pet

def remove_pet_by_name(pet_shop, name):
     for pet in pet_shop["pets"]:
        if pet["name"] == name:
             pet_shop["pets"].remove(pet)


def add_pet_to_stock(pet_shop, new_pet):
     pet_shop["pets"].append(new_pet)

def get_customer_cash(customers):
     return customers["cash"]
     
def remove_customer_cash(customer, amount):
     customer["cash"] -= amount

def get_customer_pet_count(customer):
     return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
     customer["pets"].append(new_pet)


def customer_can_afford_pet(customer, new_pet):
     new_pet_price = new_pet["price"]
     if new_pet_price <= customer["cash"]:
          return True
     else:
          return False

# to be completed mon morning
def sell_pet_customer(pet_shop, pet, customer):
    for pet in pet_shop:
         if customer["cash"] >= pet["price"]:
              customer["cash"].append(pet["price"])

         

    #  add 1 to customer pet count
    #  add 1 to pets sold
    #  take customer cash (same price as pet)
    #  add to total cash

