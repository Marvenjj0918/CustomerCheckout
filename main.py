

from pyrecord import Record


def salesTax():
    state = input("Enter the State you're in? (MA,NH,ME): ")
    if state in ['MA', 'ma', 'massachusett', 'Massachusett']:
        state = 'Massachusett'
        salesTax.tax = 0.625
        print(state, salesTax.tax)
        return state, salesTax.tax
    elif state in ['NH', 'nh', 'New Hampshire', 'new hampshire']:
        state = 'New Hampshire'
        salesTax.tax = 0
        print(state, salesTax.tax)
        return state, salesTax.tax
    elif state in ['ME', 'me', 'Maine', 'maine']:
        state = 'Maine'
        salesTax.tax = 0.55
        print(state, salesTax.tax)
        return state, salesTax.tax
    else:
        exit('State Error, We only working with those following state: Massachusett, New Hampshire, Maine')


def product():
    typeOfGoog = Record.create_type("typeOfGoog","name", "price" )
    wicEligibleFood = typeOfGoog.extend_type("wicEligibleFood")
    everytingElse = typeOfGoog.extend_type("everytingElse")
    clothing = typeOfGoog.extend_type("clothing")
    apple = wicEligibleFood("apple", 2.99)
    bananas = wicEligibleFood("bananas",4.4)
    jeans = clothing("jeans", 25)
    shirt = clothing("shirt", 15)
    Refrigerator = everytingElse("Refrigerator", 585)
    Dishwasher = everytingElse("Dishwasher", 260)
    print(apple, bananas)
    print(jeans, shirt)
    print(Refrigerator, Dishwasher)
    numberOfItem = int(input("How many item are you buying?"))
    j = 0
    newShoppingList=[]
    while j != numberOfItem:
        shoppinglist = input("Please choose a item in the lis above:")
        if shoppinglist == "apple":
            price = apple.price
            print("Apple ", "$", price)
        elif shoppinglist == "bananas":
            price = bananas.price
            print("bananas", "$", price)
        elif shoppinglist == "jeans":
            price = jeans.price
            print("jeans", "$", price)
        elif shoppinglist == "shirt":
            price = shirt.price
            print("shirt", "$", price)
        elif shoppinglist == "Refrigerator":
            price = Refrigerator.price
            print("Refrigerator", "$", price)
        elif shoppinglist == "Dishwasher":
            price = Dishwasher.price
            print("Dishwasher", "$", price)
        else:
            print("not in the list")
            price = 0
        newShoppingList.append(price)
        numberOfItem = numberOfItem-1
    Sum = sum(newShoppingList)
    print("Total before tax is: ","$",Sum)
    totals = (Sum * salesTax.tax) + Sum
    print("Sales tax is:",salesTax.tax)
    print("Total with tax included is: ", "$", totals)


def total(sate):
    return

#Press the green button in the gutter to run the script.
if __name__ == '__main__':
    salesTax()
    product()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
