import sys


def solve():
    """
    length = int(input())
    numbers = list(map(int, input().split()))
    answer = 1
    return answer
    """
    # ACTUAL SOLVE CODE GOES HERE
    numbers = list(map(int, input().split()))
    rows, cols = numbers[0], numbers[1]
    out = "\n"
    for i in range(rows * 2 + 1):
        for j in range(cols * 2 + 1):
            if i <= 1 and j <= 1:
                out += "."
            elif i % 2 == 0 and j % 2 == 0:
                out += "+"
            elif i % 2 == 1 and j % 2 == 0:
                out += "|"
            elif i % 2 == 0 and j % 2 == 1:
                out += "-"
            else:
                out += "."
        if i != rows * 2:
            out += "\n"
    return out


def main():
    t = int(input())
    for i in range(t):
        sys.stdout.write('Case #{}: {}\n'.format(i + 1, solve()))


if __name__ == '__main__':
    main()

