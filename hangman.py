import random

word_list = [
    "apple", "chair", "house", "table", "zebra", "grape", "music", "light", "stone", "bread",
    "picture", "holiday", "balloon", "diamond", "blanket", "monster", "journey", "battery", "kingdom", "flamingo",
    "adventure", "happiness", "instrument", "volunteer", "pineapple", "backwards", "mysterious", "knowledge", "television", "wonderland"
]

logo = r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print(logo)
lives = 6


chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(f"****************************<{lives}>/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You have already guessed: {guess}")
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True

            print(f"***********************IT WAS {chosen_word}YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])


"""
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/
Word to guess: _____
****************************<6>/6 LIVES LEFT****************************
Guess a letter: a
Word to guess: __a__

  +---+
  |   |
      |
      |
      |
      |
=========

****************************<6>/6 LIVES LEFT****************************
Guess a letter: e
Word to guess: __a_e

  +---+
  |   |
      |
      |
      |
      |
=========

****************************<6>/6 LIVES LEFT****************************
Guess a letter: p
Word to guess: __ape

  +---+
  |   |
      |
      |
      |
      |
=========

****************************<6>/6 LIVES LEFT****************************
Guess a letter: g
Word to guess: g_ape

  +---+
  |   |
      |
      |
      |
      |
=========

****************************<6>/6 LIVES LEFT****************************
Guess a letter: r
Word to guess: grape
****************************YOU WIN****************************

  +---+
  |   |
      |
      |
      |
      |
=========  """