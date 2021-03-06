#Made by MiniatureDev
#License: CC0


# import module 

import random 

  
# Print multiline instruction 
# performstring concatenation of string 

print("Winning Rules of the Rock Paper Scissor game as follows: \n"

                                +"Rock vs paper: paper wins \n"

                                + "Rock vs scissor: Rock wins \n"

                                +"paper vs scissor: scissor wins \n") 

  

while True: 

    print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n") 

      

    # take the input from user 

    choice = int(input("User Choice: ")) 

  


    while choice > 3 or choice < 1: 

        choice = int(input("enter valid input: ")) 

          

  

    # initialize value of choice_name variable 

    # corresponding to the choice value 

    if choice == 1: 

        choice_name = 'Rock'

    elif choice == 2: 

        choice_name = 'paper'

    else: 

        choice_name = 'scissor'

          

    # print user choice  

    print("user choice is: " + choice_name) 

    print("\nNow its computer turn.......\n") 

  

    # Computer chooses randomly any number  

    # among 1 , 2 and 3. Using randint method 

    # of random module 

    comp_choice = random.randint(1, 3) 

      

    # looping until comp_choice value  

    # is equal to the choice value 

    while comp_choice == choice: 

        comp_choice = random.randint(1, 3) 

  

    # initialize value of comp_choice_name  

    # variable corresponding to the choice value 

    if comp_choice == 1: 

        comp_choice_name = 'Rock'

    elif comp_choice == 2: 

        comp_choice_name = 'paper'

    else: 

        comp_choice_name = 'scissor'

          

    print("Computer Chooses: " + comp_choice_name+"\n") 

  

    print(choice_name + " V/s " + comp_choice_name+"\n") 

  

    # condition for winning 

    if((choice == 1 and comp_choice == 2) or

      (choice == 2 and comp_choice ==1 )): 

        print("Winner = ", end = "") 

        result = "paper"

          

    elif((choice == 1 and comp_choice == 3) or

        (choice == 3 and comp_choice == 1)): 

        print("Winner=", end = "") 

        result = "Rock"

    else: 

        print("Winner=", end = "") 

        result = "scissor"

  

    # Printing either user or computer wins 

    if result == choice_name: 

        print("User") 

    else: 

        print("Computer") 

          

    print("\nDo you want to play again? (Y/N)") 

    ans = input() 

  

  

    # if user input n or N then condition is True 

    if ans == 'n' or ans == 'N': 

        break


print("\nThanks for playing!!")
