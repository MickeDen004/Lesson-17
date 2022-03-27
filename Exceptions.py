# Exception 1 (ZeroDivisionError)
try:
    k = 1/0
except ZeroDivisionError:
    k = 0
print(k)
# Exception 2 (ArithmeticError)
try:
    k = 1/0
except ArithmeticError:
    k = 6
print(k)

# Exception 3 (ValueError)

f = open('1.txt')
ints = []
try:
    for line in f:
        ints.append(int(line))
    s = sum(ints)
except ValueError:
    print('Wrong number. Exit.')
except Exception:
    print('What is this?!')
else:
    print('Everything is okay')
finally:
    f.close()
    print(ints)
    print(s)
    print('File closed')