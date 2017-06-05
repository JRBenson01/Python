x = 0
print "Welcome to the quiz"
print "What is 2+2?"
print "A. A Window"
print "B. 2"
print "C. Deez Nuts"
print "D. I don't care"
answer = raw_input("Choose wisely:   ").lower()
if answer == "a":
    print "Wrong answer"
    x = x-1
    print "Your score: %s" % (x)
elif answer == "b":
    print "Correct Answer"
    x = x+1
    print "Your score: %s" % (x)
elif answer == "c":
    print "Wrong Answer"
    x = x-1
    print "Your score: %s" % (x)
elif answer == "d":
    print "Wrong Answer"
    x = x-1
    print "Your score: %s" % (x)
