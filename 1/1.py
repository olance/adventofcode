from collections import defaultdict
from io import open


def main():
    col1 = []
    col2 = []
    col2_counts = defaultdict(int)

    with open("input.txt") as f:
        while l := f.readline():
            (id1, id2) = l.split('   ')
            col1.append(int(id1.strip()))

            id2 = int(id2.strip())
            col2.append(id2)

            col2_counts[id2] += 1


    col1.sort()
    col2.sort()

    distance = 0
    similarity = 0

    while len(col1) > 0:
        id1 = col1.pop()
        distance += abs(id1 - col2.pop())
        similarity += id1 * col2_counts[id1]

    print(f"Distance: {distance}")
    print(f"Similarity: {similarity}")


if __name__ == "__main__":
    main()
