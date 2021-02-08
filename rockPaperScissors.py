import random
import os
import re
os.system('cls' if os.name=='nt' else 'clear')
while (1 < 2):
    print ("\n")
    print ("Rock, Paper, Scissors - Shoot!")
    userChoice = str.upper(input("Choose your weapon [R]ock], [P]aper, or [S]cissors: "))
    if not re.match("[SsRrPp]", userChoice):
        print ("Pleace choose a letter:")
        print ("[R]ock, [S]cissors or [P]aper.")
        continue

    print ("You choose: " + userChoice)
    choices = ['R', 'P', 'S']
    opponenentChoice = random.choice(choices)
    print ("I chose: " + opponenentChoice)
    if opponenentChoice == userChoice:
        print ("Tie! ")
    elif opponenentChoice == 'R' and userChoice == 'S':
        print ("Scissors beats rock, I win! ")
        continue
    elif opponenentChoice == 'S' and userChoice == 'P':
        print ("Scissors beats paper! I win! ")
        continue
    elif opponenentChoice == 'P' and userChoice == 'R':
        print ("Paper beat rock, I win! ")
        continue
    else:
        print ("You win!")