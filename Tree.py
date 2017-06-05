def Tree1():
    print "You find a tree"
    print "The tree can either be cut down or kept for later"
    answer = raw_input('Which do you choose?').lower()
    if answer == "cut down" or answer == "cut":
        print "You get 2 logs from the tree"
    elif answer == "keep" or answer == "keep tree":
        print "The tree is getting much healthier and now bears fruit"
    else:
        print "You big BABY! GROW A PAIR AND PICK A SIDE!"
        Tree1()

Tree1()
                       
