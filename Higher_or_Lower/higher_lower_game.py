from game_data import data
import random
current_score = 0
choice_a = random.choice(data)
choice_b = random.choice(data)
def choice(user_choice):
    if user_choice in ('A' , 'B'):
        if user_choice == 'A' :
            return choice_a['follower_count'] > choice_b['follower_count']
        else :
            return choice_a['follower_count'] < choice_b['follower_count']
    else :
        return False
while True :
    if choice_a == choice_b :
    choice_b = random.choice(data)
    print(f"Compare A : {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}")
    print("VS")
    print(f"Compare B : {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}")
    user_input = input("Who has more followers? Type 'A' or 'B': ").upper()
    if choice(user_input) == True:
        current_score += 1
        print("\n" * 20)
        print(f"You are right! Current score: {current_score}")
        choice_a = choice_b
        choice_b = random.choice(data)
    else :
        print("\n" *20)
        print(f"Sorry, that's wrong. Final score: {current_score}")
        break

