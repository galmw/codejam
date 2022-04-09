import sys


def solve():
    """
    """
    AMOUNT = 10 ** 6
    # ACTUAL SOLVE CODE GOES HERE
    printer_1 = list(map(int, input().split()))
    printer_2 = list(map(int, input().split()))
    printer_3 = list(map(int, input().split()))
    min_colors = list(min(printer_1[i], printer_2[i], printer_3[i]) for i in range(len(printer_1)))
    if sum(min_colors) < AMOUNT:
        return "IMPOSSIBLE\n"
    else:
        if min_colors[0] >= AMOUNT:
            res = (AMOUNT, 0, 0, 0)
        elif sum(min_colors[0:2]) >= AMOUNT:
            res = (min_colors[0], AMOUNT - min_colors[0], 0, 0)
        elif sum(min_colors[0:3]) >= AMOUNT:
            res = (min_colors[0], min_colors[1], AMOUNT - sum(min_colors[0:2]), 0)
        else:
            residue = 10 ** 6 - (min_colors[0] + min_colors[1] + min_colors[2])
            res =  (min_colors[0], min_colors[1], min_colors[2], residue)
    return f"{res[0]} {res[1]} {res[2]} {res[3]}\n"


def main():
    t = int(input())
    for i in range(t):
        sys.stdout.write('Case #{}: {}\n'.format(i + 1, solve()))


if __name__ == '__main__':
    main()
