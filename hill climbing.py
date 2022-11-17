from copy import deepcopy
import random


def printBoard(board):
 for i in range(board_size):
 for j in range(board_size):
 print(board[i][j], end=" ")
 print()


def placeQueens(board):
 i = 0
 while i < board_size:
 row = random.randint(0, board_size - 1)
 if board[row][i] != "Q":
 board[row][i] = "Q"
 i += 1


def getQueens(board):
 queen_positions = []
 for i in range(board_size):
 for j in range(board_size):
 if board[i][j] == "Q":
 temp = i, j
 queen_positions.append(temp)
 return queen_positions


def objective_function(board):
 positions = getQueens(board)
 attacking_queens = 0
 count = 0
 for i in range(0, len(positions)):
 current_queen = positions[i]
 for j in range(0, len(positions)):
 count += 1
 if i != j:
 other_queen = positions[j]
 if other_queen[0] == current_queen[0]:
 attacking_queens += 1

 otherx = other_queen[0]
 othery = other_queen[1]
 x = deepcopy(current_queen[0])
 y = deepcopy(current_queen[1])
 while x >= 0 and y >= 0:
 x -= 1
 y -= 1
 if x == otherx and y == othery:
 attacking_queens += 1
 x = deepcopy(current_queen[0])
 y = deepcopy(current_queen[1])
 while x < board_size and y < board_size:
 x += 1
 y += 1
 if x == otherx and y == othery:
 attacking_queens += 1
 x = deepcopy(current_queen[0])
 y = deepcopy(current_queen[1])
 while x < board_size and y >= 0:
 x += 1
 y -= 1
 if x == otherx and y == othery:
 attacking_queens += 1
 x = deepcopy(current_queen[0])
 y = deepcopy(current_queen[1])
 while x >= 0 and y < board_size:
 x -= 1
 y += 1
 if x == otherx and y == othery:
 attacking_queens += 1
 return (int)(attacking_queens / 2)


def expandBoard(board, queen_position):
 boards = []

 for i in range(len(queen_position)):
 x = deepcopy(queen_position[i][0])
 y = deepcopy(queen_position[i][1])
 for j in range(board_size):
 if x != j:
 b = deepcopy(board)
 b[x][y] = "*"
 b[j][y] = "Q"
 boards.append(b)
 return boards


def minBoard(boards):
 boards.sort(key=objective_function)
 return boards[0]


def hillClimbing(board):
 moves = 0
 while True:
 moves += 1
 queen_position = getQueens(board)
 heuristic = objective_function(board)
 boards = expandBoard(board, queen_position)
 minimum = minBoard(boards)
 minimum_atacking_queens = objective_function(minimum)
 if minimum_atacking_queens >= heuristic:
 return board, moves, heuristic
 elif minimum_atacking_queens == 0:
 return minimum, moves, minimum_atacking_queens
 else:
 board = minimum


def main():
 global board_size
 board_size = int(input("Enter the board size:"))
 rows, cols = (board_size, board_size)
 board = []

 for i in range(rows):
 col = []
 for j in range(cols):
 col.append("*")
 board.append(col)
 print()
 print("Initial Board after randomization = ")
 print()
 placeQueens(board)
 printBoard(board)
 print()
 print()
 print("  # HILL CLIMBING ALGORITHM
# ")
 result, moves, h=hillClimbing(board)
 print()
 print("The BEST possible solution is = ")
 print()
 printBoard(result)
 print()
 print("The number of attacking queens in this combination are = ", h)
 print()
 print("The total number of moves (cost) is = ", moves)
if __name__ == "__main__":
 main()
