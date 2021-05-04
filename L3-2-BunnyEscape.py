'''
from collections import deque

class Square:
    def __init__(self, row, col, dist):
        self.row = row
        self.col = col
        self.dist = dist

    def __repr__(self):
        return "(" + str(self.row) + ", " + str(self.col) + ")"
    
    def __eq__(self, other):
        # For checking square matches
        return (self.row == other.row) and (self.col == other.col)
    
    def __hash__(self):
        # For visted set
        return hash((self.row, self.col))


def solution(map):

    # Board specs
    cols = len(map)
    rows = len(map[0])
    optimal_dist = rows + cols - 1
  

    # Typical traversal algorithm
    # Going for dfs as we have an optimal goal trying to hit
    start = Square(0, 0, 1)
    end = Square(rows-1, cols-1, 0)

    # Moves - order by right, down, left, up
    horizontal = [0, 1, -1, 0]
    vertical   = [1, 0, 0, -1]
    moves = zip(horizontal, vertical)

    # Is it valid
    def valid_square(row, col):
        return not (row < 0 or row > rows - 1 or
                    col < 0 or col > cols - 1)

    # It is blocked
    def open_square(row, col):
        return not map[row][col]

    def traverse(square, wall_removed, visited, best):
        if (best == optimal_dist) or (square.dist > best):
            return best
        
        if (square == end):
            return square.dist
        
        if square not in visited:
            visited.add(square)
            
            for horiz, vert in moves:
                row_next = square.row + vert
                col_next = square.col + horiz
                if valid_square(row_next, col_next):
                    if open_square(row_next, col_next):
                        # Move unhindered
                        square_next = Square(row_next, col_next, square.dist + 1)
                        best = min(traverse(square_next, wall_removed, visited, best), best)
                    elif not wall_removed:
                        square_next = Square(row_next, col_next, square.dist + 1)
                        # Move if haven't removed a wall yet
                        best = min(traverse(square_next, True, visited, best), best)
        return best                    

    return traverse(start, False, set(), rows*cols)
'''

from collections import deque

class Square:
    def __init__(self, row, col, dist):
        self.row = row
        self.col = col
        self.dist = dist

    def __repr__(self):
        return "(" + str(self.row) + ", " + str(self.col) + ")"
    
    def __eq__(self, other):
        # For checking square matches
        return (self.row == other.row) and (self.col == other.col)
    
    def __hash__(self):
        # For visted set
        return hash((self.row, self.col))


def solution(map):

    # Board specs
    rows, cols = len(map), len(map[0])
    optimal_dist = rows + cols - 1

    # Moves
    horizontal = [0, 1, -1, 0]
    vertical   = [1, 0, 0, -1]
    moves = zip(horizontal, vertical)

    # Is it valid
    def valid_square(row, col):
        return not (row < 0 or row > rows - 1 or
                    col < 0 or col > cols - 1)

    # It is blocked
    def blocked_square(row, col):
        return map[row][col]

    def traverse(square, wall_removed, visited, best):
        print square, wall_removed, visited
        if (best == optimal_dist) or (square.dist >= best):
            return best
        
        if (square.row == rows-1) and (square.col == cols-1):
            return square.dist

        # Is the wall blocked?
        if blocked_square(square.row, square.col):
            if wall_removed:
                return best
            wall_removed = True
        
        if square not in visited:
            visited.add(square)

            # Check all the possible moves
            for horiz, vert in moves:
                row_next = square.row + vert
                col_next = square.col + horiz
                
                if valid_square(row_next, col_next):
                    square_next = Square(row_next, col_next, square.dist + 1)
                    best = min(traverse(square_next, wall_removed, visited.copy(), best), best)
                    if best == optimal_dist:
                        break
        return best                    

    return traverse(Square(0, 0, 1), False, set(), rows*cols)



if __name__ == "__main__":
    import time
    
    grid = [[0, 1, 1, 0], # 0
            [0, 1, 0, 1], # 1 
            [1, 1, 0, 0], # 2
            [1, 1, 1, 0]] # 3
            #0  1  2  3']
    
    start = time.time()
    answer = solution(grid) # 7
    end = time.time()
    print "1."
    print "answer:", answer
    print "time:", end - start
    
    grid = [[0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0]]

    start = time.time()
    answer = solution(grid) # 11
    end = time.time()
    print "2."
    print "answer:", answer
    print "time:", end - start

    grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = time.time()
    answer = solution(grid) # 31
    end = time.time()
    print "3."
    print "answer:", answer
    print "time:", end - start

    grid = [[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1],
            [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0],
            [1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
            [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1],
            [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
            [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]]

    start = time.time()
    answer = solution(grid) # 31
    end = time.time()
    print "4."
    print "answer:", answer
    print "time:", end - start

    grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = time.time()
    answer = solution(grid) # 31
    end = time.time()
    print "5."
    print "answer:", answer
    print "time:", end - start
    

    
    
    
