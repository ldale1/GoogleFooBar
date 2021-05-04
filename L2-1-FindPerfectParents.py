def solution(h, q):
    nodes = 2 ** h - 1

    def traverse(num, root, depth):
        left = root - 2**(h-depth)
        right = root - 1
        
        if num == left or num == right:
            return root
        
        if num <= left:
            return traverse(num, left, depth+1)
        else:
            return traverse(num, right, depth+1)
    return [-1 if num==nodes else traverse(num, nodes, 1) for num in q] 
    
    


if __name__ == "__main__":
    h = 3
    q = [7, 3, 5, 1]
    sol = [-1,7,6,3]
    print solution(h, q)

    h = 30
    q = [19, 14, 28]
    sols = [21, 15, 29]
    print solution(h, q)
