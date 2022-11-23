""" Today we are going to be creating a Hangman game"""
import random
from word_list import guess_words



def get_word():
    word=random.choice(guess_words)
    return word.upper()
   
   

        
def display_hangman(tries):
     stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
     return stages[tries]
def play(word):
    word_completion="_"*len(word)
    guessed=False
    guessed_letters=[]
    guess_words=[]
    tries=6
    print("Time to play hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("/n")
    while not guessed and tries>0:
        guess=input("Guess a letter or a word:").upper()
        if len(guess)==1 and guess.isalpha():
            if guess  in guessed_letters:
                print("Your guess is already in the word.")
            elif guess not in guessed_letters:
              tries-=1
              guessed_letters.append(guess)
              word_as_list=list(word_completion)
              indices=[i for i,letter in enumerate(word) if letter==guess]
              for index in indices:
                  word_as_list[index]=guess
                  word_completion= "".join(word_as_list)
                  if "_" not in word_completion:
                      guessed=True
                      
              
            else:
                print(f"{guess} is in the word.")
        
        
        elif len(guess)==len(word) and guess.isalpha():
            if guess in guess_words:
                print("You already guessed the ",guess)
            elif guess!=word:
                print(guess,"is not in the word")
                tries-=1
                guess_words.append(guess)
            else:
             guessed=True
             word_completion=word
             
            
        else:
            print("Nope!Guess again!")
        print(display_hangman(tries))
        print(word_completion)
        print("/n")
        
    if guessed==True:
        print("Congrats! You guessed the word")
    else:
        print("Sorry! You ran out of tries. The word was",word)
        
            
def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
    
        
        
    