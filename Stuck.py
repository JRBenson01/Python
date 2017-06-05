def shut_down(s = "yes"):
    return s

if shut_down(s = "yes"):
    print ("Shutting down")
elif shut_down(s = "no"):
    print ("Shutdown aborted")
else:
    print ("Sorry")
