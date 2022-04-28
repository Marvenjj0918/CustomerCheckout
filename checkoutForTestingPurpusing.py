from pyrecord import Record

def product(state):
    typeOfGoog = Record.create_type("typeOfGoog","name", "price" )
    wicEligibleFood = typeOfGoog.extend_type("wicEligibleFood")
    everytingElse = typeOfGoog.extend_type("everytingElse")
    clothing = typeOfGoog.extend_type("clothing")
    apple = wicEligibleFood("apple", 2.99)
    bananas = wicEligibleFood("bananas", 4.5)
    jeans = clothing("jeans", 25)
    shirt = clothing("shirt", 15)
    Refrigerator = everytingElse("Refrigerator", 585)
    Dishwasher = everytingElse("Dishwasher", 260)
    newShoppingList = apple.price + bananas.price + jeans.price + shirt.price + Refrigerator.price + Dishwasher.price
    #newShoppingList.append("price")
    print(newShoppingList)

    if state in ['MA', 'ma', 'massachusett', 'Massachusett']:
        tax = 0.625
        totals = (newShoppingList * tax) + newShoppingList
        print(totals)
        return totals
    elif state in ['NH', 'nh', 'New Hampshire', 'new hampshire']:
        tax = 0
        totals = (newShoppingList * tax) + newShoppingList
        print(totals)

        return tax
    elif state in ['ME', 'me', 'Maine', 'maine']:
        tax = 0.55
        totals = (newShoppingList * tax) + newShoppingList
        print(totals)

        return tax
    else:
        exit('State Error, We only working with those following state: Massachusett, New Hampshire, Maine')