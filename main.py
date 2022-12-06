# Create a cool title 

# Function to get letter from the user
def getLetter():
  # Create a variable to hold the letter with a dummy value
  userWord = ""
  # Until the user enters a string with ONE character...
  while len(userWord) !=1:
    # Prompt the user to enter a letter
    userWord = input("Please enter a letter: ")
  # Return the letter
  return userWord.lower()

# Create a function that displays the secret word
def hiddenWord(word, guesses):
  # Go through each letter in the secret word, and determine HOW we display it
  for letter in word:
    
    # If this letter (from the secret word) has been guessed, display the letter
    if letter in guesses:
      print(letter, end=" ")
    # Otherwise, display an underscore ( _ ) 
    else: 
      print("_", end=" ")
  

test = "______"
secretWord = "hitboxes" 
letters = [ ]
guessCounter = 0
max_Guesses = 5  
# Create a function that determines if the user has won the game
def getWinner(word , guesses):
  
  # Let's use an "Innocent Until Proven Guilty" Algorithm...
  # ...and create a variable that is set to "True"
  Win = True 
  # Go through each letter in the secret word
  for letter in word: 
    # Check if the letter has been guessed
    if letter not in guesses: 
      
      # If it has NOT been guessed, set the variable we created to False, and stop the loop
      Win = False 
      break
  return Win 

while not getWinner(secretWord, letters) and guessCounter < 5:

  # Get a letter from
  userGuess = getLetter() 
  
  # Add the guess to your list of guesses
  letters.append(userGuess)
   
  # Determine if the letter is in the word
  if userGuess in secretWord:  
    # if it is, display that it was a good guess
    print("Correct!")
  # Otherwise
  else:
    # display it's a bad guess
    max_Guesses = max_Guesses - 1
    print("Incorrect!")
    print()
    print(f"You have {max_Guesses} guesses left ")
    print()
    # add a strike to your strike counter 
    guessCounter += 1
  
  hiddenWord(secretWord, letters)
  print()
  
if guessCounter == 5:
  print("Sorry you lose try again? ")
else:
  print("Congrats!!! you won!!") 

  