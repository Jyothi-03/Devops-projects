import sys

def print_name(name, k):
    for i in range(k):
        print(("*" + name + "*" + " ") * (i+1))

if __name__ == "__main__":
    name = sys.argv[1]
    k = int(sys.argv[2])
    print_name(name, k)
