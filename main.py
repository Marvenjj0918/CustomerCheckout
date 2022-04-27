

from pyrecord import Record

def salesTax():
    state = input("Enter the State you're in? (MA,NH,MA): ")
    if state in ['MA', 'ma', 'massachusett', 'Massachusett']:
        state = 'Massachusett'
        tax = 0.625
        print(state, tax)
        return tax
    if state in ['HN', 'nh', 'New Hampshire', 'new hampshire']:
        state = 'New Hampshire'
        tax = 0
        print(state, tax)
        return tax
    if state in ['ME', 'me', 'Maine', 'maine']:
        state = 'Maine'
        tax = 0.55
        print(state, tax)
        return state, tax
    elif state:
        exit('State Error, We only working with those following state: Massachusett, New Hampshire, Maine')

def product():
    typeOfGoog = Record.create_type("typeOfGoog","name", "price" )
    wicEligibleFood= typeOfGoog.extend_type("wicEligibleFood")
    everytingElse = typeOfGoog.extend_type("everytingElse")
    clothing = typeOfGoog.extend_type("clothing")
    apples = wicEligibleFood("apples", 2.99)
    bananas = wicEligibleFood("bananas",4.4)
    jeans = clothing("jeans", 25)
    shirt = clothing("shirt", 15)
    Refrigerator = everytingElse("Refrigerator", 585)
    Dishwasher = everytingElse("Dishwasher", 260)
    print(apples,bananas)



    numberOfItem = int(input("How many item are you buying?"))
    j = 0
    newShoppingList=[]
    while j != numberOfItem:
        shoppinglist = input("Please choose a item in the lis above:")
        if shoppinglist == "apple":
            print(apples)
        else:
            print("not in the list")

        newShoppingList.append(shoppinglist)
        numberOfItem = numberOfItem-1
        print(numberOfItem, shoppinglist)
    print(newShoppingList)
    return

 #Press the green button in the gutter to run the script.
if __name__ == '__main__':
    salesTax()
    product()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
