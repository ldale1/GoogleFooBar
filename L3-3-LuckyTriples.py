def solution(l):
    pass



if __name__ == "__main__":
    import time
    
    tests = [
        ([1, 1, 1], 1), #1
        ([1, 2, 3, 4, 5, 6], 3) # 3
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
