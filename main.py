Gameover = 0
def wincheck():
  for Row1 in range(0,3):
    conseq = 0
    for Col1 in range(0,3):
      if arr[Row1][Col1] == player:
        conseq = conseq + 1
        if conseq == 3:
          print (player,"wins!")
          Gameover.int(3)
  for Col1 in range(0,3):
    conseq = 0
    for Row1 in range(0,3):
      if arr[Row1][Col1] == player:
        conseq = conseq + 1
        if conseq == 3:
          return (player,"wins!")
          Gameover.int(3)
  conseq = 0
  for temp in range(0,3):
    if arr[temp][temp] == player:
      conseq = conseq + 1
      if conseq == 3:
        print (player,"wins!")
        Gameover.int(3)
  temp1 = 2
  conseq = 0
  for temp in range(0,3):
    if arr[temp][temp1] == player:
      conseq = conseq + 1
      temp1 = temp1 - 1
      if conseq == 3:
        print (player,"wins!")
        Gameover.int(3)
  if draw == 9:
    print ("draw")
    Gameover.int(3)
def display():
  print (arr[0])
  print (arr[1])
  print (arr[2])
arr = [[" "," "," "],[" "," "," "],[" "," "," "]] 
positions = [""]
player = ""
played = 0
draw = 0
pos = 0
done = 0
i = 0
while Gameover != 1:
  while played == 0:
    done = 1
    xRow = int(input("enter row"))
    xCol = int(input("enter col"))
    pos = (xRow * 10) + xCol
    for i in positions:
       if pos == i:
          print ("not there")
          done = 0
    if done == 1:
        positions.append(pos)
        arr[xRow][xCol] = ("X")
        display()
        played = 1
        draw = draw + 1
        player = "X"
        wincheck()
  while played == 1:
    done = 1
    oRow = int(input("enter row"))
    oCol = int(input("enter col"))
    pos = (oRow * 10) + oCol
    for i in positions:
       if pos == i:
          print ("not there")
          done = 0
    if done == 1:
        positions.append(pos)
        arr[oRow][oCol] = ("O")
        display()
        draw = draw + 1
        player = "O"
        wincheck()
        played = 0