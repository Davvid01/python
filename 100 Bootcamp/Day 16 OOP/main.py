from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

money_machine.report()

coffee_maker.report()


while is_on:
    options = menu.get_items()
    choice = input(f"Wgat w+ ould toy like: {options} ")
    if choice == "off":
        is_on=False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        product = menu.find_drink(choice)
        #name = product.name
        #cost = product.cost
        #ingredients = product.ingredients
        #print(cost)
        resources_sufficient = coffee_maker.is_resource_sufficient(product)

    if resources_sufficient and money_machine.make_payment(product.cost):
        coffee_maker.make_coffee(product)
    is_on=False