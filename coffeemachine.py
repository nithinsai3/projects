menu = {
    "tea":{
        "ingredients":{
            "water":100,
            "milk":60,
            "powder":30,
        },
        "cost":20,
    },
    "coffee":{
        "ingredients":{
            "water":80,
            "milk":40,
            "powder":20,
        },
        "cost":25,
    },
    "milk":{
        "ingredients":{
            "water":100,
            "milk":100,
            "powder":10,
        },
        "cost":30,
    }
    }
profit =0
resources ={
    "water":200,
    "milk": 200,
    "powder":50,
}
def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print(f"sorry there is no enough {item} to deliver to you ")
            return False
        return True
def process_coin():
    print("please insert coins")
    total=0
    coins_five=int(input("how many five coins you have inserted? :"))
    coins_ten=int(input("how many ten coins you have inserted? :"))
    coins_twenty=int(input("how many twenty coins you have inserted? :"))
    total=coins_five*5+coins_ten*10+coins_twenty*20
    return total

def is_payment_successful(money_received,drink_cost):
    if money_received>=drink_cost:
        global profit
        profit=profit+drink_cost
        change=money_received-drink_cost
        print(f"here is your {change} ")
        
        return True
    else:
        print("sorry that's not enough money. Money refunded")
        return False
def make_drink(drink_name,order_ingredinets):
    for item in order_ingredinets:
        resources[item]-=order_ingredinets[item]
    print(f"here is your {drink_name} ☕️. Enjoy!")


is_on=True
while is_on:
    choice = input("What would you like to have ? (milk/coffee/tea): ")
    if choice == "off":
        print("The system has been switched off")
        break
    elif choice=="report":
        print(f"water={resources['water']}ml")
        print(f"milk={resources['milk']}ml")
        print(f"powder={resources['powder']}grams")
        print(f"the profit is {profit} rupees")
    else:
        drink_type=menu[choice]
        print(drink_type)
        if check_resources(drink_type['ingredients']):
            payment=process_coin()
            if is_payment_successful(payment,drink_type['cost']):
                make_drink(choice,drink_type['ingredients'])





    


