for k in range(1, 100):
    def is_prime(x):
        if x <= 3:
            return True
        if x > 3:
            for i in range(2, x-1):
               # print "Var", x, "EX", i
                if x % i == 0:
                    return False

            return True
    if is_prime(k) == True:
        print k
