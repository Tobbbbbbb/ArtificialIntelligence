"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    #raise NotImplementedError
    turn = 0
    for i in range(3):
        for j in range(3):
            if board[i][j]==X:
                turn+=1
            elif board[i][j]==O:
                turn-=1
    if turn==0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    #raise NotImplementedError
    actionList = []
    for i in range(3):
        for j in range(3):
            if board[i][j]==None:
                actionList.append((i,j))
    return actionList


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #raise NotImplementedError
    if board[action[0]][action[1]] != None:
        raise IndexError
    cop = copy.deepcopy(board)
    cop[action[0]][action[1]] = player(cop)
    return cop


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == X and board[0][1] == X and board[0][2] == X:
        return X
    elif board[1][0] == X and board[1][1] == X and board[1][2] == X:
        return X
    elif board[2][0] == X and board[2][1] == X and board[2][2] == X:
        return X
    elif board[0][0] == X and board[1][0] == X and board[2][0] == X:
        return X
    elif board[0][1] == X and board[1][1] == X and board[2][1] == X:
        return X
    elif board[0][2] == X and board[1][2] == X and board[2][2] == X:
        return X
    elif board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    elif board[2][0] == X and board[1][1] == X and board[0][2] == X:
        return X

    if board[0][0] == O and board[0][1] == O and board[0][2] == O:
        return O
    elif board[1][0] == O and board[1][1] == O and board[1][2] == O:
        return O
    elif board[2][0] == O and board[2][1] == O and board[2][2] == O:
        return O
    elif board[0][0] == O and board[1][0] == O and board[2][0] == O:
        return O
    elif board[0][1] == O and board[1][1] == O and board[2][1] == O:
        return O
    elif board[0][2] == O and board[1][2] == O and board[2][2] == O:
        return O
    elif board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    elif board[2][0] == O and board[1][1] == O and board[0][2] == O:
        return O

    return None
    #raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if(winner(board) != None):
        return True
    
    for i in range(3):
        for j in range(3):
            if(board[i][j]==None):
                return False
    return True

    #raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if(winner(board)==X):
        return 1
    elif(winner(board)==O):
        return -1
    else:
        return 0
    #raise NotImplementedError


class Node():
    def __init__(self, state, parent, result, action):
        self.state = state
        self.parent = parent
        self.result = result
        self.action = action

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #raise NotImplementedError

    if terminal(board):
        return None

    #if O, then we min
    #if X, then we max
    playr = player(board)

    root = Node(board, None, 0, None)
    if(playr==X):
        return max(root).action
    if(playr==O):
        return min(root).action
    

def min(node):
    nodeList = []
    for action in actions(node.state):
        temp = result(node.state, action)
        nod = None
        if(terminal(temp)):
            nod = Node(temp, node, utility(temp), action)
            if(nod.result==-1):
                return nod
        else:
            nod = Node(temp, node, 0, action)
            nod.result = max(nod).result
        nodeList.append(nod)
    minResult = nodeList[0].result
    minNode = nodeList[0]
    for n in nodeList:
        if(n.result < minResult):
            minResult = n.result
            minNode = n
    return minNode

def max(node):
    nodeList = []
    for action in actions(node.state):
        temp = result(node.state, action)
        nod = None
        if(terminal(temp)):
            nod = Node(temp, node, utility(temp), action)
            if(nod.result==1):
                return nod
        else:
            nod = Node(temp, node, -2, action)
            nod.result = min(nod).result
        nodeList.append(nod)
    maxResult = nodeList[0].result
    maxNode = nodeList[0]
    for n in nodeList:
        if(n.result > maxResult):
            maxResult = n.result
            maxNode = n
    return maxNode
    