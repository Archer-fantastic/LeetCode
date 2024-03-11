def B():
    n = int(input())
    arr = [1,3,5,7,11,13,17,19,23,31,37,41,43,47,53,61,67,71,73,79,83,89,91,97]
    _min = bin(n)[2:].count("1")
    for a in arr:
        _min = min(_min,bin(n*a)[2:].count("1"))
    print(_min)
    # return _min

B()