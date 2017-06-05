def test(x):
    print "This is the test to determine your S-M-R-T-ness"
    print "Start with the first question:"
    a = raw_input('2+2?: ')
    if a == "4" or a == "2+2":
        print "Correct!"
        return x = x+1
    else:
        print "NOPE"
        test(x)

test(x)
    
