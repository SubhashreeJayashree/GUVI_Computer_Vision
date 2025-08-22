import random
def number():
    print("Welcome to the number guessing game")
    number=random.randint(1,10)
    chances=3
    for i in range(1,chances+1):
        try:
            guess=int(input("Enter the number:"))
            if(guess < number):
                print("The number is low")
            elif(guess > number):
                print("The number is high")
            else:
                print("The number is guessed in this chances",chances)
                print("The number is",number)
        except ValueError:
            print("Invalid")
    else:
        print("The number is",+number)
number()