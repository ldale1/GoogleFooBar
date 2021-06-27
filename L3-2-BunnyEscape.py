## You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander
## Lambda's bunny prisoners, but once they're free of the prison blocks, the bunnies are going
## to need to escape Lambda's space station via the escape pods as quickly as possible.
## Unfortunately, the halls of the space station are a maze of corridors and dead ends that
## will be a deathtrap for the escaping bunnies. Fortunately, Commander Lambda has put you in
## charge of a remodeling project that will give you the opportunity to make things a little
## easier for the bunnies. Unfortunately(again), you can't just remove all obstacles between
## the bunnies and the escape pods - at most you can remove one wall per escape pod path, both
## to maintain structural integrity of the station and to avoid arousing Commander Lambda's
## suspicions.
##
## You have maps of parts of the space station, each starting at a prison exit and ending at
## the door to an escape pod. The map is represented as a matrix of 0sand 1s, where 0s are
## passable space and 1s are impassable walls. The door out of the prison is at the top left
## (0,0) and the door into an escape pod is at the bottom right (w-1,h-1).
##
## Write a function answer(map) that generates the length of the shortest path from the prison
## door to the escape pod, where you are allowed to remove one wall as part of your remodeling
## plans. The path length is the total number of nodes you pass through, counting both the
## entrance and exit nodes. The starting and ending positions are always passable (0). The map
## will always be solvable, though you may or may not need to remove a wall. The height and
## width of the map can be from 2 to 20. Moves can only be made in cardinal directions; no
## diagonal moves are allowed.

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

    
    
