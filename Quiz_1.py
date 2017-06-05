print "Pick an Answer"
print "A. Nope"
print "B. Yes"
a = raw_input("Pick:  ").lower()
if a == "a":
    print "Bad! Answer: %s" % (a)
elif a == "b":
    print "Good! Answer: %s" % (a)
