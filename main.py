from queue import PriorityQueue
from operator import itemgetter

def find_index(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))

# Manhattan distance
def manhattan_distance(initial_board, goal_board)-> int:

  distance = 0

  for i in range(3):
    for j in range(3):

      if initial_board[i][j] != '0':
        
        # Calculate Manhattan distance
        a = find_index(goal_board,initial_board[i][j])
        x_diff = abs(a[0]-i)
        y_diff = abs(a[1]-j)
        distance += x_diff + y_diff

  return distance


# Misplaced count
def count_misplaced(initial_board, goal_board)-> int:

  count = 0

  for i in range(3):
    for j in range(3):

      if initial_board[i][j] != '0':
      
        if initial_board[i][j] != goal_board[i][j]:
          count += 1

  return count

#Test statements for heuristics
#initial_board = [['1', '2', '3'], 
#                 ['0', '5', '6'],
#                 ['4', '7', '8']]

#goal_board = [['1', '2', '3'],
 #             ['4', '5', '6'],
 #             ['7', '8', '0']]

#print(manhattan_distance(initial_board, goal_board))
#print(count_misplaced(initial_board, goal_board))

def boardGood(board)->bool:
  l1=[]
  for i in range(3):
    for j in range(3):
      l1.append(board[i][j])
  if len(set(l1))<10:
    return False
  return True

def showBoard(board:list[list[int]])->None:
  for i in range(3):
    for j in range(3):
      print(board[i][j],end=" ")
    print()
  print()

def showBoards(boards:list[list[list[int]]],n:int)->None:
  for k in range(n):
    for i in range(3):
      print(boards[i][k],end=" | ")
      print(boards[i][k],end=" | ")
      print(boards[i][k],end=" | ")
      print()
    print()

#replaces empty space " ", with zero
def replaceEmptySpace(board:list[list[int]])->list[list[int]]:
  for i in range(3):
    for j in range(3):
      if str(board[i][j]).isspace():
        board[i][j]='0'
  return board

def findEmptySpace(board:list[list[int]])->list[int]:
  for i in range(3):
    for j in range(3):
      if board[i][j]=='0':
        return [i,j]
      
  raise Exception("No space left in board, made an illegal move")
  return [0,0]

def cloneBoard(board:list[list[int]])->list[list[int]]:
  newboard=[[0,0,0],[0,0,0],[0,0,0]]
  for i in range(3):
    for j in range(3):
      newboard[i][j]=board[i][j]

  return newboard

def goalTest(board:list[list[int]],goal_board:list[list[int]])->bool:
  for i in range(3):
    for j in range(3):
      if goal_board[i][j]!=board[i][j]:
        return False

  return True

def attachManhattan(boards:list[list[list[int]]],goal:list[list[int]],count:int)->list:
  d=[]

  for i in boards:
    d.append((manhattan_distance(i,goal) + count,i))
  
  return d

def attachMisplaced(boards:list[list[list[int]]],goal:list[list[int]],count:int)->list:
  d=[]

  for i in boards:
    d.append((count_misplaced(i,goal) + count,i))
  
  return d


def actionList(board,prev_boards):
  boards=[]
  x,y = findEmptySpace(board)
  c=0
  #Check if there is a legal move in the direction - up
  if x>0:
    mvUpBoard = cloneBoard(board)
    mvUpBoard[x][y] = mvUpBoard[x-1][y]
    mvUpBoard[x-1][y] = '0'

    if mvUpBoard not in prev_boards:
      c+=1
      boards.append(mvUpBoard)
  #Check if there is a legal move in the direction - left
  if y>0:
    mvleftBoard = cloneBoard(board)
    mvleftBoard[x][y] = mvleftBoard[x][y-1]
    mvleftBoard[x][y-1] = '0'
    if mvleftBoard not in prev_boards:
      c+=1
      boards.append(mvleftBoard)
  #Check if there is a legal move in the direction - right
  if y<2:
    mvrightBoard = cloneBoard(board)
    mvrightBoard[x][y] = mvrightBoard[x][y+1]
    mvrightBoard[x][y+1] = '0'
    if mvrightBoard not in prev_boards:
      c+=1
      boards.append(mvrightBoard)
  #Check if there is a legal move in the direction - down
  if x<2:
    mvdownBoard = cloneBoard(board)
    mvdownBoard[x][y] = mvdownBoard[x+1][y]
    mvdownBoard[x+1][y] = '0'
    if mvdownBoard not in prev_boards:
      c+=1
      boards.append(mvdownBoard)


  return (boards,c)

