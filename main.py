# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


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
    wicEligibleFood =['apples', 'bananas', 'carrots']
    wicEligibleFoodPrices = [2.99, 4.50, 5]

    clothing = ['jeans', 'shirt', 't-shirt']
    clothingPrices = [25.99, 14.50, 15]


    everytingElse = ['Refrigerator ', 'cooktop', 'Dishwasher ']
    everytingElsePrices = [599, 450, 255]

    mergeList = wicEligibleFood + clothing + everytingElse
    mergePrice = wicEligibleFoodPrices + clothingPrices + everytingElsePrices
    for i in mergeList:
        print(i)

    numberOfItem = int(input("How many item are you buying?"))
    j = 0
    newShoppingList=[]
    while j != numberOfItem:
        shoppinglist = input("Please choose a item in the lis above:")
        if shoppinglist == "apples":
            print(mergeList[0],mergePrice[0])

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
