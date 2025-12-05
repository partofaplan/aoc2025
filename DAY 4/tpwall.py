# Create a grid from the input file
def create_grid_from_file(file_path):
    grid = []
    with open(file_path, 'r') as file:
        for line in file:
            grid.append(list(line.strip()))
    return grid

def print_grid(grid):
    for row in grid:
        print(''.join(row))

if __name__ == "__main__":
    file_path = 'input.txt'  # Replace with your input file path
    grid = create_grid_from_file(file_path)
    print_grid(grid)


def replace_isolated_ats(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    
    new_grid = [row[:] for row in grid]  
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                at_neighbors = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                        at_neighbors += 1
                if at_neighbors <= 3:
                    new_grid[r][c] = 'x'
    
    return new_grid

if __name__ == "__main__":
    file_path = 'input.txt'  #
    grid = create_grid_from_file(file_path)
    print("Original Grid:")
    print_grid(grid)
    
    modified_grid = replace_isolated_ats(grid)
    print("\nModified Grid:")
    print_grid(modified_grid)


def count_x_characters(grid):
    count = 0
    for row in grid:
        count += row.count('x')
    return count

if __name__ == "__main__":
    file_path = 'input.txt'  
    grid = create_grid_from_file(file_path)
    modified_grid = replace_isolated_ats(grid)
    
    x_count = count_x_characters(modified_grid)
    print(f"\nNumber of 'x' characters in the modified grid: {x_count}")

