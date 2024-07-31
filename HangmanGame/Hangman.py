#Step 1
import random
import wordlist
import Art


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
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




print(Art.logo)

word_list = wordlist.word_list
end=False
lives=6
chosen_word=random.choice(word_list)

l=len(chosen_word)
new=[]
for i in range(l):
    new.append('_')


while not end:
    guess=input("enter any letter:").lower()
    if guess in new:
        print(f"you have already guessed {guess}")
    for position in range (len(chosen_word)):
        letter=chosen_word[position]
        if letter==guess:
            new[position]=guess

    if guess not in chosen_word:
        lives-=1
        if lives==0:
            print('You lose')
            end=True
    print(f"{''.join(new)}")
    if '_' not in new:
        end = True
        print("you win")

    print(stages[lives])