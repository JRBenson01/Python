def purify(x):
    for i in range(len(x)):
        print i
        if x[i] % 2 == 0:
            print "Even"
        elif x[i] % 2 != 0:
            x.pop(i)
            print "Odd"
    print x

purify([4, 5, 5, 4])
