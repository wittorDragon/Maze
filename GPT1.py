import turtle
import time
import keyboard

class MazeGame:
    def __init__(self):
        self.maze = [
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", " ", " ", " ", "X", " ", "X"],
            ["X", " ", "X", " ", "X", " ", " "],
            ["X", " ", "X", " ", "X", " ", "X"],
            ["X", " ", "X", " ", " ", " ", "X"],
            ["X", " ", "X", "X", "X", "X", "X"],
        ]
        self.ply = (5, 1)  # ตำแหน่งผู้เล่น (row, col)
        self.end = (2, 6)  # จุดสิ้นสุด

        self.cell_size = 40  # ขนาดของแต่ละช่องในเขาวงกต
        self.t = turtle.Turtle()
        self.screen = turtle.Screen()
        self.screen.tracer(0)  # ปิด animation เพื่อให้วาดเร็วขึ้น
        self.draw_maze()
        self.draw_player()

    def draw_maze(self):
        """ วาดเขาวงกตจากข้อมูล """
        self.t.penup()
        self.t.goto(-self.cell_size * len(self.maze[0]) // 2, self.cell_size * len(self.maze) // 2)
        
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                self.t.goto(-self.cell_size * (len(row) // 2 - x), self.cell_size * (len(self.maze) // 2 - y))
                if cell == "X":  # กำแพง
                    self.t.pendown()
                    self.t.fillcolor("black")
                    self.t.begin_fill()
                    for _ in range(4):
                        self.t.forward(self.cell_size)
                        self.t.right(90)
                    self.t.end_fill()
                    self.t.penup()
                elif (y, x) == self.end:  # จุดหมาย
                    self.t.write("E", align="center", font=("Arial", 16, "bold"))

    def draw_player(self):
        """ วาดตัวละครที่ตำแหน่งปัจจุบัน """
        y, x = self.ply
        self.t.penup()
        self.t.goto(-self.cell_size * (len(self.maze[0]) // 2 - x) + self.cell_size // 2,
                    self.cell_size * (len(self.maze) // 2 - y) - self.cell_size // 2)
        self.t.pendown()
        self.t.fillcolor("blue")
        self.t.begin_fill()
        self.t.circle(self.cell_size // 4)  # ตัวละครเป็นวงกลม
        self.t.end_fill()
        self.t.penup()
        self.screen.update()

    def move_player(self, dy, dx):
        """ ย้ายตำแหน่งของผู้เล่น """
        y, x = self.ply
        new_y, new_x = y + dy, x + dx

        if 0 <= new_y < len(self.maze) and 0 <= new_x < len(self.maze[0]) and self.maze[new_y][new_x] != "X":
            self.ply = (new_y, new_x)
            self.t.clear()
            self.draw_maze()
            self.draw_player()

            if self.ply == self.end:
                print("🎉 Congraturation! You won!")
                self.t.goto(0, 0)
                self.t.write("You Won!", align="center", font=("Arial", 24, "bold"))
                time.sleep(2)
                turtle.bye()

# เริ่มเกม
game = MazeGame()

# จับคีย์บอร์ดเพื่อเคลื่อนที่
keyboard.add_hotkey("w", lambda: game.move_player(-1, 0))  # ขึ้น
keyboard.add_hotkey("s", lambda: game.move_player(1, 0))   # ลง
keyboard.add_hotkey("a", lambda: game.move_player(0, -1))  # ซ้าย
keyboard.add_hotkey("d", lambda: game.move_player(0, 1))   # ขวา

turtle.mainloop()  # รันเกม

