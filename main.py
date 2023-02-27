

menu = {
 "espresso": {
     "ingredients": { "water": 50, "coffee": 18, } , "cost": 1.5, },
 "latte": {
        "ingredients": { "water":200, "coffee": 24, "milk":150, }, "cost":2.5, },
 "cappuccino": { "ingredients": { "water":250, "milk":100, "coffee":24, }, "cost": 3.0 ,}

}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100, }



def is_res_sufficient(order_ingredients):
    """return True if order is valid and false if ingredients are not enough"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """return the total calculated from inserting coins"""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns True if payment is accepted or False if insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that is not enough money. Money Refunded")
        return False



def make_coffee(drink_name, order_ingredients ):
    """deduct the ingredients from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy")




is_on = True

while is_on:
   choice = input("What would you like? (latte/cappuccino/espresso): ")
   if choice == "off":
        is_on = False
   elif choice == "report":
      print(f"water: {resources['water']}ml")
      print(f"milk: {resources['milk']}ml")
      print(f"coffee: {resources['coffee']}g")
      print(f"money: ${profit} ")

   else:
       drink = menu[choice]
       if is_res_sufficient(drink["ingredients"]):
           payment = process_coins()
           if is_transaction_successful(payment, drink["cost"]):
               make_coffee(choice, drink["ingredients"])


