# Manhattan distance
def manhattan_distance(initial_board, goal_board):

  distance = 0

  for i in range(3):
    for j in range(3):

      if initial_board[i][j] != 0 and initial_board[i][j] != None:
        
        # Calculate Manhattan distance
        x_diff = abs(j - goal_board[i].index(initial_board[i][j]))  
        y_diff = abs(i - initial_board.index(initial_board[i]))
        distance += x_diff + y_diff

  return distance


# Misplaced count
def count_misplaced(initial_board, goal_board):

  count = 0

  for i in range(3):
    for j in range(3):

      if initial_board[i][j] != 0 and initial_board[i][j] != None:
      
        if initial_board[i][j] != goal_board[i][j]:
          count += 1

  return count

#Test statements for heuristics
#initial_board = [[1, 2, 3], [4, 5, 6],[0, 7, 8]]

#goal_board = [[1, 2, 3],[4, 5, 6],[7, 8, 0]]

#print(manhattan_distance(initial_board, goal_board))
#print(count_misplaced(initial_board, goal_board))

