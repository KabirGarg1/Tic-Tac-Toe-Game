import random
players = ['h','h']
symbols = ['X','O']
h=0
def askname():
   global Choose
   global players
   global gamemode
   gamemode = int(input('Press 0 for singleplayer and 1 for multiplayer'))
   if gamemode == 1:
     players[0] = input('Player 1 (symbol X):')
     players[1] = input('Player 2 (symbol O):')
   else:
     Choose = int(input('Press 0 to play with \'X\'symbol OR 1 to play with \'O\' symbol: '))
     players[Choose] = input('Enter Player name:')
     players[Choose-1] = 'Computer'
   global toss
   toss = random.randint(0,1)
   print(players[toss],'won the Toss and so will get the first turn',toss)
   board()

boardlist = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
def board():
   for i in range(3):
     for j in range(3):
       print('|',boardlist[i][j],end='')
     print('|')
     print('|__|__|__|')
   print()

def Computermove_inside(symbolcheck,symbolprint):
    global gs
    global x
    global movesequence
    x = 0
    gs=0
    for i in range(3):
      if boardlist[i].count(symbolcheck) == 2:
        for j in range(3):
          if boardlist[i][j] == ' ':
            movesequence = 1
            boardlist[i][j] = symbolprint
            board()
            return movesequence


    if movesequence==0:
      for i in range(3):
         gs = 0
         for j in range(3):
            if boardlist[j][i] == symbolcheck:
               gs+=1
         if gs == 2:
            break
         if boardlist[i][i] == symbolcheck:
            x+=1
         if x == 2:
           break
    if x==2:
      for i in range(3):
        if boardlist[i][i] == ' ':
          movesequence = 1
          boardlist[i][i] =  symbolprint
          board()
          return movesequence
          pass

    if gs==2:
        print('IN G ===2')
        for j in range(3):
          if boardlist[j][i] == ' ':
            movesequence = 1
            boardlist[j][i] = symbolprint
            board()
            return movesequence
            pass

    x =0
    for i in range(2,-1,-1):
        if boardlist[abs(i-2)][i] == symbolcheck:
          x+=1
    if x==2:
      for i in range(2,-1,-1):
          if boardlist[abs(i-2)][i] == ' ':
            movesequence = 1
            boardlist[i][i] = symbolprint
            board()
            return movesequence
            pass

random_row = 0
random_column = 0
def Computermove():
  global random_row
  global random_column
  global movesequence
  movesequence = 0
  x = 0
  Computermove_inside(symbols[Cturn],symbols[Cturn])
  x = 0
  gs = 0
  if movesequence == 0:
      Computermove_inside(symbols[Cturn-1],symbols[Cturn])
  if movesequence == 0:
    while True:
      random_row = random.randint(0,2)
      random_column = random.randint(0,2)
      if boardlist[random_row][random_column] == ' ':
        boardlist[random_row][random_column] = symbols[Cturn]
        board()
        return
        break
      else:
        print('Choose cell is already filled,fill again')


Cturn=0
a=0
b=0
pointsP2 = 0
pointsP1 = 0
condition = 0
def turn():
  global Cturn
  global continue1
  global pointsP1
  global pointsP2
  for p in range(1,10):
    if h == 0:
      if p%2 ==0:
        Cturn = toss-1
      else:
        Cturn = toss
      while True:
        condition = 0
        if gamemode == 0 and symbols[Cturn] != symbols[Choose]:
          Computermove()
          checkresult()
          break
        else:
          condition = 1
          a = int(input('Enter row number:'))-1
          b = int(input('Enter column number:'))-1
        if (0<=a<=2) and (0<=b<=2) and (boardlist[a][b] == ' ') and (condition == 1):
            boardlist[a][b] = symbols[Cturn]
            board()
            checkresult()
            break
        else:
            print('That cell is already filled...fill again')
    else:
      if Cturn == 0:
         pointsP1+=1
      elif Cturn == 1:
         pointsP2+=1
      continue1 = int(input('Enter 0 to exit OR 1 to continue playing:'))
      break


def checkresult():
  global h
  for i in range(3):
    if boardlist[i].count(symbols[Cturn]) == 3:
      h=1
      print(result[Cturn])
      break
    elif (boardlist[0][i]== symbols[Cturn]) and (boardlist[1][i]== symbols[Cturn]) and (boardlist[2][i] == symbols[Cturn]):
      h=1
      print(result[Cturn])
      break
  if (boardlist[0][0]== symbols[Cturn]) and (boardlist[1][1] == symbols[Cturn]) and (boardlist[2][2] == symbols[Cturn]):
      h=1
      print(result[Cturn])
  elif (boardlist[0][2] == symbols[Cturn])and (boardlist[1][1] == symbols[Cturn])and (boardlist[2][0] == symbols[Cturn]):
      h=1
      print(result[Cturn])
  elif (boardlist[0].count(' ')==0) and (boardlist[1].count(' ')==0) and (boardlist[2].count(' ') ==0):
      h=1
      print(result[2])


def pointstable():
  dict1 = {players[0]:pointsP1,players[1]:pointsP2}
  for x,y in dict1.items():
    print(x,'is at ',y,'points')


def cleanboard():
  for i in range(3):
    for j in range(3):
      boardlist[i][j]= ' '



askname()
result = [players[0]+' wins',players[1] +' wins','Draw']
turn()
while True:
  movesequence = 0
  if continue1 == 0:
    pointstable()
    break
  elif continue1 == 1:
    h=0
    pointstable()
    cleanboard()
    board()
    if toss == 0:
      toss +=1
    else:
      toss -=1
    turn()
  else:
    print('Wrong Input...Enter again')
