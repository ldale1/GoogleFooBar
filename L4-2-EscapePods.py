## You've blown up the LAMBCHOP doomsday device and relieved the bunnies
## of their work duries -- and now you need to escape from the space
## station as quickly and as orderly as possible! The bunnies have all
## gathered in various locations throughout the station, and need to make
## their way towards the seemingly endless amount of escape pods positioned
## in other parts of the station. You need to get the numerous bunnies
## through the various rooms to the escape pods. Unfortunately, the
## corridors between the rooms can only fit so many bunnies at a time.
## What's more, many of the corridors were resized to accommodate the
## LAMBCHOP, so they vary in how many bunnies can move through them at a
## time. 
##
## Given the starting room numbers of the groups of bunnies, the room
## numbers of the escape pods, and how many bunnies can fit through at
## a time in each direction of every corridor in between, figure out
## how many bunnies can safely make it to the escape pods at a time at
## peak.
##
## Write a function solution(entrances, exits, path) that takes an
## array of integers denoting where the groups of gathered bunnies
## are, an array of integers denoting where the escape pods are located,
## and an array of an array of integers of the corridors, returning the
## total number of bunnies that can get through at each time step as an int.
## The entrances and exits are disjoint and thus will never overlap. The
## path element path[A][B] = C describes that the corridor going from A
## to B can fit C bunnies at each time step.  There are at most 50 rooms
## connected by the corridors and at most 2000000 bunnies that will fit
## at a time.
##
## For example, if you have:
## entrances = [0, 1]
## exits = [4, 5]
## path = [
##  [0, 0, 4, 6, 0, 0],  # Room 0: Bunnies
##  [0, 0, 5, 2, 0, 0],  # Room 1: Bunnies
##  [0, 0, 0, 0, 4, 4],  # Room 2: Intermediate room
##  [0, 0, 0, 0, 6, 6],  # Room 3: Intermediate room
##  [0, 0, 0, 0, 0, 0],  # Room 4: Escape pods
##  [0, 0, 0, 0, 0, 0],  # Room 5: Escape pods
## ]
##
## Then in each time step, the following might happen:
## 0 sends 4/4 bunnies to 2 and 6/6 bunnies to 3
## 1 sends 4/5 bunnies to 2 and 2/2 bunnies to 3
## 2 sends 4/4 bunnies to 4 and 4/4 bunnies to 5
## 3 sends 4/6 bunnies to 4 and 4/6 bunnies to 5
##
## So, in total, 16 bunnies could make it to the escape pods at 4 and 5
## at each time step.  (Note that in this example, room 3 could have
## sent any variation of 8 bunnies to 4 and 5, such as 2/6 and 6/6, but
## the final solution remains the same.)

from collections import deque

def Simplify(entrances, exits, path):
    
    # Transform path to have single source sink
    length = len(path)
    new = [[path[i-1][j-1] if (1 <= i <= length) and (1 <= j <= length) else 0 \
             for j in range(length + 2)] for i in range(length + 2)]
    for entry in entrances:
        new[0][entry+1] = float("Inf")
    for exit_ in exits:
        new[exit_+1][length+1] = float("Inf")
    return new


def BreadthFirstSearch(source, sink, parent, path):
    
        # Tracking
        queue = deque()
        visited = [False] * len(parent)

        # Standard BFS
        queue.append(source)
        visited[source] = True
        while queue:
            node = queue.popleft()
            for ind, val in enumerate(path[node]):
                if (not visited[ind]) and (val):
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = node

        # Is sink reachable?
        return visited[sink]

def EdmondsKarp(path):
    
    # Fill path with BFS
    rows = len(path)
    parent = [-1] * rows

    # While there is path, improve flow
    max_flow, source, sink = 0, 0, rows-1
    while BreadthFirstSearch(source, sink, parent, path):
        
        # Minimum residual capacity BFS path
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, path[parent[s]][s])
            s = parent[s]

        # Add path flow to overall flow
        max_flow += path_flow

        # update residual capacities and reverse
        s = sink
        while s != source:
            u = parent[s]
            path[u][s] -= path_flow
            path[s][u] += path_flow
            s = parent[s]

    return max_flow


def solution(entrances, exits, path):
    return EdmondsKarp(Simplify(entrances, exits, path))
            


if __name__ == "__main__":
    import time
    
    tests = [] 

    # 1.
    entrances, exits, path = ([0], [3],
                              [[0, 7, 0, 0],
                               [0, 0, 6, 0],
                               [0, 0, 0, 8],
                               [9, 0, 0, 0]])
    ans = 6

    test = ((entrances, exits, path), ans)
    tests.append(test)

    # 2.
    entrances, exits, path = [0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    ans = 16

    test = ((entrances, exits, path), ans)
    tests.append(test)


    for i, (args, ans) in enumerate(tests):
        start = time.time()
        answer = solution(*args)
        end = time.time()
        
        print("TEST", str(i+1) + ":")
        print("answer:", answer)
        print("expected:", ans)
        print("correct:", ans == answer)
        print("time:", end - start)
        print("")

    print(path)
    print(Simplify(entrances, exits, path))
