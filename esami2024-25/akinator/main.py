# Write your solution here, DO NOT START A NEW PROJECT
# ATTENTION: if you create a new project, your exam paper will not be collected
#            and you will be obliged to come in the subsequent exam session
#
# ATTENTION: on Win 10 (Italian keyboard) characters like [ ] { } have to be
#            created using ALTgr+è (e.g. for [ ) and NOT CTRL-ALT-è
#
# ATTENTION: on macOS you have to use CTRL-C and CTRL-V inside the virtual
#            machine and NOT command-C command-V
#
# if your keyboard is broken you can do copy/paste also with mouse
# and you can copy special characters like [ ] { } < > here
#
# Scrivete qui la vostra soluzione, NON CREATE UN NUOVO PROGETTO
# ATTENZIONE: se create un nuovo progetto il vostro compito non sara'
#             raccolto correttamente e dovrete tornare all'appello successivo
#
# ATTENZIONE: su Win 10 (tastiera italiana) i caratteri speciali (es. { ) vanno
#             scritti ad esempio con ALTgr+è (caso di [ ) e NON CTRL-ALT-è
#
# ATTENZIONE: su macOS vanno usati CRTL-C e CTRL-V per il copia incolla
#                       nella macchina virtuale e NON command-C command-V
#
# se la vostra tastiera è guasta potete fare copia/incolla anche con il mouse
# e per i caratteri speciali potete copiare da questi caratteri  [  ]  {  }  <  >
# print(string.punctuation)
## ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~
import random

FILEPATH_DIFFICOLTA = {
    1 : "facile.txt",
    2 : "medio.txt",
    3 : "difficile.txt" 
    }

LETTERS_LIST = [
    'a',
    'b',
    'c', 
    'd', 
    'e', 
    'f', 
    'g', 
    'h', 
    'i', 
    'l', 
    'm', 
    'n', 
    'o', 
    'p', 
    'q', 
    'r', 
    's', 
    't', 
    'u', 
    'v', 
    'z',
    'w',
    'y', 
    'j',
    'k', 
    'x'
    ]

playing = True

difficulty_path = None

score = 10
rolled_word = ""
current_guess = list()

def main():
    global playing
    global score
    
    games_won = 0
    games_lost = 0

    while playing:
        letters_to_try = LETTERS_LIST.copy()

        global score
        score = 10

        global current_guess
        current_guess = list()

        global difficulty_path 
        difficulty_path = roll_diff()

        print(f"Partita numero {games_won + games_lost + 1}")
        print(f"Il bot seleziona la difficoltà: {difficulty()}")
        global rolled_word
        rolled_word = roll_word(difficulty_path)
        
        for _ in rolled_word:
            current_guess.append("_")

        while score > 0 and len(letters_to_try) > 0 and "".join(current_guess) != rolled_word.strip():
            guessed = guess(letters_to_try)
            roll_turn(guessed)

        won = "".join(current_guess) == rolled_word.strip()
        games_won += int(won)
        games_lost += int(not won)

        print(f"Complimenti, il bot ha vinto! La parola {rolled_word.upper()} è stata indovinata correttamente" if won else f"Peccato, il bot ha perso! La parola da indovinare era {rolled_word.upper()}")


        playing = True if input("Vuoi continuare a giocare?[S|N] ").lower() == "s" else False

    print(f"SESSIONE TERMINATA\nIl bot ha vinto {games_won} partita/e\nIl bot ha perso {games_lost} partita/e")

def roll_diff():
    return FILEPATH_DIFFICOLTA[random.randint(1, 3)]

def roll_word(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        words = file.readlines()
        return words[random.randint(0, len(words) - 1)].strip().lower()

def guess(letters_to_try):
    letter = letters_to_try[random.randint(0, len(letters_to_try) - 1)]
    letters_to_try.remove(letter)
    return letter

def roll_turn(guess):
    
    global score
    print(f"Punti {score} - La parola da indovinare è: {formatted_to_guess()}")
    is_guess_right = rolled_word.count(guess) != 0
    score -= 1 * int(not is_guess_right)
    update_current_guess(guess)
    print(f"\tLettera scelta dal bot: {guess}\n\t{f"Lettera '{guess}' non presente" if not is_guess_right else f"Lettera '{guess}' presente: {formatted_to_guess()}"}")

def update_current_guess(guess):
    for index, char in enumerate(rolled_word):
        if char == guess:
            current_guess[index] = guess

def formatted_to_guess():
    global current_guess
    return "".join(current_guess)

def difficulty():
    return f"{difficulty_path.replace(".txt", "").strip()}"

main()