## You're so close to destroying the LAMBCHOP doomsday device you can taste it! But in
## order to do so, you need to deploy special self-replicating bombs designed for you by
## the brightest scientists on Bunny Planet. There are two types: Mach bombs (M) and
## Facula bombs (F). The bombs, once released into the LAMBCHOP's inner workings, will
## automatically deploy to all the strategic points you've identified and destroy them
## at the same time.
##
## But there's a few catches. First, the bombs self-replicate via one of two distinct
## processes:
## Every Mach bomb retrieves a sync unit from a Facula bomb; for every Mach bomb,
## a Facula bomb is created;
## Every Facula bomb spontaneously creates a Mach bomb.
##
## For example, if you had 3 Mach bombs and 2 Facula bombs, they could either produce 3
## Mach bombs and 5 Facula bombs, or 5 Mach bombs and 2 Facula bombs. The replication
## process can be changed each cycle.
##
## Second, you need to ensure that you have exactly the right number of Mach and Facula
## bombs to destroy the LAMBCHOP device. Too few, and the device might survive. Too many,
## and you might overload the mass capacitors and create a singularity at the heart of the
## space station - not good!
##
## And finally, you were only able to smuggle one of each type of bomb - one Mach, one
## Facula - aboard the ship when you arrived, so that's all you have to start with. (Thus
## it may be impossible to deploy the bombs to destroy the LAMBCHOP, but that's not going
## to stop you from trying!)
##
## You need to know how many replication cycles (generations) it will take to generate the
## correct amount of bombs to destroy the LAMBCHOP. Write a function answer(M, F) where M
## and F are the number of Mach and Facula bombs needed. Return the fewest number of
## generations (as a string) that need to pass before you'll have the exact number of bombs
## necessary to destroy the LAMBCHOP, or the string "impossible" if this can't be done! M
## and F will be string representations of positive integers no larger than 10^50. For
## example, if M = "2" and F = "1", one generation would need to pass, so the answer would
## be "1". However, if M = "2" and F = "4", it would not be possible.
    
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
    
    
