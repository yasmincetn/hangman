
import random
import hangman_logo
print(hangman_logo.logo)
word_list= ["ardvark","baboon","camel"]
word=random.choice(word_list)
blank=[]
letters=[]
for n in range(0,len(word)):
    blank+="_"
for l in word:
   letters.append(l)
end_of_game=False
s=5
same_letter=[]
while end_of_game is False:
 letter=input("Guess a letter:").lower()
 if letter in blank:
    print(f"You have already guessed {letter}")
 for n in range(len(word)):
     if letters[n]==letter:
       blank[n]=letter
 
 if letter not in blank:
    print(f"You guesssed {letter}, that's not in the word.You lose a life.")
    print(hangman_logo.stages[s])
    s-=1#stages elements one by one beginning the end of the list.
    if s==-1:
       print("You lose")
       end_of_game=True
    
 print(*blank)   
 
 if "_" not in blank:
   print("You win")
   end_of_game=True
 