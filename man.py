import random

word_list = ["zindua", "hangman", "python", "palindrome", "currency", "variables", "strings", "dictionaries"]
random_word = random.choice(word_list)
guesses = " "
attempts = 6

while attempts > 0:
    failed = 0             
    for char in random_word:      
        if char in guesses:    
            print (char,end="")    
        else:
            print ("_",end=""),     
            failed += 1    
    if failed == 0:        
        print ("\nYou won") 
        break     
guess = input("\nGuess only one letter at a time without repetition: ")
guesses += guess       
if guess not in random_word:  
    attempts-= 1        
    print("\nWrong")    
    print("\nYou have", + attempts, 'more guesses') 
    if attempts == 0:           
        print ("\nYou Lose") 

