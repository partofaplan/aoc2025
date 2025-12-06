from pathlib import Path


def parse_ranges(path):
    ranges = []
    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            if "-" not in line:
                continue
            start_str, end_str = line.split("-", 1)
            try:
                start, end = int(start_str), int(end_str)
            except ValueError:
                continue
            if start > end:
                start, end = end, start
            ranges.append((start, end))
    return ranges


def merge_ranges(ranges):
    if not ranges:
        return []

    ranges = sorted(ranges, key=lambda r: r[0])
    merged = [list(ranges[0])]

    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end + 1:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])

    return [(s, e) for s, e in merged]


def total_range_length(ranges):
    return sum(end - start + 1 for start, end in ranges)


def main():
    ranges = parse_ranges(Path(__file__).with_name("input.txt"))
    merged = merge_ranges(ranges)
    print(total_range_length(merged))


if __name__ == "__main__":
    main()
