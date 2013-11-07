#! /usr/bin/python

# Written by Moshe Kaplan
# Designed to run in Python 2.7

import time


def create_board(n):
    """Set up the problem on an n x n chessboard

    Each queen can only be on a single square in a column. As such, instead of
    storing a full n x n representation of a board, we can make our life easier
    by only creating a single list, where each entry represents a column and
    the value represents which row the queen was placed on."""
    board = [0]*n
    return board


def is_valid_state(board, n=None):
    """Check if the board is currently in a state that can ultimately lead to a
    solution. Only checks the first 'n' columns"""
    if n is None:
        n = len(board)

    # Check if any of the first 'n' queens are able to attack each other
    for first_queen in range(n):
        for other_queen in range(first_queen+1, n):
            attack_horizontally = board[first_queen] == board[other_queen]
            attack_diagonally = abs(board[other_queen] - board[first_queen]) == (other_queen - first_queen)
            if attack_horizontally or attack_diagonally:
                return False
    return True


def solve_without_backtracking(board, n=0, solns=None):
    """Find every possible solution to the nqueens problem"""
    if solns is None:
        solns = []

    if n < len(board):
        for i in xrange(len(board)):
            board[n] = i
            solns = solve_without_backtracking(board, n+1, solns)
        return solns
    elif is_valid_state(board):
        # A solution was found
        return solns + [board[:]]
    else:
        return solns


def solve_with_backtracking(board, n=0, solns=None):
    """Find every possible solution to the nqueens problem"""
    if solns is None:
        solns = []

    if n < len(board):
        for i in xrange(len(board)):
            board[n] = i
            # The only difference between the two functions: An extra check
            if is_valid_state(board, n):
                solns = solve_with_backtracking(board, n+1, solns)
        return solns
    elif is_valid_state(board):
        # A solution was found
        return solns + [board[:]]
    else:
        return solns


def prettyprint_board(board):
    board_len = len(board)
    print "  " + "*"*(board_len * 2 - 1)
    for row in range(board_len):
        print "*|" + "".join(["Q|" if j == row else " |" for j in board]) + "*"
        print "*|" + "-"*(board_len * 2 - 1) + "|*"
    print "  " + "*"*(board_len * 2 - 1)


def main():
    print "Running the backtracking and non-backtracing implementations"
    for i in range(10,20):
        print
        print(str(i) + " Queens")

#         board = create_board(i)
#         start = time.clock()
#         solve_without_backtracking(board)
#         end = time.clock()
#         print("Without backtracking: " + str(end-start))

        board = create_board(i)
        start = time.clock()
        solns = solve_with_backtracking(board)
        end = time.clock()
        print("With backtracking:    " + str(end-start) )
        print "%d solutions:" % len(solns)
#         for soln in solve_with_backtracking(board):
#             print soln
#             prettyprint_board(soln)
#             print


if __name__ == "__main__":
    main()