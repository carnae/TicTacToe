Gameover = 0

def wincheck():
  #i hate bruteforcing, but i cannot think of anything else
  if win[0][0] + win[0][1] + win[0][2] == 3 or win[0][0] + win[1][0] + win[2][0] == 30 or win[1][0] + win[1][1] + win[1][2] == 33 or win[2][0] + win[1][1] + win[2][2] == 63 or win[0][1] + win[1][1] + win[2][1] == 33 or win[0][2] + win[1][2] + win[2][2] == 36 or win[0][0] + win[1][1] + win[2][2] == 33 or win[2][0] + win[1][1] + win[2][2] == 33:
    print ("X wins")
    Gameover.int(1)
  elif win[0][0] + win[0][1] + win[0][2] == -6 or win[0][0] + win[1][0] + win[2][0] == -60 or win[1][0] + win[1][1] + win[1][2] == -66 or win[2][0] + win[2][1] + win[2][2] == -126 or win[0][1] + win[1][1] + win[2][1] == -66 or win[0][2] + win[1][2] + win[2][2] == -72 or win[0][0] + win[1][1] + win[2][2] == -66 or win[2][0] + win[1][1] + win[2][2] == -66:
    print ("O wins")
    Gameover.int(1)
  print (win[0])
  print (win[1])
  print (win[2])
  if draw == 9:
    print ("draw")
    Gameover.int(3)
arr = [[" "," "," "],[" "," "," "],[" "," "," "]] 
win = [[77]*3 for i in range(3)]
positions = [""]
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
        win[xRow][xCol] = pos
        print (arr[0])
        print (arr[1])
        print (arr[2])
        played = 1
        draw = draw + 1
        wincheck()
  while played == 1:
    done = 1
    oRow = int(input("enter row"))
    oCol = int(input("enter col"))
    pos = (oRow * 10) + oCol
    print (pos)
    for i in positions:
       if pos == i:
          print ("not there")
          done = 0
    if done == 1:
        positions.append(pos)
        arr[oRow][oCol] = ("O")
        win[oRow][oCol] = pos * -2
        print (arr[0])
        print (arr[1])
        print (arr[2])
        draw = draw + 1
        wincheck()
        played = 0