print("Welcome , sorry for losing your pet. But don't WOrry we gonna find it ")
print('''
                  
            ,/\,
          . /`_`\,
        , /`____-`\,
      , /`[_ROVER_]`\,
    , /`=  ==  __-  _`\,
    /|__=  __- == _  __|
   ` |  __ .-----.  _  | `
     | - _/       \-   |
     |__  | .-"-. | __=|
     |  _=|/)   (\|    |
     |-__ (/ a a \) -__|
jgs  |___ /`\_Y_/`\____|
          \)8===8(/
''')
way=input("You are on cross roadwich way you want to start with left or right: ").lower()

if way=="left":
    transportation=input("Wich transportation option do you wnat to use bus or taxi: ").lower()
    if transportation=="taxi":
        place=input("where do you want to start searching for your pet, supermarket, homes , school:" ).lower()
        if place=="school":
            print("congrats, you dog is here")
        elif place=="supermarket" or place=="homes":
             print("sorry we couldn't find you pet here , start over agin")
        else:
            print("the place you entered cannot be even an option you lose the game")
          
    elif transportation=="bus":
        print("Buses do not use this route , use another option")
    else:
        print("Invalid choice of transporation , game over")
else:
    print("Sorry this direction  is not allowed  to cross, you lose your pet , game over")



    


    
    

    






























