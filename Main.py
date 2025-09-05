import random
AI = random.choice(["rock", "paper", "scissors"]) #all code made by Joel or ThatOneDev-studio
while True:
    PL = input("Let's play rock paper scissors! Pick a choice and press enter! ")
    if PL == AI:
         print("Tie")
    elif PL == "rock" and AI == "paper":
        print("Win")
    elif PL == "paper" and AI == "rock":
        print("Win")
    elif PL == "scissors" and AI == "paper":
        print("Win")
    else:
        print("Lose")
