from random import randint
t = ["Rock", "Paper", "Scissors"]

computer = t[randint(0,2)]

player = False

while player == False:
  player = input("Rock, Paper, Scissors? ")
  if player == computer:
    print("It's a tie")
  elif player == "Rock":
    if computer == "Paper":
      print("You loose", computer, "beats",player)
    else:
      print("You win!!!",player, "beats",computer)
  elif player == "Paper":
    if computer == "Scissors":
      print("you lose",computer, "cuts",player)
    else:
      print("you win!!!",player,"beats", computer)
  elif player == "Scissors":
    if computer == "Rock":
      print("You loose",computer, "beats", player)
    else:
      print("You win!!!", player, "beats",computer) 
  else:
    print("That's not an option")
  if player == "Rock" or "Paper" or "Scissors":
      computer = t[randint(0,2)]
      player = False
  else:
    player = True