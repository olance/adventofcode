from io import open


WORD = 'XMAS'
WORD_REVERSED = 'SAMX'

def find_above(lines, line_idx, char_idx):
    found = 0

    # Vertical
    if (
            lines[line_idx - 0][char_idx] == WORD[0] and
            lines[line_idx - 1][char_idx] == WORD[1] and
            lines[line_idx - 2][char_idx] == WORD[2] and
            lines[line_idx - 3][char_idx] == WORD[3]
    ):
        found += 1

    # Diagonal left
    if char_idx >= len(WORD) - 1:
        if (
                lines[line_idx - 0][char_idx - 0] == WORD[0] and
                lines[line_idx - 1][char_idx - 1] == WORD[1] and
                lines[line_idx - 2][char_idx - 2] == WORD[2] and
                lines[line_idx - 3][char_idx - 3] == WORD[3]
        ):
            found += 1

    # Diagonal right
    if len(lines[line_idx]) - char_idx >= len(WORD):
        if (
                lines[line_idx - 0][char_idx + 0] == WORD[0] and
                lines[line_idx - 1][char_idx + 1] == WORD[1] and
                lines[line_idx - 2][char_idx + 2] == WORD[2] and
                lines[line_idx - 3][char_idx + 3] == WORD[3]
        ):
            found += 1

    return found

def find_below(lines, line_idx, char_idx):
    found = 0

    # Vertical
    if (
            lines[line_idx + 0][char_idx] == WORD[0] and
            lines[line_idx + 1][char_idx] == WORD[1] and
            lines[line_idx + 2][char_idx] == WORD[2] and
            lines[line_idx + 3][char_idx] == WORD[3]
    ):
        found += 1

    # Diagonal left
    if char_idx >= len(WORD) - 1:
        if (
                lines[line_idx + 0][char_idx - 0] == WORD[0] and
                lines[line_idx + 1][char_idx - 1] == WORD[1] and
                lines[line_idx + 2][char_idx - 2] == WORD[2] and
                lines[line_idx + 3][char_idx - 3] == WORD[3]
        ):
            found += 1

    # Diagonal right
    if len(lines[line_idx]) - char_idx >= len(WORD):
        if (
                lines[line_idx + 0][char_idx + 0] == WORD[0] and
                lines[line_idx + 1][char_idx + 1] == WORD[1] and
                lines[line_idx + 2][char_idx + 2] == WORD[2] and
                lines[line_idx + 3][char_idx + 3] == WORD[3]
        ):
            found += 1

    return found

def find_left(line, char_idx):
    if line.find(WORD_REVERSED, char_idx - len(WORD) + 1, char_idx + 1) != -1:
        return 1
    else:
        return 0

def find_right(line, char_idx):
    if line.find(WORD, char_idx, char_idx + len(WORD)) != -1:
        return 1
    else:
        return 0


def main():
    with open("input.txt") as f:
        lines = f.readlines()
        word_count = 0

        for line_idx, line in enumerate(lines):
            scan_from = -1
            while scan_from < len(line):
                scan_from = line.find('X', scan_from + 1)
                if scan_from == -1:
                    break

                if line_idx >= len(WORD) - 1:
                    word_count += find_above(lines, line_idx, scan_from)

                if len(lines) - line_idx >= len(WORD):
                    word_count += find_below(lines, line_idx, scan_from)

                if scan_from >= len(WORD) - 1:
                    word_count += find_left(line, scan_from)

                if len(line) - scan_from >= len(WORD):
                    word_count += find_right(line, scan_from)

        print(word_count)


if __name__ == "__main__":
    main()
