import random


from random import randint


def displayIntro():
    print(r"""
 _______________________________________________
  _                                             
 | |                                            
 | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
 | '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
 | | | | (_| | | | | (_| | | | | | | (_| | | | |
 |_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                     __/ |                      
                    |___/                       
 _______________________________________________
 _______________________________________________
 ____________________Rules______________________
 Try to guess the hidden word one letter at a   
 time. The number of dashes are equivalent to   
 the number of letters in the word. If a player 
 suggests a letter that occurs in the word,     
 blank places containing this character will be 
 filled with that letter. If the word does not  
 contain the suggested letter, one new element  
 of a hangman’s gallow is painted. As the game  
 progresses, a segment of a victim is added for 
 every suggested letter not in the word. Goal is
 to guess the word before the man hangs!        
 _______________________________________________
""")

def getWord():
        with open("hangman-words", "r") as file:
            words = file.readlines()
        return random.choice(words).strip()



def valid(guess):
        return guess.isalpha() and guess.islower() and len(guess) == 1





def displayHangman(lives):
    hangman_visuals = [
        r"""
     ._______.
     |/          
     |           
     |           
     |           
     |           
     |           
 ____|___       
        """,

        r"""
     ._______.   
     |/      |   
     |           
     |           
     |           
     |           
     |           
 ____|___ 
        """,
        r"""
     ._______.   
     |/      |   
     |      (_)  
     |           
     |           
     |           
     |           
 ____|___ 
        """,
        r"""
     ._______.   
     |/      |   
     |      (_)  
     |       |  
     |       |    
     |           
     |           
 ____|___  
        """,
        r"""
      ._______.   
      |/      |   
      |      (_)  
      |      \|/  
      |       |   
      |           
      |           
  ____|___   
         """,
        r"""
        ._______.   
     |/      |   
     |      (_)  
     |      \|/  
     |       |   
     |      / \  
     |           
 ____|___ 
         """
    ]
    print(hangman_visuals[5 - lives])



def displayEnd(result, word, lives):
    if result:
        winner()
        print("Hidden word was:", word)
        print("You win!")
    else:
        loser()
        print("Hidden word was:", word)
        print("You lose!")




def winner():
    print(r"""
________________________________________________________________________
          _                                  _                          
         (_)                                (_)                         
__      ___ _ __  _ __   ___ _ __  __      ___ _ __  _ __   ___ _ __    
\ \ /\ / / | '_ \| '_ \ / _ \ '__| \ \ /\ / / | '_ \| '_ \ / _ \ '__|   
 \ V  V /| | | | | | | |  __/ |     \ V  V /| | | | | | | |  __/ |      
  \_/\_/ |_|_| |_|_| |_|\___|_|      \_/\_/ |_|_| |_|_| |_|\___|_|      
           | |   (_)    | |                  | (_)                      
        ___| |__  _  ___| | _____ _ __     __| |_ _ __  _ __   ___ _ __ 
       / __| '_ \| |/ __| |/ / _ \ '_ \   / _` | | '_ \| '_ \ / _ \ '__|
      | (__| | | | | (__|   <  __/ | | | | (_| | | | | | | | |  __/ |   
       \___|_| |_|_|\___|_|\_\___|_| |_|  \__,_|_|_| |_|_| |_|\___|_|   
________________________________________________________________________
""")



def loser():
    print(r"""
____   __          _           _   _                                  
\ \   / /          | |         | | | |                                   
 \ \_/ /__  _   _  | | ___  ___| |_| |                                   
  \   / _ \| | | | | |/ _ \/ __| __| |                                   
   | | (_) | |_| | | | (_) \__ \ |_|_|                                   
   |_|\___/ \__,_| |_|\___/|___/\__(_)                                   
       _______ _                                        _ _          _ _ 
      |__   __| |                                      | (_)        | | |
         | |  | |__   ___   _ __ ___   __ _ _ __     __| |_  ___  __| | |
         | |  | '_ \ / _ \ | '_ ` _ \ / _` | '_ \   / _` | |/ _ \/ _` | |
         | |  | | | |  __/ | | | | | | (_| | | | | | (_| | |  __/ (_| |_|
         |_|  |_| |_|\___| |_| |_| |_|\__,_|_| |_|  \__,_|_|\___|\__,_(_)
__________________________________________________________________________
""")

def play():
    word = getWord()
    guessed_letters = set()
    lives = 5

    while lives > 0:
        displayHangman(lives)
        display_word = ""
        for char in word:
            if char in guessed_letters:
                display_word = display_word + char
            else:
                display_word = display_word + "_"
        print("Guess the word:", display_word)

        guess = input("Enter the letter: ")
        if not valid(guess):
            print("Please enter a valid lowercase letter.")
            continue

        if guess in word:
            print("Correct guess!")
            guessed_letters.add(guess)
            if all(char in guessed_letters for char in word):
                return True, word, lives
        else:
            print("Incorrect guess!")
            lives = lives - 1

    return False, word, lives

def hangman():
    while True:
        displayIntro()
        result, word, lives = play()
        displayEnd(result, word, lives)
        play_again = input("Do you want to play again? (yes/no) ")
        if play_again.lower() != "yes":
            break

if __name__ == "__main__":
    hangman()