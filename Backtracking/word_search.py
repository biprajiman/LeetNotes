"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"

find the starting letter position in grid and BFS until we find the word.
how to check the visited letter.
BFS will not work here since we need to backtrack and replace visited letter.
Need better way to mark visited.
"""

from collections import deque
from typing import List


def bfs(row, col, board, word):
    neighbors = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    q = deque()
    q.append((row, col, ""))
    visited = set()

    while q:
        curr_row, curr_col, curr_letter = q.popleft()
        if (curr_row, curr_col) in visited:
            continue
        visited.add((curr_row, curr_col))

        new_letter = curr_letter + board[curr_row][curr_col]
        print(new_letter)
        if new_letter == word:
            return True
        
        for neigh in neighbors:
            new_row, new_col = curr_row + neigh[0], curr_col + neigh[1]
            if 0 <= new_row < len(board) and 0<= new_col < len(board[0]):
                q.append((new_row, new_col, new_letter))
                
    return False

def dfs(row, col, board, current_pos, word):
    if 0 <= row < len(board) and 0<= col < len(board[0]):
        if current_pos == len(word):
            return True
        
        neighbors = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        if board[row][col] != word[current_pos]:
            return False
        
        curr_letter = board[row][col]
        board[row][col] = '#'
        
        result = []
        for neigh in neighbors:
            result.append(dfs(row+neigh[0], col+neigh[1], board, current_pos+1, word))
        
        
        if any(result):
            return True
        
        board[row][col] = curr_letter # back track

    return False

def word_search(board: List[List[str]], word: str) -> bool:
    """
    Word search
    """
    candidate_start_pos = []
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == word[0]:
                candidate_start_pos.append((i, j))

    for (row, col) in candidate_start_pos:
        if dfs(row, col, board, 0, word):
            return True
 
    return False

if __name__ == '__main__':
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    result = word_search(board, word)
    assert result == True, result