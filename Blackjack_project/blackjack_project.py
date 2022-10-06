import random
from turtle import clearscreen

card = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def deal_card():
    """Returns a random card from the choices available to it"""
    c = random.choice(card)
    return c

def calculate_score(ls):
        s = sum(ls)
        if(s == 21 and len(ls)==2):
            return 0
            """we have to return that it's a blackjack"""
        if(11 in ls and s>21):
            ls.remove(11)
            ls.append(1)
            s -= 10
        return s

def compare(us, cs):
    if(us==cs):
        return "DRAW"
    elif(cs==0):
        return "Lose , opponent has a blackjack!"
    elif(us == 0):
        return "Win with a blackjack"
    elif(us > 21):
        return "Lose as you went over"
    elif(cs > 21):
        return "Win as the opponent went over"
    elif(us > cs):
        return "You win "
    else:
        return "Lose"

def play_game():
    is_game_over = False
    user = []
    computer = [] 
    for _ in range(2):
        user.append(deal_card())
        computer.append(deal_card())
    while(is_game_over == False):
        user_score = calculate_score(user)
        computer_score = calculate_score(computer)
        print(f" Your cards are : {user} and your score is {user_score}")
        print(f" Computer's cards are : {computer} and their score is {computer_score}")

        if(user_score == 0 or computer_score==0 or user_score > 21):
            is_game_over = True
        else:
            print("The user may deal another card. Want to deal one more : y/n?")
            ans = input()
            if(ans == "yes" or ans == 'y' or ans=="Y"):
                user.append(deal_card())
            else:
                is_game_over=True

    while(computer_score != 0 and computer_score<17):
        computer.append(deal_card())
        computer_score = calculate_score(computer)

    print(compare(user_score,computer_score))


while(input("Wanna play black jack ??? Y?N : ") == 'Y'):
    clearscreen()
    play_game()
