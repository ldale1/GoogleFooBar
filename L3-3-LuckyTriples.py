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
