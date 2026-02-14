import random
# Function to get a valid integer input
def get_valid_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter an integer.")


            
m = get_valid_integer("Enter the lower limit of guessing -> ")
n = get_valid_integer("Enter the upper limit of guessing -> ")
while(m>n or m==n):
    print("Lower limit must be lower than upper limit ")
    m = get_valid_integer("Enter the lower limit of guessing -> ")
    n = get_valid_integer("Enter the upper limit of guessing -> ")

computer_guess = random.randint(m,n)
attempts_limit =max(5, int((n-m)*0.1))
attempts = 0
user_guess = get_valid_integer("Enter the number guessed by the computer -> ")

while(True):
    attempts += 1
    if(user_guess>computer_guess):
        print("Guess smaller number ")

    elif(user_guess<computer_guess):
        print("Guess greater number ")
    else:
        print(f"Congratulation!!\nYou guessed the number {user_guess} in {attempts} attempts ")
        break
    if(attempts>=attempts_limit):
        print("You are out of attempts better luck next time")
        break
    user_guess = get_valid_integer("your guess -> ")

