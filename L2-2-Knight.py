# 0->63 encode squres

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
