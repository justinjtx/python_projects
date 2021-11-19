    # WELCOME TO GAS MONEY !!!!

    # There are 2 separate prizes (gas money prize, grand prize(car))

    # The goal for the player is to *NOT* guess how much the car is worth

    # There will be 5 differnet amounts of money written on a card to pick from
        # Create a list with 5 differnet amounts of money (front) <-- this will be the value of the car in 5 differnet amounts of money

    # behind the card, there are another 5 differnet amounts of money
            # this will be the gas money prize up to $10,000
                # list both amounts of money in key&value

    # On the front side of the card, there will be 4 correct answers and 1 incorrect answer
        # correct answer = value of the car . incorrect answer = 4 other amounts

    # if the player can pick 4 incorrect answers without picking the correct answer, player receives the car and also wins $10,000
        # however, if the player picks the correct answer, player loses current prize and loses the game
            # player will no longer be able to continue the game

    # Player can stop playing the game any moment and walk away with whatever he/she has currently won (gas money)


    # WIN BIG OR GO HOME


from lamborghini import lamborghini
from counts import counts


# game_rule = print("""
# WELCOME TO GAAAAAAAAAAAAAAAAAAAS MONEY!!!!!
# THIS IS THE GAME RULE. READ CAREFULLY!!!

# There's a brand new spankin' Lamborghini behind us.
# Your Goal is to NOT pick how this car is worth.
# You will see 5 differnet amounts written in a card to choose from.
# There's cash up to $10,000 behind 4 of these cards.
# There's a car title behind the last card
# behind 4 of those cards, there will be different amounts of cash.
# If you pick all 4 cards that contains cash, you go home with $10,000 + brand new spankin' Lamborghini.
# However, if you pick the card with a car title behind it, you lose the game and you will no longer be able to continue.

# I WISH YOU THE BEST LUCK!!!!
# LET THE GAAAAAAAAAAAAAAAAAAAS MONEY BEGIN!!!!!
# """)



# select = input("Enter any key to begin the game:" )

game_rule = print("""
WELCOME TO GAAAAAAAAAAAAAAAAAAAS MONEY!!!!!
THIS IS THE GAME RULE. READ CAREFULLY!!!

There's a brand new spankin' Lamborghini behind us.
Your Goal is to NOT pick how much this car is worth.
You will see 5 differnet amounts written in a card to choose from.
There's cash up to $10,000 behind 4 of these cards.
There's a car title behind the last card
behind 4 of those cards, there will be different amounts of cash.
If you pick all 4 cards that contains cash, you go home with $10,000 + brand new spankin' Lamborghini.
However, if you pick the card with a car title behind it, you lose the game and you will no longer be able to continue.
After picking the correct card you get to choose an option whether to continue the game or leave the game
with your current cash prize!

I WISH YOU THE BEST LUCK!!!!
LET THE GAAAAAAAAAAAAAAAAAAAS MONEY BEGIN!!!!!
""")

