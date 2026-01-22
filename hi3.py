# We will have 3 doors: 1 door is the winner
# The contestant picks one door, then the host opens a different door
#The contestant should change their potion
#We reveal if the contestant has the right door

import random

winning_Door = random.randint(1,3)
contestChoice = random.randint(1,3)

print("winner: + str(winningDoor) + "; Contestant Choice:"+ str(contestChoice)
