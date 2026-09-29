import art
import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
Ace = cards[0]
def deal_card():
    return random.choice(cards)
def calculate_score(hand):
    score = sum(hand)
    if score > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        score = sum(hand)

    return score

blackjack = True
while blackjack:
    user_cards = []
    computer_cards = []
    want_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if want_play == "n":
        blackjack = False
        continue
    if want_play == "y":
        print(art.logo)
        for card in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())
            if calculate_score(user_cards) == 21:
                print(f"Your final hand: {user_cards}")
                print(f"Computer's final hand:{computer_cards[0]}")
                print("Black Jack! You won!")

            if calculate_score(computer_cards) == 21:
                print("You lose")
                print(f"Your final hand: {user_cards}")
                print("Get black jacked! You lose!")
                
            if calculate_score(user_cards) == calculate_score(computer_cards):
                print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}")
                print(f"Computer's final hand: {computer_cards}, final score: {calculate_score(computer_cards)}")
                print("Draw")

    print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
    print(f"Computer's first card:{computer_cards[0]}")

    draw_another = True
    while draw_another:
        draw = input("Type 'y' to get another card, type 'n' to pass: ")

        if draw == "y":
            user_cards.append(deal_card())
            print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
            print(f"Computer's first card:{computer_cards[0]}")
            if calculate_score(user_cards) > 21:
                print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}")
                print(f"Computer's final hand:{computer_cards[0]}, final score: {computer_cards[0]}")
                print("You went over. You lose")
                draw_another = False

        if draw == "n":
            while calculate_score(computer_cards) < 17:
                computer_cards.append(deal_card())

            if calculate_score(computer_cards) > 21:
                print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}")
                print(f"Computer's final hand:{computer_cards}, final score: {calculate_score(computer_cards)}")
                print("Opponent went over. You win")
                draw_another = False

            if (calculate_score(computer_cards) > calculate_score(user_cards)
                and calculate_score(computer_cards) <= 21
            ):
                print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}")
                print(f"Computer's final hand:{computer_cards}, final score: {calculate_score(computer_cards)}")
                print("You lose ")
                draw_another = False

            if calculate_score(user_cards) > calculate_score(computer_cards):
                print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}")
                print(f"Computer's final hand: {computer_cards}, final score: {calculate_score(computer_cards)}")
                print("You win")
                draw_another = False

            if calculate_score(user_cards) == calculate_score(computer_cards):
                print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}")
                print(f"Computer's final hand: {computer_cards}, final score: {calculate_score(computer_cards)}")
                print("Draw")
                draw_another = False