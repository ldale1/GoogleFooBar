## As a henchman on Commander Lambda's space station, you're expected to be resourceful,
## smart, and a quick thinker. It's not easy building a doomsday device and capturing bunnies
## at the same time, after all! In order to make sure that everyone working for her is
## sufficiently quick-witted, Commander Lambda has installed new flooring outside the
## henchman dormitories. It looks like a chessboard, and every morning and evening you have
## to solve a new movement puzzle in order to cross the floor. That would be fine if you got
## to be the rook or the queen, but instead, you have to be the knight. Worse, if you take
## too much time solving the puzzle, you get "volunteered" as a test subject for the LAMBCHOP
## doomsday device!
##
## To help yourself get to and from your bunk every day, write a function called
## answer(src, dest) which takes in two parameters: the source square, on which you start,
## and the destination square, which is where you need to land to solve the puzzle.  The
## function should return an integer representing the smallest number of moves it will take
## for you to travel from the source square to the destination square using a chess knight's
## moves (that is, two squares in any direction immediately followed by one square
## perpendicular to that direction, or vice versa, in an "L" shape).  Both the source and
## destination squares will be an integer between 0 and 63, inclusive, and are numbered like
## the example chessboard below:
##
## -------------------------
## | 0| 1| 2| 3| 4| 5| 6| 7|
## -------------------------
## | 8| 9|10|11|12|13|14|15|
## -------------------------
## |16|17|18|19|20|21|22|23|
## -------------------------
## |24|25|26|27|28|29|30|31|
## -------------------------
## |32|33|34|35|36|37|38|39|
## -------------------------
## |40|41|42|43|44|45|46|47|
## -------------------------
## |48|49|50|51|52|53|54|55|
## -------------------------
## |56|57|58|59|60|61|62|63|
## -------------------------

from collections import deque

class Square:
    def __init__(self, row, col, dist):
        self.row = row
        self.col = col
        self.dist = dist
    
    def __eq__(self, other):
        # For checking square matches
        return (self.row == other.row) and (self.col == other.col)
    
    def __hash__(self):
        # For visted set
        return hash((self.row, self.col))

def solution(src, dest):
    # Possible moves
    board_size = 8
    row_jumps = [-1, -1, 1, 1, -2, -2, 2, 2]
    col_jumps = [-2, 2, -2, 2, -1, 1, -1, 1]
    
    def valid_coordinate(row, col):
        # Not outside
        return not (row < 0 or row > board_size -1 or col < 0 or col > board_size - 1)
    
    def min_moves(src_row, src_col, dest_row, dest_col):
        # Data structures for BFS
        queue = deque([])
        visited = set()
        
        # From and to
        start = Square(src_row, src_col, 0)
        end = Square(dest_row, dest_col, 0)
        queue.append(start)
        
        # begin the dfs
        while len(queue) > 0:
            # Check if next move is the end
            move = queue.pop()
            r = move.row
            c = move.col
            if move == end:
                return move.dist
                
            # Enqueue the next few valid jumps       
            if not move in visited:
                visited.add(move)
                for row_jump, col_jump in zip(row_jumps, col_jumps):
                    row_next = move.row + row_jump
                    col_next = move.col + col_jump
                    if valid_coordinate(row_next, col_next):
                        move_next = Square(row_next, col_next, move.dist + 1)
                        queue.append(move_next)
        return -1
    
    # Put it in a nicer format which reflects actual board
    def get_square(square):
        row = square / board_size
        column = square % board_size
        return row, column
    
    src_row, src_col = get_square(src)
    dest_row, dest_col = get_square(dest)
    return min_moves(src_row, src_col, dest_row, dest_col)


if __name__ == "__main__":
    print solution(0, 1)
