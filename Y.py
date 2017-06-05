#Broken Code
def fizz_count(x):
    count = 0
    for item in x:
        if item == "fizz":
            count = count + 1 # This is correct right?
        print count 
fizz_count(['fizz', 'buzz'])
