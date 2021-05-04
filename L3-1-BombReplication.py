    
def solution(x, y):
    
    def traverse(M, F, depth):

        # Have an answer
        if M==1 or F==1:
            if M == F:
                return str(depth)
            else:
                return str(depth + max(M, F) - 1)
            

        # Both have to be positive
        # Can't be equal
        # Can't both be even
        elif M*F <= 0 or M == F or (M % 2)+(F % 2) == 0:
            return "Impossible"

        # Can't subtract the bigger from the smaller,
        # as this will push answer negative
        smaller = min(M, F)
        larger = max(M, F)
        multiplier = larger / smaller
        
        return traverse(larger - smaller * multiplier, smaller, depth + multiplier)
            
    return traverse(int(x), int(y), 0)
    


if __name__ == "__main__":
    print solution(10**50, 123)

    print solution(4, 7)
    
    print solution(196, 335)
    
    print solution(8, 4)

    print solution(1, 1)

    print solution(0, 0)
    
    