select = input("Enter any key to begin the game:" )
prize_pool = 0 
def main(prize_pool):      
    if prize_pool == 10000:
        print("""
  ______    ______    _______        _____  ____    ______   _______    ______   __    __ 
 /      \  /      \  /       |      /     \/    \  /      \ /       \  /      \ /  |  /  |
/$$$$$$  | $$$$$$  |/$$$$$$$/       $$$$$$ $$$$  |/$$$$$$  |$$$$$$$  |/$$$$$$  |$$ |  $$ |
$$ |  $$ | /    $$ |$$      \       $$ | $$ | $$ |$$ |  $$ |$$ |  $$ |$$    $$ |$$ |  $$ |
$$ \__$$ |/$$$$$$$ | $$$$$$  |      $$ | $$ | $$ |$$ \__$$ |$$ |  $$ |$$$$$$$$/ $$ \__$$ |
$$    $$ |$$    $$ |/     $$/       $$ | $$ | $$ |$$    $$/ $$ |  $$ |$$       |$$    $$ |
 $$$$$$$ | $$$$$$$/ $$$$$$$/        $$/  $$/  $$/  $$$$$$/  $$/   $$/  $$$$$$$/  $$$$$$$ |
/  \__$$ |                                                                      /  \__$$ |
$$    $$/                                                                       $$    $$/ 
 $$$$$$/                                                                         $$$$$$/ 

******************THANK YOU FOR PLAYING GAS MONEY.*************************
HERE'S YOUR $10,000 AND YOUR GRRRRRRRRRRRRRRAND PRIZE ....... LAMBORGHINI!!
""")
        quit()

    
    print("""
    1. $190,000
    2. $200,000
    3. $210.000
    4. $220,000
    5. $230,000
    6. View Current Prize
    """)  
    
    selection = input("Select one of the numbers 1 through 5: ")
    
    if selection == "1":
        if counts["count1"] == 1:            
            print("You already selected this option. Choose another option. ")
            main(prize_pool)
                
        else:
            counts["count1"] += 1            
            prize_pool = prize_pool + lamborghini['$190,000']
            print(f"Wow! That was a close one, ${lamborghini['$190,000']} has been added to your prize pool! \n ")
            first_prize = input(f"Your current prize is ${prize_pool} \nDo you want to continue? \nYes or No: ")

            # if first_prize != "Yes" or first_prize != "yes" or first_prize != "No" or first_prize != "no":
                
            # while True:
            #     if first_prize != "Yes" or first_prize != "yes" or first_prize != "No" or first_prize != "no":
            #         print("Error. Choose between Yes or No ")
            #         first_prize = input(f"Yes or No: ")                
            #     elif first_prize == "Yes" or first_prize == "yes" or first_prize == "No" or first_prize == "no":
            #         break
        # while first_prize != "no":
        #     print("Error. Choose between Yes or No ")
        #     first_prize = input(f"Yes or No: ")
        #     if first_prize == "Yes" or first_prize == "yes" or first_prize == "No" or first_prize == "no":
        #         break      

        if first_prize == "Yes" or first_prize == "yes":                
            main(prize_pool)
        elif first_prize == "No" or first_prize == "no":
            confirm = input(f"Are you sure you want to walk away with ${prize_pool}? Yes or No: ")
            while True:
                if confirm == "No" or confirm == "no":
                    main(prize_pool)
                elif confirm == "Yes" or confirm == "yes":
                    print(f"Thank you for playing here's your ${prize_pool}!! ") 
                    exit()                          
                else:
                    print("Please pick one of the options Yes or No: ")
                    break
        
        else:
            error_code = input("Error. Chose between Yes or No: ")
            while True:
                if error_code not in ["Yes", "yes", "No", "no"]:
                    error_code = input("Error. Choose between Yes or No: ")
                elif error_code == "Yes" or error_code == "yes" or error_code == "No" or error_code == "no":
                    break
        main(prize_pool)

    elif selection == "2":
        if counts["count2"] == 1:            
            print("You already selected this option. Choose another option. ")
            main(prize_pool)
        else:
            counts["count2"] += 1 
            prize_pool = prize_pool + lamborghini['$200,000']
            print(f"Wow! That was a close one, ${lamborghini['$200,000']} has been added to your prize pool! \n ")
            second_prize = input(f"Your current prize is ${prize_pool} \nDo you want to continue? \nYes or No: ")

        if second_prize == "Yes" or second_prize == "yes":                
            main(prize_pool)
        elif second_prize == "No" or second_prize == "no":
            confirm = input(f"Are you sure you want to walk away with ${prize_pool}? Yes or No: ")
            while True:
                if confirm == "No" or confirm == "no":
                    main(prize_pool)
                elif confirm == "Yes" or confirm == "yes":
                    print(f"Thank you for playing here's your ${prize_pool}!! ") 
                    exit()                          
                else:
                    print("Please pick one of the options Yes or No: ")
                    break
        
        else:
            error_code = input("Error. Chose between Yes or No: ")
            while True:
                if error_code not in ["Yes", "yes", "No", "no"]:
                    error_code = input("Error. Choose between Yes or No: ")
                elif error_code == "Yes" or error_code == "yes" or error_code == "No" or error_code == "no":
                    break
        main(prize_pool)

    elif selection == "4":
        if counts["count4"] == 1:            
            print("You already selected this option. Choose another option. ")
            main(prize_pool)
        else:
            counts["count4"] += 1
            prize_pool = prize_pool + (lamborghini['$220,000'])
            print(f"Outstanding! Unbeliveable luck!, ${lamborghini['$220,000']} has been added to your prize pool! \n ")
            third_prize = input(f"Your current prize is ${prize_pool} \nDo you want to continue? \nYes or No: ")
            
        if third_prize == "Yes" or third_prize == "yes":
            main(prize_pool)
        elif third_prize == "No" or third_prize == "no":
            confirm = input(f"Are you sure you want to walk away with ${prize_pool}? Yes or No: ")
            while True:
                if confirm == "No" or confirm == "no":
                    main(prize_pool)
                elif confirm == "Yes" or confirm == "yes":
                    print(f"Thank you for playing here's your ${prize_pool}!! ") 
                    exit()                         
                else:
                    print("Please pick one of the options Yes or No: ")
                    break
        else:
            error_code = input("Error. Chose between Yes or No: ")
            while True:
                if error_code not in ["Yes", "yes", "No", "no"]:
                    error_code = input("Error. Choose between Yes or No: ")
                elif error_code == "Yes" or error_code == "yes" or error_code == "No" or error_code == "no":
                    break
        main(prize_pool)

    elif selection == "5":
        if counts["count5"] == 1:            
            print("You already selected this option. Choose another option. ")
            main(prize_pool)
        else:
            counts["count5"] += 1 
        prize_pool = prize_pool + (lamborghini['$230,000'])
        print(f"You should go buy Power Ball today!, ${lamborghini['$230,000']} has been added to your prize pool! \n ")
        fourth_prize = input(f"Your current prize is ${prize_pool} \nDo you want to continue? \nYes or No: ")
            
        if fourth_prize == "Yes" or fourth_prize == "yes":
            main(prize_pool)
        elif fourth_prize == "No" or fourth_prize == "no":
            confirm = input(f"Are you sure you want to walk away with ${prize_pool}? Yes or No: ")
            while True:
                if confirm == "No" or confirm == "no":
                    main(prize_pool)
                elif confirm == "Yes" or confirm == "yes":
                    print(f"Thank you for playing here's your ${prize_pool}!! ") 
                    exit()                          
                else:
                    print("Please pick one of the options Yes or No: ")
                    break
        else:
            error_code = input("Error. Chose between Yes or No: ")
            while True:
                if error_code not in ["Yes", "yes", "No", "no"]:
                    error_code = input("Error. Choose between Yes or No: ")
                elif error_code == "Yes" or error_code == "yes" or error_code == "No" or error_code == "no":
                    break
        main(prize_pool)

    elif selection == "3":
        print(f"Oh no..You've selected, {lamborghini['$210,000']} ")
        print("You lost the game.. Try again next time!")
        exit()

    elif selection == "6":
        current_prize_pool = prize_pool
        current_prize_pool = input(f"Your current Prize is ${prize_pool}.\nPress 'Q' to go back to main menu: ")
    
        while True:
            if current_prize_pool == "Q" or current_prize_pool == "q":
                main(prize_pool)
            else:
                print("I don't think you pressed 'Q' ")
                current_prize_pool(prize_pool)
    else:
        print("\nYou have to select a number 1 through 5! ")
        main(prize_pool)


main(prize_pool)   

    #lose = input(f"Oh no.. You've selected {lamborghini['$210,000']}")
    # or i in lamborghini:
                # if i == lamborghini['$210,000']:
                #     print("You lost.. better luck next time!")
                #     quit()



