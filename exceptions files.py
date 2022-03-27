import os

# example 1
print("Example 1")
try:
    f = open('lesson_file_one.txt', 'x')
except FileExistsError:
    print('This file exists')
else:
    print('Creating new file')
finally:
    print('File created\n')


# example 2
print("Example 2")
try:
    f = open('lesson_file_two', 'r')
    ints = []
    for line in f:
        ints.append(float(line))
    s = sum(ints)
except FileNotFoundError:
    print('File is nonexistent')
except ValueError:
    print("Invalid number")
else:
    print('Searching file')
    print(s)
    print(ints)
finally:
    print("Operation is finished\n")


# example 3
print("Example 3")
try:
    f = open('1.txt')
    ints = []
    for line in f:
        ints.append(float(line))
    s = sum(ints)
except FileNotFoundError:
    print('File is nonexistent')
except ValueError:
    print("ValueError")
except Exception:
    print("What is this?! I'm broken....")
else:
    print('Searching file')
    print(f"Sum of values in file: {s}")
    print(f"List created from vallues in file: {ints}")
finally:
    print("Operation is finished\n")


# example 4

if not os.path.isfile('lesson_file_two.txt'):
    raise FileNotFoundError

# exampple 5from
fn = f'{input("Enter filename")}.txt'
try:
    f = open(fn, 'r')
except FileNotFoundError:
    try:
        f = open(fn, 'x')
    except FileExistsError:
        print('File exists')
    try:
        while line := input():
            f.write(f"{line}\n")
        f.close()
    except IsADirectoryError:
        print("Waiting for a file")
finally:
    f = open('fn.txt', 'r')
    print(f.read())
    f.close()



