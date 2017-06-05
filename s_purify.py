def purify(x):
    for i in range(len(x)):
       # print i
        print x[i]
        if x[i] == 5:
            x.pop(i)
            print "pop"
    print x
purify([4, 5, 5, 4])
