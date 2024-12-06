from collections import defaultdict
from functools import cmp_to_key
from io import open

rules = defaultdict(lambda: {"comes_before": set(), "comes_after": set()})

def main():
    with open("rules.txt") as f:
        while rule := f.readline():
            x, y = map(int, rule.strip().split("|"))
            rules[x]["comes_before"].add(y)
            rules[y]["comes_after"].add(x)

    with open("updates.txt") as f:
        valid_sum = 0
        invalid_sum = 0
        invalid_updates = []

        while update := f.readline():
            pages = list(map(int, update.strip().split(",")))

            valid = True
            for idx, page in enumerate(pages):
                before = set(pages[:idx])
                after = set(pages[idx+1:])

                if not before.issubset(rules[page]["comes_after"]) or not after.issubset(rules[page]["comes_before"]):
                    valid = False
                    invalid_updates.append(pages)
                    break

            if valid:
                valid_sum += pages[len(pages) // 2]

        for invalid_update in invalid_updates:
            fixed_update = sorted(invalid_update, key=cmp_to_key(rule_sort))
            invalid_sum += fixed_update[len(fixed_update) // 2]

    print(f"Valid sum: {valid_sum}")
    print(f"Invalid sum: {invalid_sum}")


def rule_sort(a: int, b: int) -> int:
    if a == b:
        return 0

    if b in rules[a]["comes_before"]:
        return -1

    if b in rules[a]["comes_after"]:
        return 1

if __name__ == "__main__":
    main()
