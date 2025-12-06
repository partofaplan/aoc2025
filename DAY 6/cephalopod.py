from math import prod
from pathlib import Path


def read_grid(path):
    lines = [line.rstrip("\n") for line in Path(path).read_text().splitlines()]
    width = max(len(line) for line in lines)
    return [line.ljust(width) for line in lines]


def find_segments(grid):
    width = len(grid[0])
    segments = []
    in_block = False
    start = 0

    for col in range(width):
        column_has_char = any(row[col] != " " for row in grid)
        if column_has_char and not in_block:
            start = col
            in_block = True
        elif not column_has_char and in_block:
            segments.append((start, col))
            in_block = False

    if in_block:
        segments.append((start, width))

    return segments


def evaluate_segment(grid, start, end):
    numbers = []
    for row in grid[:-1]:
        num_str = row[start:end].strip()
        if not num_str:
            raise ValueError(f"Missing number in segment {start}-{end}")
        numbers.append(int(num_str))

    op_section = grid[-1][start:end]
    op = next((c for c in op_section if c in "+*"), None)
    if op is None:
        raise ValueError(f"Missing operator in segment {start}-{end}")

    if op == "+":
        return sum(numbers)
    if op == "*":
        return prod(numbers)
    raise ValueError(f"Unknown operator {op} in segment {start}-{end}")


def main():
    grid = read_grid(Path(__file__).with_name("input.txt"))
    segments = find_segments(grid)
    total = sum(evaluate_segment(grid, start, end) for start, end in segments)
    print(total)


if __name__ == "__main__":
    main()
