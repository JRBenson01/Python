
c = False
a = False
t = False
word= [c, a, t]
first = ""
second = ""
third = ""
completed = False
while completed == False:
    guess = raw_input("Guess a letter:   ")
    for letter in word:
        if letter == "c":
            c = True
        if letter == "a":
             a = True
        if letter == "t":
            t = True
    if c == True and a == True and t == True:
        completed = True
    if c == True:
        first = "c"
    if a == True:
        second = "a"
    if t == True:
        third = "t"
    print first, second, third
        

    


        
        
        
