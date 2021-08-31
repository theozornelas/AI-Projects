from queue import PriorityQueue
import copy

"""
Completed Matrix
"""
goalMatrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

movesMatrix = [[2, 3, 2],
               [3, 4, 3],
               [2, 3, 2]]

"""
Trivial Matrix
"""
easy = [[1, 2, 0],
 [4, 5, 3],
 [7, 8, 6]]

queueSize = [] #tracks size of queue per call
nodes = 0

"""
Class for the board.
    h = heuristic
    g = history
    board = node board
"""
class boardNode:
    def __init__(self, userBoard):
        self.weight = 0
        self.h = 0
        self.g = 0

        self.board = []

        #initialize node board
        if(userBoard is not None):
            self.board = userBoard.copy()


    """
    overloading the less tha operator
    """
    def __lt__(self, other):
        selfP = self.h
        return selfP


    """
    Function to clone the board and add it to the queue
    """

    def clone(self):
        newBoard = []
        newBoard = copy.deepcopy(self.board)

        return newBoard

    """
    This function switches blank in the specified position
    """
    def swap(self, rowBlank, colBlank, rowMove, colMove):

        self.board[rowBlank][colBlank] = self.board[rowMove][colMove]
        self.board[rowMove][colMove] = 0  # put blank in new spot


    """
    Get the coordinates of the blank tile
    """
    def getBlank(self):
        for r in range(3):
            for c in range(3):
                if (self.board[r][c] == 0):
                    return r, c

    """
    Move the blank of tile
    """
    def moveBlank(self, move):

        blankRow,blankCol = self.getBlank()

        if(move == "up"):
            self.swap(self, blankRow,blankCol)

    def setBoard(self, newBoard):
        for r in range(3):
            for c in range(3):
                self.board[r][c] = newBoard[r][c]

    """
    Print the board for the user to see
    """
    def PrintBoard(self):

        boardStr = ""
        for r in range(3):
            for c in range(3):
                boardStr += str(self.board[r][c])
                boardStr += ", "
            boardStr += "\n"
        return boardStr


