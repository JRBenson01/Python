shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    total = 0 
    for item in food:
        total = prices[item]+total
        print "Before: %s" % (stock[item])
        stock[item] += -1
        print "After: %s" % (stock[item])
        if stock[item] < 0:
            total=total-prices[item]
    print total
compute_bill(["banana", "banana", "banana", "banana", "banana", "banana", "banana"])
