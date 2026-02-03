def create_stack():
    return []
def push_stack(item,stack):
    stack.append(item)
def pop_stack(stack):
    return stack.pop()
# Optional helper for stack peek (not used in current implementation)
def top_stack(stack):
    return stack[-1]
def is_empty(stack):
    return stack == []

def find_start_position(grid):
    z_axis = len(grid)
    rows = len(grid[0])
    cols = len(grid[0][0])

    for z in range(z_axis):
        for r in range(rows):
            for c in range(cols):
                if grid[z][r][c] == "F":
                    return (z, r, c)

    return None

def is_valid_move(grid, position, visited, directions):
    z, r, c = position

    z_axis = len(grid)
    rows = len(grid[0])
    cols = len(grid[0][0])

    # Boundary check
    if not (0 <= z < z_axis and 0 <= r < rows and 0 <= c < cols):
        return False

    # Cell type check
    if grid[z][r][c] in ("S"):
        return False

    # Visited check
    if position in visited:
        return False

    # Neighborhood safety constraint
    for dz, dr, dc, _ in directions:
        nz, nr, nc = z + dz, r + dr, c + dc
        if 0 <= nz < z_axis and 0 <= nr < rows and 0 <= nc < cols:
            if grid[nz][nr][nc] == "S":
                return False

    return True

def safe_path_3d(grid):
    start_pos = find_start_position(grid)
    if start_pos is None:
        return []

    stack = create_stack()
    visited = set()

    push_stack((start_pos, []), stack)
    visited.add(start_pos)

    directions = [
        (1, 0, 0, "up"),
        (-1, 0, 0, "down"),
        (0, 1, 0, "south"),
        (0, -1, 0, "north"),
        (0, 0, 1, "east"),
        (0, 0, -1, "west"),
    ]

    while not is_empty(stack):
        (cur_z, cur_r, cur_c), cur_path = pop_stack(stack)

        if grid[cur_z][cur_r][cur_c] == "M":
            return cur_path

        for dz, dr, dc, direction_name in directions:
            next_pos = (cur_z + dz, cur_r + dr, cur_c + dc)

            if is_valid_move(grid, next_pos, visited, directions):
                push_stack((next_pos, cur_path + [direction_name]), stack)
                visited.add(next_pos)
    return []
if __name__ == "__main__":
    # Example usage
    example_grid = [
    [
        ["F", "O", "O", "O"],
        ["O", "O", "O", "O"],
        ["O", "O", "O", "O"],
        ["O", "O", "O", "M"]
    ]
]


    path = safe_path_3d(example_grid)
    print("Path:", path)
