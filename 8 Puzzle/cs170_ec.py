from Graph import puzzle
from Graph import boardNode
from Graph import queueSize

trivial = [[1, 2, 3],
 [4, 5, 6],
 [7, 8, 0]]
beginner = [[1, 2, 3],
 [4, 5, 6],
 [7, 0, 8]]
easy = [[1, 2, 0],
 [4, 5, 3],
 [7, 8, 6]]
medium = [[0, 1, 2],
 [4, 5, 3],
 [7, 8, 6]]
hard = [[8, 7, 1],
 [6, 0, 2],
 [5, 4, 3]]
veteran = [[1, 2, 3],
 [4, 5, 6],
 [8, 7, 0]]
goal_state = [[1, 2, 3],
 [4, 5, 6],
 [7, 8, 0]]

def init_default_puzzle_mode():
 selected_difficulty = input("You wish to use a default puzzle. Please enter a desired difficulty on a scale from 0 to 5." + '\n')
 if selected_difficulty == "0":
    print("Difficulty of 'Trivial' selected.")
    return trivial
 if selected_difficulty == "1":
    print("Difficulty of 'beginner' selected.")
    return beginner
 if selected_difficulty == "2":
    print("Difficulty of 'Easy' selected.")
    return easy
 if selected_difficulty == "3":
    print("Difficulty of 'medium' selected.")
    return medium
 if selected_difficulty == "4":
    print("Difficulty of 'hard' selected.")
    return hard
 if selected_difficulty == "5":
    print("Difficulty of 'veteran' selected.")
    return veteran

def print_puzzle(puzzle):
 for i in range(0, 3):
    print(puzzle[i])
 print('\n')

def getQueueSum():
   sumAll = 0

   for num in queueSize:
     sumAll += num

   return sumAll


def select_and_init_algorithm(boardToSolve):

 algorithm = input("Select algorithm. (1) for Uniform Cost Search, (2) for the Misplaced Tile Heuristic, "
 "or (3) the Manhattan Distance Heuristic." + '\n')


 solution = puzzle(boardToSolve)
 solveNode = boardNode(boardToSolve)

 if(algorithm == "1"):

     #passes in a board into the function
     solutionNode = solution.uniformedSearch(solveNode, algorithm)

     print("finished solving uniformed search\n")
     print("It took " + str(solutionNode.g) + " levels\n")
     print("Number of Nodes Expanded: " + str(getQueueSum()-1) + "\n")
     queueSize.sort()
     print("Max queue size was " + str(queueSize[len(queueSize)-1]) + " nodes\n")

 elif (algorithm == "2"):

     solutionNode = solution.uniformedSearch(solveNode, algorithm)
     print("finished solving Heuristic Tile search\n")
     print("It took " + str(solutionNode.g) + " levels\n")
     print("Number of Nodes Expanded: " + str(getQueueSum() - 1) + "\n")
     queueSize.sort()
     print("Max queue size was " + str(queueSize[len(queueSize) - 1]) + " nodes\n")
 else:
     solutionNode = solution.uniformedSearch(solveNode, algorithm)
     print("finished solving Manhattan Distance search\n")
     print("It took " + str(solutionNode.g) + " levels\n")
     print("Number of Nodes Expanded: " + str(getQueueSum() - 1) + "\n")
     queueSize.sort()
     print("Max queue size was " + str(queueSize[len(queueSize) - 1]) + " nodes\n")



"""
Here main Starts
"""

puzzle_mode = input("Welcome to an 8-Puzzle Solver. Type '1' to use a default puzzle, or '2' to create your own."+ '\n')

if puzzle_mode == "1":

    select_and_init_algorithm(init_default_puzzle_mode())
if puzzle_mode == "2":
    print("Enter your puzzle, using a zero to represent the blank. " +
    "Please only enter valid 8-puzzles. Enter the puzzle demilimiting " +
    "the numbers with a space. RET only when finished." + '\n')
    puzzle_row_one = input("Enter the first row: ")
    puzzle_row_two = input("Enter the second row: ")
    puzzle_row_three = input("Enter the third row: ")
    puzzle_row_one = puzzle_row_one.split()
    puzzle_row_two = puzzle_row_two.split()
    puzzle_row_three = puzzle_row_three.split()
    for i in range(0, 3):
        puzzle_row_one[i] = int(puzzle_row_one[i])
        puzzle_row_two[i] = int(puzzle_row_two[i])
        puzzle_row_three[i] = int(puzzle_row_three[i])
    user_puzzle = [puzzle_row_one, puzzle_row_two, puzzle_row_three]
    select_and_init_algorithm(user_puzzle)
