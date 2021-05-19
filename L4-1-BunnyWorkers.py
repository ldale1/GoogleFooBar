## You need to free the bunny workers before Commander Lambda's space station explodes! Unfortunately, the Commander was very careful with the highest-value workers -- they all work in separate, maximum-security work rooms. 
## The rooms are opened by putting keys into each console, then pressing the open button on each console simultaneously. 
## When the open button is pressed, each key opens its corresponding lock on the work room. 
## So, the union of the keys in all of the consoles must be all of the keys. 
## The scheme may require multiple copies of one key given to different minions.
## 
## The consoles are far enough apart that a separate minion is needed for each one. 
## Fortunately, you have already relieved some bunnies to aid you - and even better, you were able to steal the keys while you were working as Commander Lambda's assistant. 
## The problem is, you don't know which keys to use at which consoles. 
## The consoles are programmed to know which keys each minion had, to prevent someone from just stealing all of the keys and using them blindly. 
## There are signs by the consoles saying how many minions had some keys for the set of consoles. 
## You suspect that Commander Lambda has a systematic way to decide which keys to give to each minion such that they could use the consoles.
## 
## You need to figure out the scheme that Commander Lambda used to distribute the keys. 
## You know how many minions had keys, and how many consoles are by each work room.  
## You know that Command Lambda wouldn't issue more keys than necessary (beyond what the key distribution scheme requires), and that you need as many bunnies with keys as there are consoles to open the work room.
##
## SPEC:
## Given the number of bunnies available and the number of locks required to open a work room,
## write a function solution(num_buns, num_required) which returns a specification of how 
## to distribute the keys such that any num_required bunnies can open the locks, but no
## group of (num_required - 1) bunnies can.
##
## Each lock is numbered starting from 0. 
## The keys are numbered the same as the lock they open (so for a duplicate key, the number will repeat, since it opens the same lock). 
## For a given bunny, the keys they get is represented as a sorted list of the numbers for the keys. 
## To cover all of the bunnies, the final solution is represented by a sorted list of each individual bunny's list of keys.  
## Find the lexicographically least such key distribution - that is, the first bunny should have keys sequentially starting from 0.
##
## num_buns will always be between 1 and 9, and num_required will always be between 0 and 9 (both inclusive).  


from itertools import combinations

def solution(num_buns, num_required):
    # one of num_buns - (num_required - 1) must have the last key
    keys = [[] for b in range(num_buns)]
    key_duplicates = num_buns - (num_required - 1)
    combos = combinations(range(num_buns), key_duplicates)
    for key, bunnies in enumerate(combos):
        for bunny in bunnies:
            keys[bunny].append(key)
    return keys


if __name__ == "__main__":
    import time
    
    tests = [] 

    # 1. One req, so any can open
    nb = 3
    nr = 1
    ans = [[0], [0], [0]]

    test = ((nb,nr), ans)
    tests.append(test)

    # 2. Two req, so one can't open
    nb = 2
    nr = 2
    ans = [[0], [1]]

    test = ((nb,nr), ans)
    tests.append(test)
    
    # 3. Two req, so one can't open
    nb = 3
    nr = 2
    ans = [[0,1], [0,2], [1,2]]

    test = ((nb,nr), ans)
    tests.append(test)
    
    # 4. Three req, so two can't open

    # answer
    # 10 locks
    # 6 keys
    nb = 5
    nr = 3
    ans = [[0, 1, 2, 3, 4, 5],  # 6 7 8 9
          [0, 1, 2, 6, 7, 8],   # 3 4 5 9
          [0, 3, 4, 6, 7, 9],   # 1 2 5 8
          [1, 3, 5, 6, 8, 9],   # 0 2 4 7
          [2, 4, 5, 7, 8, 9]]   # 0 1 3 6

    test = ((nb,nr), ans)
    tests.append(test)
    
    for i, ((nb, nr), ans) in enumerate(tests):
        start = time.time()
        answer = solution(nb, nr)
        end = time.time()
        
        print("TEST", str(i+1) + ":")
        print("answer:", answer)
        print("expected:", ans)
        print("correct:", ans == answer)
        print("time:", end - start)
        print("")
