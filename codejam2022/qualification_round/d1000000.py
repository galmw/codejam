import sys


def solve():
    """
    """
    # ACTUAL SOLVE CODE GOES HERE
    num_dices = int(input())
    dices = list(map(int, input().split()))
    max_possible = min(num_dices, max(dices))
    dices = sorted(dices)
    
    candidate = 1
    dice_idx = 0
    while candidate <= max_possible:
        if dice_idx == len(dices):
            break
        while dice_idx < len(dices) and candidate > dices[dice_idx]:
            dice_idx += 1

        if dice_idx < len(dices):
            candidate += 1
            dice_idx += 1

    return candidate - 1


def main():
    t = int(input())
    for i in range(t):
        sys.stdout.write('Case #{}: {}\n'.format(i + 1, solve()))


if __name__ == '__main__':
    main()