def aStarSearchManhattan(initial_board, goal_board)->list:
  path = []
  fringe=[]
  visited=[]
  count=0
  generated=0
  #(f(n),g(n),h(n),node)
  fringe.append((0,0,0,initial_board))
  min_heu=999999
  while len(fringe)>0:
    node=fringe.pop(0)
    curr_g=node[1]
    curr_board=node[3]


    visited.append(curr_board)

    if goalTest(curr_board,goal_board):
      print("Nodes expanded: ", count+1)
      print("Nodes generated: ", generated+1)
      print("cost",curr_g)
      path.append(curr_board)
      return path
    
    prospectiveBoards = actionList(curr_board,visited)
    generated+=prospectiveBoards[1]
    d = attachManhattan(prospectiveBoards[0],goal_board,curr_g+1)
    #updating the fringe, if board/node already exists, check if we have a better heuristic to update it in the frontier
    for key in d:
      if key[1] in visited:
        continue
      else:
        fringe.append((key[0],curr_g+1,0,key[1]))
    fringe.sort(key=itemgetter(0))
    path.append(curr_board)
    count+=1
  print("No solution found")
  print("Nodes expanded: ", count+1)
  print("Nodes generated: ", generated+1)
  return path


def aStarSearchMisplaced(initial_board, goal_board)->list:
  path = []
  fringe=[]
  visited=[]
  count=0
  generated=0
  #(f(n),g(n),h(n),node)
  fringe.append((0,0,0,initial_board))
  min_heu=999999
  while len(fringe)>0:
    node=fringe.pop(0)
    curr_g=node[1]
    curr_board=node[3]

    visited.append(curr_board)

    if goalTest(curr_board,goal_board):
      print("Nodes expanded: ", count+1)
      print("Nodes generated: ", generated+1)
      print("cost",curr_g)
      path.append(curr_board)
      return path
    
    prospectiveBoards = actionList(curr_board,visited)
    generated+=prospectiveBoards[1]
    d = attachMisplaced(prospectiveBoards[0],goal_board,curr_g+1)
    #updating the fringe, if board/node already exists, check if we have a better heuristic to update it in the frontier
    for key in d:
      if key[1] in visited:
        continue
      else:
        fringe.append((key[0],curr_g+1,0,key[1]))
    fringe.sort(key=itemgetter(0))
    path.append(curr_board)
    count+=1
  print("No solution found")
  print("Nodes expanded: ", count+1)
  print("Nodes generated: ", generated+1)
  return path


print("###### Welcome to 8 Puzzle Solver ######")
while(1):
  # Input for the initial state
  print(f"Enter Initial State Board.")
  init_board = []
  for i in range(3):
          row = list(map(str,input().split()))
          if len(row) != 3:
              print("Invalid input. Enter 3 elements for each row.")
          init_board.append(row)

  # Input for the goal state
  print(f"Enter Goal State Board.")
  goal = []
  for i in range(3):
          row = list(map(str,input().split()))
          if len(row) != 3:
              print("Invalid input. Enter 3 elements for each row.")
          goal.append(row)


  init_board=replaceEmptySpace(init_board)
  goal=replaceEmptySpace(goal)
  print("Misplaced")
  print(aStarSearchMisplaced(init_board,goal))


  print("Manhattan")

  print(aStarSearchManhattan(init_board,goal))
