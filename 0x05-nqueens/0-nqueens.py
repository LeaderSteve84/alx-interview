#!/usr/bin/env python3
""""""
import sys


def print_board(board):
    """prints the board"""
    print([[i, j] for i, j in enumerate(board)])


def is_safe(board, row, col):
    """Checks if a position is safe"""
    for i in range(col):
        if board[i] == row or \
            board[i] - i == row - col or \
                board[i] + i == row + col:
            return False
    return True


def solve_nqueens(board, col):
    """Solves the N queens problem"""
    N = len(board)
    if col == N:
        print_board(board)
        return

    for i in range(N):
        if is_safe(board, i, col):
            board[col] = i
            solve_nqueens(board, col + 1)


def check_args():
    """Checks the arguments"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    return N


def main():
    """Main function"""
    N = check_args()
    board = [-1] * N
    solve_nqueens(board, 0)


if __name__ == "__main__":
    main()
