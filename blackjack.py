import random
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def deal_card():
    return random.choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if sum(cards) > 21 and 11 in cards:
        cards[cards.index(11)] = 1
    return sum(cards)

def compare(user_score, comp_score):
    if user_score > 21:
        return "You went over. You lose 😤"
    if comp_score > 21:
        return "Computer went over. You win 😎"
    if user_score == comp_score:
        return "Draw 🙃"
    if comp_score == 0:
        return "Lose, opponent has Blackjack 😱"
    if user_score == 0:
        return "Win with a Blackjack 😎"
    if user_score > comp_score:
        return "You win 😃"
    return "You lose 😤"

def play_game():
    print(logo)

    user_cards = [deal_card(), deal_card()]
    comp_cards = [deal_card(), deal_card()]
    
    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(comp_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {comp_cards[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            game_over = True
        else:
            user_choice = input("Type 'hit' to get another card, type 'stand' to pass: ").lower()
            if user_choice == "hit":
                user_cards.append(deal_card())
            else:
                game_over = True

    while calculate_score(comp_cards) < 17 and sum(user_cards) < 22:
        comp_cards.append(deal_card())

    print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}")
    print(f"Computer's final hand: {comp_cards}, final score: {calculate_score(comp_cards)}")
    print(compare(calculate_score(user_cards), calculate_score(comp_cards)))

while input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ") == "yes":
    print("\n" * 30)
    play_game()

"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |
      `------'                           |__/

Your cards: [2, 11], current score: 13
Computer's first card: 4
Type 'hit' to get another card, type 'stand' to pass: hit
Your cards: [2, 11, 6], current score: 19
Computer's first card: 4
Type 'hit' to get another card, type 'stand' to pass: stand
Your final hand: [2, 11, 6], final score: 19
Computer's final hand: [4, 10, 8], final score: 22
Computer went over. You win 😎
Do you want to play a game of Blackjack? Type 'yes' or 'no':"""