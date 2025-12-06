from pathlib import Path


DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]


def create_grid_from_file(file_path):
    grid = []
    with open(file_path, "r") as file:
        for line in file:
            grid.append(list(line.strip()))
    return grid


def replace_isolated_ats(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    new_grid = [row[:] for row in grid]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "@":
                continue

            neighbors = 0
            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "@":
                    neighbors += 1

            if neighbors <= 3:
                new_grid[r][c] = "x"

    return new_grid


def count_x_characters(grid):
    return sum(row.count("x") for row in grid)


def main():
    grid = create_grid_from_file(Path(__file__).with_name("input.txt"))
    modified_grid = replace_isolated_ats(grid)
    print(count_x_characters(modified_grid))


if __name__ == "__main__":
    main()
