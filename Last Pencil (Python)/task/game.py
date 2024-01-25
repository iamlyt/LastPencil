import sys
import random


def check_number(input_to_check):
    # check if user_input is number and less than 3 and more than 0
    if not user_input.isnumeric():
        print("Possible values: '1', '2' or '3'")
    else:
        user_number = int(input_to_check)
        if user_number not in [1, 2, 3]:
            print("Possible values: '1', '2' or '3'")
        elif user_number > difference:
            print("Too many pencils were taken")


print("How many pencils would you like to use:")
while True:
    pencils_amt = input()

    if not pencils_amt.isnumeric():
        print("The number of pencils should be numeric")
    else:
        pencils = int(pencils_amt)

        if pencils <= 0:
            print("The number of pencils should be a positive integer")
        else:
            print("Who will be the first (John, Jack):")
            name = input()

            while name not in ["John", "Jack"]:
                print("Choose between 'John' and 'Jack'")
                name = input()

            difference = pencils
            pencils_list = ['|' for _ in range(pencils)]
            switch_flag = (name == "John")

            print(''.join(pencils_list))

            while difference > 0:
                name = "John" if switch_flag else "Jack"


                # if John - user_inputs number

                # if Jack's turn - automatic (bot)

                if name == "John":
                    print("John's turn!")
                    user_input = input()
                    # check if user_input is number and less than 3 and more than 0
                    if not user_input.isnumeric():
                        print("Possible values: '1', '2' or '3'")
                    else:
                        user_number = int(user_input)
                        if user_number not in [1, 2, 3]:
                            print("Possible values: '1', '2' or '3'")
                        elif user_number > difference:
                            print("Too many pencils were taken")
                        else:
                            difference -= int(user_input)
                            print("|" * difference)
                            switch_flag = not switch_flag

                if name == "Jack":

                    print("Jack's turn:")
                    remainder = difference % 4

                    if difference == 1:
                        difference = 0
                        print("1")
                        print("|" * difference)
                        # print("John won!")
                        switch_flag = not switch_flag
                        break

                    if remainder == 0:
                        difference -= 3
                        print("3")
                    elif remainder == 1:
                        random_number = random.randint(1, 3)
                        difference -= random_number
                        print(f"{random_number}")
                    elif remainder == 2 and difference:
                        difference -= 1
                        print("1")
                    elif remainder == 3:
                        difference -= 2
                        print("2")
                    else:
                        print("Invalid")

                    print("|" * difference)
                    switch_flag = not switch_flag

            winner = "Jack" if switch_flag else "John"
            loser = "John" if switch_flag else "Jack"

            print(f"{loser} won!")
            sys.exit()  # Terminate the program


