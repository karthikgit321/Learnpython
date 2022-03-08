import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

games_images=[rock,paper,scissors]
user_choice=int(input("Enter 0 for rock,1 for paper and 2 for scissors\n"))
if user_choice>=3 or user_choice<0:
    print("You have chose invalid number")
else:
    print(games_images[user_choice])
    comp_choice=random.randint(0,2)
    print("computer choice is:")
    print(comp_choice)
    print(games_images[comp_choice])


    if comp_choice==user_choice:
        print("its a draw")
    elif comp_choice==2 and user_choice==0:
        print("you win")
    elif user_choice==2 and comp_choice==0:
        print("You lose")
    elif comp_choice > user_choice:
        print("You lose")
    elif user_choice > comp_choice:
        print("You win!")


