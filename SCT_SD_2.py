#number guessing game
import random #Importing random package
random_num=random.randint(1,100) #Generating a random number
attempt=0
print("Welcome to number guessing game!")
print("I've selected a number between 1 and 100. Can you guess it?")
while True:
    try:
        n1=int(input("Enter a number between 1 to 100:"))
        attempt=attempt+1
        if n1<random_num:
            print("Oh-no!too short try again!")
        elif n1>random_num:
            print("Oh-no!Too large try again!")
        else:
             print(f"Congratulations!\nYou have predicted the correct number {random_num} in {attempt} attempts.")
             break
    except ValueError:
        print("Invalid Input! Enter a number.")