"""
This is the driver class for the board solver
"""
class puzzle:
    def __init__(self, board):
        self.heuristicTotal = 0
        self.manhattanTotal = 0

        self.mainPQ = PriorityQueue()

        #data structure for the tile will be an adjacency matrix
        self.board = []
        #initialize the matrix (root board)
        for i in range(3):
            self.board.append(board[i][:])

    def getBoard(self):
        retBoard = []

        retBoard = self.board

        return retBoard


    """
    Get the coordinates of the blank tile
    """
    def getBlank(self, newBoard):
        for r in range(3):
            for c in range(3):
                if(newBoard[r][c] == 0):
                    return r,c



    def getNodesMade(self, row, col):
        return movesMatrix[row][col]

    """
    Get the new children made based on the number of nodes
    def setBoard(self, newBoard)
    
    """
    def GetChildren(self, newBoard):

        childrenList = []
        blankRow, blankCol = newBoard.getBlank()

        """
        Look for blank location 
        Clone the board as added to the child
        After cloning, modify so it replects the move made
        """

        if(blankRow == 0 and blankCol == 0):
            """
            make 2 clones, one down and one right
            """

            boardDown = boardNode(newBoard.clone())
            boardRight = boardNode(newBoard.clone())

            boardDown.swap(0, 0, 1, 0)
            boardRight.swap(0, 0, 0, 1)

            childrenList.append(boardDown)
            childrenList.append(boardRight)

        if(blankRow == 0 and blankCol == 1):

            boardDown = boardNode(newBoard.clone())
            boardRight = boardNode(newBoard.clone())
            boardLeft = boardNode(newBoard.clone())

            boardDown.swap(0, 1, 1, 1)
            boardRight.swap(0, 1, 0, 2)
            boardLeft.swap(0, 1, 0, 0)

            childrenList.append(boardDown)
            childrenList.append(boardRight)
            childrenList.append(boardLeft)

        if (blankRow == 0 and blankCol == 2):
            """
            make 2 clones, one down and one right
            """

            boardDown = boardNode(newBoard.clone())
            boardLeft = boardNode(newBoard.clone())

            boardDown.swap(0, 2, 1, 2)
            boardLeft.swap(0, 2, 0, 1)

            childrenList.append(boardDown)
            childrenList.append(boardLeft)

        if (blankRow == 1 and blankCol == 0):

            boardUp = boardNode(newBoard.clone())
            boardDown = boardNode(newBoard.clone())
            boardRight = boardNode(newBoard.clone())

            boardUp.swap(1, 0, 0, 0)
            boardDown.swap(1, 0, 2, 0)
            boardRight.swap(1, 0, 1, 1)

            childrenList.append(boardUp)
            childrenList.append(boardRight)
            childrenList.append(boardDown)

        if (blankRow ==1 and blankCol == 1):

            boardUp = boardNode(newBoard.clone())
            boardDown = boardNode(newBoard.clone())
            boardRight = boardNode(newBoard.clone())
            boardLeft = boardNode(newBoard.clone())

            boardUp.swap(1, 1, 0, 1)
            boardDown.swap(1, 1, 2, 1)
            boardRight.swap(1, 1, 1, 2)
            boardLeft.swap(1, 1, 1, 0)

            childrenList.append(boardUp)
            childrenList.append(boardRight)
            childrenList.append(boardDown)
            childrenList.append(boardLeft)

        if (blankRow == 1 and blankCol == 2):

            boardUp = boardNode(newBoard.clone())
            boardDown = boardNode(newBoard.clone())
            boardLeft = boardNode(newBoard.clone())

            boardUp.swap(1, 2, 0, 2)
            boardDown.swap(1, 2, 2, 2)
            boardLeft.swap(1, 2, 1, 1)

            childrenList.append(boardUp)
            childrenList.append(boardDown)
            childrenList.append(boardLeft)

        if (blankRow == 2 and blankCol == 0):

            boardUp = boardNode(newBoard.clone())
            boardRight = boardNode(newBoard.clone())

            boardUp.swap(2, 0, 1, 0)
            boardRight.swap(2, 0, 2, 1)

            childrenList.append(boardUp)
            childrenList.append(boardRight)

        if (blankRow == 2 and blankCol == 1):

            boardUp = boardNode(newBoard.clone())
            boardRight = boardNode(newBoard.clone())
            boardLeft = boardNode(newBoard.clone())

            boardUp.swap(2, 1, 1, 1)
            boardRight.swap(2, 1, 2, 2)
            boardLeft.swap(2, 1, 2, 0)

            childrenList.append(boardUp)
            childrenList.append(boardRight)
            childrenList.append(boardLeft)

        if (blankRow == 2 and blankCol == 2):

            boardUp = boardNode(newBoard.clone())
            boardRight = boardNode(newBoard.clone())
            boardLeft = boardNode(newBoard.clone())

            boardUp.swap(2, 2, 1, 2)
            boardLeft.swap(2, 2, 2, 1)

            childrenList.append(boardUp)
            childrenList.append(boardLeft)

        for child in childrenList:
            child.g = newBoard.g + 1

        return childrenList


    """
    Get the manhattan distance
    """
    def getManhattanDistance(self,childBoard):
        manhattan = 0
        # get value of child
        # find the correct index
        # make the calculation
        for r in range(3):
            for c in range(3):
                if (childBoard.board[r][c] != goalMatrix[r][c]):
                    actualR, actualC = self.findInGrid(childBoard.board[r][c])
                    manhattan += (abs(r - actualR) + abs(c - actualC))

        return manhattan

    """
    find the correct spot in the goal matrix
    """
    def findInGrid(self,valueToFind):
        for r in range(3):
            for c in range(3):
                if(goalMatrix[r][c] == valueToFind):
                    return r,c


    """
    Get the number of misplaced tiles
    """
    def getMisplacedTiles(self, childBoard):
        matchCount = 0

        for r in range(3):
            for c in range(3):
                if (childBoard.board[r][c] != goalMatrix[r][c]):
                    matchCount += 1

        # return true or false if there were any missmatches
        return matchCount

    """
    Priority Queue Function for the search algorithm
    children is a list of child
    """
    def queueingFunctionUniformed(self, nodes, children):

        thisset = set((children))

        for child in children:

            #if child is not repeated
            if(child in thisset):
                #set the value of h
                child.h = 0
                # put(key, val)
                nodes.put((int(child.g + child.h), child))

        return nodes

    """
    Priority Queue Function for the search algorithm
    """
    def queueingFunctionMisplacedTile(self, newBoard, children):

        pq = PriorityQueue()

        for child in children:
            child.h = self.getMisplacedTiles(child)

            #put(key, val)
            pq.put((child.g + child.h, child))

        return pq

    """
    Priority Queue Function for the mahattan A* search algorithm
    """
    def queueingFunctionManhattan(self, nodes, children):

        pq = PriorityQueue()

        for child in children:
            child.h = self.getManhattanDistance(child)

            #put(key, val)
            pq.put((child.g + child.h, child))

        return pq

    """
    create the queue of states
    """
    def makeQueue(self, initialBoard):
        pq = PriorityQueue()
        pq.put((0, initialBoard))

        return pq

    """
    check if the board is equal to the desired one
    """
    def isGoalState(self, currentState):

        matchCount = 0

        for r in range(3):
            for c in range(3):
                if (currentState.board[r][c] != goalMatrix[r][c]):
                    matchCount += 1

        # return true or false if there were any missmatches
        return matchCount

    """
    This solves the puzzle using Uniformed cost algorithm
    
    refactor to this def uniformedSearch(self, newBoard, searchType):
    newBoard -- board object
    """
    def uniformedSearch(self, newBoard, searchType):

        nodes = PriorityQueue()

        nodes = self.makeQueue(newBoard)

        while(1):

            if(nodes.empty()):
                return None

            queueSize.append(nodes.qsize()) #get the sizes of the queue
            key, node = nodes.get()

            print(node.PrintBoard())

            if(self.isGoalState(node) == 0):
                return node

            """
            Here we perform the search based on the one selected by user
            """
            if(searchType == "1"):
                nodes = self.queueingFunctionUniformed(nodes, self.GetChildren(node))
            elif (searchType == "2"):
                nodes = self.queueingFunctionMisplacedTile(nodes, self.GetChildren(node))
            else:
                nodes = self.queueingFunctionManhattan(nodes, self.GetChildren(node))
