print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

step1 = input('Oh no! You\'ve come across a fork in the road. Be careful, making the wrong choice could be deadly! Do you want to go Left or Right? \n').lower()
if step1 =="left":
  print('Phew! That was close!')
  step2 = input('Now you\'ve come to a lake. There is an island in the middle of the lake. Do you want to wait for a boat or swim across? \n').lower()
  if step2 == "wait":
    print('Good choice!')
    step3 = input('What\'s that ahead? Looks like a spooky house! There are three doors to choose from - red, blue or yellow. Which one do you choose? \n').lower()
    if step3 =="red":
     print('Ah! It\'s a room full of fire! Game Over.')
    elif step3 =="yellow":
      print('Yay! You found the treasure! Great Job, treaure hunter!')
    elif step3 =="blue":
      print('Oh no! You entered a room full of hungry beasts! Game Over.')
    else:
      print('You chose a door that doesn\'t exist. Game Over.')
  else:
    print('You were attacked by an alligator! Game Over.')
else:
  print('Oops! You fell into a hole. Game Over.')
