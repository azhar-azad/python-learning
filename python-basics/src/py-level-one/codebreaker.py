import random


def main():
    print_initial_message()
    computer_num = str(get_computer_number())
    # print(computer_num)

    win = False
    i = 0
    while i < 20:
        user_input = get_user_input()

        if user_input == computer_num:
            print("You guessed RIGHT!!")
            win = True
            break

        print(get_clue(user_input, computer_num))
        i += 1

    if win:
        if i > 1:
            print("You tried {} times".format(i + 1))
        else:
            print("You tried {} time".format(i + 1))
    else:
        print("All chances are over")



def get_user_input():

    user_input = input("Enter your guess: ")

    if len(user_input) != 3:
        print("Please enter only 3 digit number")
        get_user_input()

    if user_input[0] == user_input[1] or user_input[1] == user_input[2] or user_input[2] == user_input[0]:
        print("No repeating digits!! Try again")
        get_user_input()

    if int(user_input) < 100:
        print("No 0 is allowed, Guess with a number that doesn't contain 0(zero)")
        get_user_input()

    return user_input;


def print_message(message):
    print(message);


def print_initial_message():

    initial_message1 = "Welcome Code Breaker! Let's see if you can guess my 3 digit number!"
    initial_message2 = "Code has been generated and you have 20 guesses!!"

    print_message(initial_message1)
    print_message(initial_message2)


def get_computer_number():

    # generate all digits from 1 to 9
    digits = [str(num) for num in range(1, 10)];

    # shuffle the digits
    random.shuffle(digits)

    # grab the first three and return as string
    num = ""
    for i in range(3):
        num += digits[i]
    return num



def get_clue(user_input, computer_num):
    clue = ""
    user_num = user_input

    if user_num[0] == computer_num[0] or user_num[1] == computer_num[1] or user_num[2] == computer_num[2]:
        clue += "Match"
        return clue

    for i in range(len(user_num)):
        if user_num[i] in [computer_num[0], computer_num[1], computer_num[2]]:
            clue += "Close"
            return clue

    clue += "Nope"
    return clue

main()
# print(get_computer_number())