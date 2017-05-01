count = 0
while True:
    try:
        x = int(raw_input("Enter number:   "))
        break
    except ValueError:
        print "Input a number you moron"
        count += 1
print "Your number: ", x
if count > 5:
    print "About time, jackass"
