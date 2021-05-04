from collections import Counter

def trim(data, n):
    counter = Counter(data)
    i = 0
    while i < len(data):
        job = data[i]
        if counter[job] > n:
            data.pop(i)
        else:
            i += 1
    return data

if __name__ == "__main__":
    x = [1, 2, 2, 3, 3, 3, 4, 5, 5]
    n = 1

    print trim(x, n)
