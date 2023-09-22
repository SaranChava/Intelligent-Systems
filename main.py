from queue import PriorityQueue

# Manhattan distance
def manhattan_distance(initial_board, goal_board)-> int:

  distance = 0

  for i in range(3):
    for j in range(3):

      if initial_board[i][j] != '0':
        
        # Calculate Manhattan distance
        print(goal_board[i],initial_board[i][j])
        x_diff=abs()
        x_diff = abs(j - goal_board[i].index(initial_board[i][j]))  
        y_diff = abs(i - initial_board.index(initial_board[i]))
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
#initial_board = [[1, 2, 3], [4, 5, 6],[0, 7, 8]]

#goal_board = [[1, 2, 3],[4, 5, 6],[7, 8, 0]]

#print(manhattan_distance(initial_board, goal_board))
#print(count_misplaced(initial_board, goal_board))
def boardGood(board)->bool:
  l=['1','2','3','4','5','6','7','8','9','0']
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
      if str(board[i][j]).isspace() or board[i][j]=='0':
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
    showBoard(i)
    print("goal",end=" ")
    showBoard(goal)
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

  #Check if there is a legal move in the direction - up
  if x>0:
    mvUpBoard = cloneBoard(board)
    mvUpBoard[x][y] = mvUpBoard[x-1][y]
    mvUpBoard[x-1][y] = '0'

    if mvUpBoard not in prev_boards:
      boards.append(mvUpBoard)
  #Check if there is a legal move in the direction - left
  if y>0:
    mvleftBoard = cloneBoard(board)
    mvleftBoard[x][y] = mvleftBoard[x][y-1]
    mvleftBoard[x][y-1] = '0'
    if mvleftBoard not in prev_boards:
      boards.append(mvleftBoard)
  #Check if there is a legal move in the direction - right
  if y<2:
    mvrightBoard = cloneBoard(board)
    mvrightBoard[x][y] = mvrightBoard[x][y+1]
    mvrightBoard[x][y+1] = '0'
    if mvrightBoard not in prev_boards:
      boards.append(mvrightBoard)
  #Check if there is a legal move in the direction - down
  if x<2:
    mvdownBoard = cloneBoard(board)
    mvdownBoard[x][y] = mvdownBoard[x+1][y]
    mvdownBoard[x+1][y] = '0'
    if mvdownBoard not in prev_boards:
      boards.append(mvdownBoard)

  return boards

def aStarSearchManhattan(initial_board, goal_board)->dict:
  path = {}
  fringe=[]
  visited=[]
  count=0
  fringe = PriorityQueue()
  fringe.put((0,initial_board))
  while not fringe.empty():
    curr_board=fringe.get_nowait()[1]
    visited.append(curr_board)
    if goalTest(curr_board,goal_board):
      return path
    prospectiveBoards = actionList(curr_board,visited)
    d = attachManhattan(prospectiveBoards,goal_board,count+1)

    #updating the fringe, if board/node already exists, check if we have a better heuristic to update it in the frontier
    for key in d:
      if any(key in item for item in fringe.queue):
        while not (fringe.empty()):
          curr=fringe.get_nowait()
          if key not in curr:
            fringe.put_nowait(curr)
      else:
        fringe.put((d[key],key))
    path[curr_board]=count
    count+=1
  return path


def aStarSearchMisplaced(initial_board, goal_board)->list:
  path = []
  fringe=[]
  visited=[]
  count=0
  fringe = PriorityQueue()
  fringe.put((0,initial_board))
  while not fringe.empty():
    curr_board=fringe.get_nowait()[1]
    if curr_board in visited:
      pass
    if not boardGood:
      raise Exception(" Bad board")

    visited.append(curr_board)
    if goalTest(curr_board,goal_board):
      path.append((curr_board,count))
      return path
    prospectiveBoards = actionList(curr_board,visited)
    d = attachMisplaced(prospectiveBoards,goal_board,count+1)
    #updating the fringe, if board/node already exists, check if we have a better heuristic to update it in the frontier
    for key in d:
      fringe.put(key)
    path.append((curr_board,count))
    count+=1
  return path


initial_boards = [[['1', '2', '3'], ['4', '5', '6'],[' ', '7', '8']],[['2','8','1'],['3','4','6'],['7','5','0']],[['7','2','4'],['5','0','6'],['8','3','6']],[['1','2','3'],['7','4','5'],['6','8','0']]]

goal_boards = [[['1', '2', '3'],['4', '5', '6'],['7', '8', '0']],[['3','2','1'],['8','0','4'],['7','5','6']],[['1','2','3'],['4','5','6'],['7','8','0']],[['1','2','3'],['8','6','4'],['7','5','0']]]


for i in range(4):
  initial_board = replaceEmptySpace(initial_boards[i])
  goal_board = replaceEmptySpace(goal_boards[i])
  print(aStarSearchMisplaced(initial_board,goal_board))