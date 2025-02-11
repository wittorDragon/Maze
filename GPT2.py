import turtle
import time
import keyboard

class Maze:
    def __init__(self):
        self.maze = [
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", " ", " ", " ", "X", " ", "X"],
            ["X", " ", "X", " ", "X", " ", " "],
            ["X", " ", "X", " ", "X", " ", "X"],
            ["X", " ", "X", " ", " ", " ", "X"],
            ["X", " ", "X", "X", "X", "X", "X"],
        ]
        self.ply = Pos(5, 1)
        self.end = Pos(2, 6)
        self.maze[self.ply.y][self.ply.x] = "R"
        self.maze[self.end.y][self.end.x] = "E"
        
        self.screen = turtle.Screen()
        self.screen.tracer(0)
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.hideturtle()
        
    def draw_maze(self):
        self.t.clear()
        self.t.penup()
        for y, row in enumerate(self.maze):
            for x, col in enumerate(row):
                self.t.goto(x * 20, -y * 20)
                if col == "X":
                    self.t.color("black")
                    self.t.begin_fill()
                    for _ in range(4):
                        self.t.forward(20)
                        self.t.right(90)
                    self.t.end_fill()
                elif col == "E":
                    self.t.color("red")
                    self.t.write("E", align="center", font=("Arial", 14, "bold"))
                elif col == "R":
                    self.t.color("blue")
                    self.t.write("R", align="center", font=("Arial", 14, "bold"))
        self.screen.update()
    
    def move(self, dy, dx):
        next_y, next_x = self.ply.y + dy, self.ply.x + dx
        if 0 <= next_y < len(self.maze) and 0 <= next_x < len(self.maze[0]):
            if self.maze[next_y][next_x] in [" ", "E"]:
                self.maze[self.ply.y][self.ply.x] = " "
                self.ply = Pos(next_y, next_x)
                if self.maze[next_y][next_x] == "E":
                    print("Congratulations! You reached the end!")
                    return False
                self.maze[next_y][next_x] = "R"
                self.draw_maze()
        return True

class Pos:
    def __init__(self, y, x):
        self.y = y
        self.x = x

if __name__ == '__main__':
    m = Maze()
    m.draw_maze()
    
    running = True
    while running:
        if keyboard.is_pressed("q"):
            print("Quit Program")
            break
        elif keyboard.is_pressed("w"):
            running = m.move(-1, 0)
        elif keyboard.is_pressed("s"):
            running = m.move(1, 0)
        elif keyboard.is_pressed("a"):
            running = m.move(0, -1)
        elif keyboard.is_pressed("d"):
            running = m.move(0, 1)
        time.sleep(0.1)
