from collections import defaultdict
from io import open


def sign(n: int) -> -1 | 1:
    return -1 if n < 0 else 1

def check_reports(reports):
    current = reports.pop(0)
    direction = sign(reports[0] - current)
    safe = True

    while len(reports) > 0:
        previous = current
        current = reports.pop(0)

        diff = current - previous
        if abs(diff) > 3 or abs(diff) < 1 or sign(diff) != direction:
            safe = False
            break

    return safe


def main():
    safe_count = 0
    dampening = True

    with open("input.txt") as f:
        while l := f.readline().strip():
            l = list(map(int, l.split()))

            if not check_reports(l.copy()):
                if dampening:
                    for i in range(len(l)):
                        if check_reports(l[:i] + l[i+1:]):
                            safe_count += 1
                            break
            else:
                safe_count += 1

    print(f"Safe count: {safe_count}")




if __name__ == "__main__":
    main()
