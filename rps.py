#Go fuck yourself
import random
choose = ""
win = 8
Pscore = 0
Cscore = 0
round_number = 0
def scoreboard(Pscore, Cscore):
    print "Your score:", Pscore, "  Computer's score:", Cscore 
def check_winner(Pscore, Cscore):
    if Pscore > Cscore:
        print "YOU WIN THE GAME"
    if Pscore < Cscore:
        print "YOU LOST THE GAME"
    if Pscore == Cscore:
        print "YOU TIED YA PLEB"
def right_answer(choice):
    valid = False
    options = ["rock", "paper", "scizzors"]
    for option in options:
        if choice == option:
            valid = True
        
            
while round_number < 3:
    
    num = random.randint(1, 3)
    if num == 1:
        choose = "scizzors"
    if num == 2:
        choose = "paper"
    if num == 3:
        choose = "rock"
    player_option = raw_input("Choose rock, paper, or scizzors:    ")
    choice = player_option.lower()
    if choice == "rock" and num == 1: #scizzors
        win = True
        #print "1"
    if choice == "paper" and num == 1: #scizzors
        win = False
        #print "2"
    if choice == "scizzors" and num == 2: #paper
        win = True
        #print "3"
    if choice == "rock" and num == 2: #paper
        win = False
        #print "4"
    if choice == "scizzors" and num == 3: #rock
        win = False
        #print "5"
    if choice == "paper" and num == 3: #rock
        win = True
        #print "6"
    if choice == choose:
        win = 2
    for item in 
    print "Your Choice:", choice, "  Computer's Choice:", choose
    if win == True:
        print "YOU WON!"
        Pscore += 1
    if win == False:
        print "YOU LOST"
        Cscore += 1
    if win == 2:
       print "YOU BOTH CHOSE THE SAME THING, DUMBASS."
    scoreboard(Pscore, Cscore)
    round_number += 1
scoreboard(Pscore, Cscore)
check_winner(Pscore, Cscore)

