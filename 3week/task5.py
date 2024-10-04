"""
https://leetcode.com/problem-list/array/?difficulty=MEDIUM
URL: https://leetcode.com/problems/game-of-life/?envType=problem-list-v2&envId=array&difficulty=MEDIUM
"""

from typing import List


class Solution:
    WILL_DIE = -1  # Клетка была жива, но умрет
    WILL_LIVE = 2  # Клетка была мертва, но оживет

    def gameOfLife(self, board: List[List[int]]) -> None:
        n = len(board)
        m = len(board[0])

        def cnt_neighbors(y, x) -> int:
            cnt = 0
            for i in range(y - 1, y + 2):
                for j in range(x - 1, x + 2):
                    if (i == y and j == x) or i < 0 or i >= n or j < 0 or j >= m:
                        continue
                    elif board[i][j] in [self.WILL_DIE, 1]:
                        cnt += 1
            return cnt

        for i in range(n):
            for j in range(m):
                live_neighbors = cnt_neighbors(i, j)
                if board[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = self.WILL_DIE
                elif board[i][j] == 0:
                    if live_neighbors == 3:
                        board[i][j] = self.WILL_LIVE

        for i in range(n):
            for j in range(m):
                if board[i][j] == self.WILL_DIE:
                    board[i][j] = 0
                elif board[i][j] == self.WILL_LIVE:
                    board[i][j] = 1


board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
Solution().gameOfLife(board)
for row in board:
    print(row)
