from io import open


WORD = 'MAS'
WORD_REVERSED = 'SAM'

def main():
    with open("input.txt") as f:
        lines = f.readlines()
        x_count = 0

        for line_idx, line in enumerate(lines[1:len(lines)-1]):
            scan_from = 0
            line_idx += 1

            while True:
                scan_from = line.find('A', scan_from + 1, len(line) - 2)

                if scan_from == -1:
                    break

                print(f"{line_idx}:{scan_from}")

                left = {
                    lines[line_idx - 1][scan_from - 1],
                    lines[line_idx + 1][scan_from + 1],
                }

                right = {
                    lines[line_idx - 1][scan_from + 1],
                    lines[line_idx + 1][scan_from - 1],
                }

                if left == {'M', 'S'} and right == {'M', 'S'}:
                    x_count += 1

        print(x_count)


if __name__ == "__main__":
    main()
