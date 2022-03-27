def nums():
    lst = [*range(0, 201, 2)]
    def gen(a=0):
        while a < len(lst):
            yield lst[a]
            a += 1
    a = gen()
    try:
        while True:
            print(next(a), end = " ")
    except StopIteration:
        return sum(lst)

print('\n', nums(), sep="")