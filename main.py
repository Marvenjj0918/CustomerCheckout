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
        return tax
    elif state:
        exit('State Error, We only working with those following state: Massachusett, New Hampshire, Maine')

def product():
    wicEligibleFood =['apples', 'bananas', 'carrots', 'potatoes','Cheese','Milk','Juice','Bread','Cereal','Yogurt']
    for i in wicEligibleFood:
        print(i)
    clothing = ['jeans', 'shirt', 't-shirt', 'pantys' 'boxer', 'sweater','jacket','coat','socks','shorts','tracksuit']
    for i in clothing:
        print(i)
    everytingElse =['Refrigerator ','cooktop ','Dishwasher ','washer ','dryer','Microwave ','oven']
    for i in everytingElse:
        print(i)
    return

 #Press the green button in the gutter to run the script.
if __name__ == '__main__':
    salesTax()
    product()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
