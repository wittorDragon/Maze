import random

def generate_maze(width, height, complexity):
    maze = [["X" for _ in range(width)] for _ in range(height)]
    start_x, start_y = 1, random.randint(1, height - 2)
    end_x, end_y = width - 2, random.randint(1, height - 2)
    maze[start_y][start_x] = "S"
    maze[end_y][end_x] = "E"
    
    open_list = [(start_x, start_y)]
    for _ in range(complexity):
        if not open_list:
            break
        x, y = random.choice(open_list)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 < nx < width - 1 and 0 < ny < height - 1 and maze[ny][nx] == "X":
                maze[y + dy][x + dx] = " "
                maze[ny][nx] = " "
                open_list.append((nx, ny))
    return maze

def print_maze(maze):
    for row in maze:
        print("".join(row))
    print()

sizes = [(10, 10), (12, 12), (15, 15)]
complexities = [18, 40, 30,]
mazes = [generate_maze(w, h, c) for (w, h), c in zip(sizes, complexities)]

for i, maze in enumerate(mazes):
    print(f"Maze {i + 1}:")
    print_maze(maze)

