from random import randint  # Do not delete this line

def displayIntro():
    print("""_______________________________________________
 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/
_______________________________________________
_____________________Rules_____________________
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
_______________________________________________""")


def displayEnd(result):
    if result:
        print("""________________________________________________________________________
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
________________________________________________________________________""")
    else:
        print(""" __     __           _           _   _                                    
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
__________________________________________________________________________""")


def displayHangman(state):
    stages = ["""                
     ._______.   
     |/          
     |           
     |           
     |           
     |           
     |           
 ____|___        """,
 """    ._______.   
     |/      |   
     |           
     |           
     |           
     |           
     |           
 ____|___       """,
 """    ._______.   
     ._______.   
     |/      |   
     |      (_)  
     |           
     |           
     |           
     |           
 ____|___        
            """,
 """    ._______.   
     ._______.   
     |/      |   
     |      (_)  
     |       |   
     |       |   
     |           
     |           
 ____|___       """,
 """    ._______.   
     ._______.   
     |/      |   
     |      (_)  
     |      \|/  
     |       |   
     |           
     |           
 ____|___       """,
 """     ._______.   
     |/      |   
     |      (_)  
     |      \|/  
     |       |   
     |      / \  
     |           
 ____|___  """
              ]
    print(stages[5 - state])


def getWord():
    with open("hangman-words.txt", "r") as file:
        words = file.readlines()
    return words[randint(0, len(words)-1)].strip()


def valid(c):
    if len(c) != 1:
        return False
    elif 97 <= ord(c) <= 122:
        return True
    else:
        return False


def play():
    word = getWord()
    xword = ['#'] * len(word)
    lives = 5

    while lives > 0:
        displayHangman(lives)
        joinword = ' '.join(xword)
        print(f'Guess the word: {joinword}')

        guess = input("Enter the letter: ")

        if not valid(guess):
            print("Invalid input. Please enter the lowercase, English letter: ")
            continue

        if guess in word:
            for i in range(0, len(word)):
                if guess == word[i]:
                    xword[i] = guess
        else:
            lives -= 1

        if '#' not in xword:
            displayHangman(lives)
            print(f'hidden word was {word}')
            return True

    displayHangman(lives)
    print(f'hidden word was {word}')
    return False


def hangman():
    while True:
        displayIntro()
        result = play()
        displayEnd(result)
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break


if __name__ == "__main__":
    hangman()
