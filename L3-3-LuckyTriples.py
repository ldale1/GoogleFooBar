## You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's
## bunny prisoners, but once they're free of the prison blocks, the bunnies are going to need
## to escape Lambda's space station via the escape pods as quickly as possible. Unfortunately,
## the halls of the space station are a maze of corridors and dead ends that will be a
## deathtrap for the escaping bunnies. Fortunately, Commander Lambda has put you in charge of
## a remodeling project that will give you the opportunity to make things a little easier for
## the bunnies. Unfortunately(again), you can't just remove all obstacles between the bunnies
## and the escape pods - at most you can remove one wall per escape pod path, both to maintain
## structural integrity of the station and to avoid arousing Commander Lambda's suspicions.
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

from collections import defaultdict

def solution1(l):
    # Dictionary of index:factors
    nums = len(l)
    factors = {}
    for i in range(nums-1, -1, -1):
        factors[i] = []
        vi = l[i]
        for j, vj in enumerate(l[:i]):
            if not vi%vj:
                factors[i].append(j)

    # Sum i,j perms
    total = 0
    for i in range(nums-1, -1, -1):
        js = factors[i]
        for j in js:
            total += len(factors[j])

    return total

def solution(l):
    total = 0
    nums = len(l)

    # Every time descendent is found,
    # Add the number of parents to total
    multiples = defaultdict(int)
    for i in range(nums-1, -1, -1):
        vi = l[i]
        for j, vj in enumerate(l[:i]):
            if not vi%vj:
                multiples[j] += 1
                total += multiples[i]
    return total
            

if __name__ == "__main__":
    import time
    
    tests = [
        ([1, 1, 1], 1), #1
        ([1, 2, 3, 4, 5, 6], 3) # 3 [ (1,2,4), (1,2,6), (1,3,6) ]
        ] 
    
    for i, (l, ans) in enumerate(tests):
        start = time.time()
        answer = solution(l)
        end = time.time()
        
        print "TEST", str(i+1) + ":"
        print "answer:", answer
        print "expected:", ans
        print "time:", end - start
        print ""
