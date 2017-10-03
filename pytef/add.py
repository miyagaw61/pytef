import sys

def add_func(x, y):
    if type(y) == int:
        return x + y
    else:
        return TypeError

if __name__ == '__main__':
    print(add_func(int(sys.argv[1]), int(sys.argv[2])))
