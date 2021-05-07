import sys


"""
def solve():
    length = int(input())
    numbers = list(map(int, input().split()))
    # ACTUAL SOLVE CODE GOES HERE

"""

def solve():
    length = int(input())
    numbers = list(map(int, input().split()))
    # ACTUAL SOLVE CODE GOES HERE
    answer = 1
    return answer


def main():
    t = int(input())
    for i in range(t):
        sys.stdout.write('Case #{}: {}\n'.format(i + 1, solve()))


if __name__ == '__main__':
    main()
