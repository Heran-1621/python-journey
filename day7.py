#HANGMAN PROJECT
import random
from hangmanascii import stages
lives=6
display=[]
word_list=["ardvark","baboon","camel"]
chosen_word=random.choice(word_list)
word_len=len(chosen_word)
for letter in range(word_len):
    display.append("_")
print(display)


while "_" in display and lives>0:
    guess=input("guess a letter: ").lower()
    for letter in range(word_len):
        if chosen_word[letter]==guess:
                display[letter]=guess
    if guess not in chosen_word:
        lives-=1
    print(display)
    print(f"you have {lives} lives left")
    print(stages[lives])
if "_" not in display:
    print("you win")
else:
    print("you lose")