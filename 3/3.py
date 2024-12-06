import re
from io import open



def main():

    with open("input.txt") as f:
        memory = f.read()
        print(memory)

        muls = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
        dos = re.compile(r'do\(\)')
        donts = re.compile(r"don't\(\)")

        parts = donts.split(memory)

        sum = 0
        for g in muls.findall(parts[0]):
            sum += int(g[0]) * int(g[1])

        for part in parts[1:]:
            subparts = dos.split(part, maxsplit=1)
            if len(subparts) == 2:
                for g in muls.findall(subparts[1]):
                    sum += int(g[0]) * int(g[1])

        print(sum)




if __name__ == "__main__":
    main()
