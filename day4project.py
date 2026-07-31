import random

rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
paper='''
        _______
     ---'   ____)____
               ______)
               _______)
              _______)
     ---.__________)
'''
scissors='''
          _______
       ---'   ____)____
                 ______)
              __________)
             (____)
       ---.__(___)
'''
item_list=[rock,paper,scissors]
computerchoice=random.choice(item_list)
player_choice=input("What do you chose? Type 0 for Rock , 1 for paper or 2 for scissors")
finalchoice=item_list[int(player_choice)]
print(f"your choice is {item_list[int(player_choice)]}")
print(f" computer choice is {computerchoice}")

if  computerchoice==scissors and  finalchoice == rock:
    print("you won")
elif computerchoice==finalchoice:
    print("it is draw")
elif computerchoice==paper and finalchoice==scissors:
    print("you won")
elif computerchoice==rock and finalchoice==paper:
    print("you won ")
else:
    print("you lose")
