"Deta 8/01/2025 "
import turtle
import time
PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = 'X'
DEAD_END = '-'

class Maze:
    def __init__(self, maze_file_name):
        rows_in_maze = 0
        columns_in_maze = 0
        self.maze_list = []
        maze_file = open(maze_file_name,'r')
        rows_in_maze = 0
        for line in maze_file:
            row_list = []
            col = 0
            for ch in line[: -1]:
                row_list.append(ch)
                if ch == 'S':
                    self.start_row = rows_in_maze
                    self.start_col = col
                col = col + 1
            rows_in_maze = rows_in_maze + 1
            self.maze_list.append(row_list)
            columns_in_maze = len(row_list)
                    
        self.rows_in_maze = rows_in_maze
        self.columns_in_maze = columns_in_maze
        self.x_translate = - columns_in_maze / 2
        self.y_translate = rows_in_maze / 2
        self.t = turtle.Turtle()
        self.t.shape('turtle')
        self.wn = turtle.Screen()
        self.wn.setworldcoordinates(- (columns_in_maze - 1) / 2 - 5,- (rows_in_maze - 1) / 2 - 5,(columns_in_maze - 1) / 2 + 5,(rows_in_maze - 1) / 2 + 5)
    
    def draw_maze(self):
        self.t.speed(100)
        for y in range(self.rows_in_maze):
            for x in range(self.columns_in_maze):
                if 0 <= y < len(self.maze_list) and 0 <= x < len(self.maze_list[0]):
                    if self.maze_list[y][x] == OBSTACLE:
                        self.draw_centered_box(x + self.x_translate,- y + self.y_translate, 'orange')
        self.t.color('black')
        self.t.fillcolor('blue')
        
    def draw_centered_box(self, x, y, color):
        self.t.up()
        self.t.goto(x - .5, y - .5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()
    
    def move_turtle(self, x, y):
        self.t.up()
        self.t.setheading(self.t.towards(x + self.x_translate,- y + self.y_translate))
        self.t.goto(x + self.x_translate, - y + self.y_translate)
    
    def drop_bread_crumb(self, color):
        self.t.dot(10, color)
   
    def update_position(self, row, col, val=None):
        if val:
            self.maze_list[row][col] = val
        self.move_turtle(col, row)
        if val == PART_OF_PATH:
            color = 'green'
        elif val == OBSTACLE:
            color = 'red'
        elif val == TRIED:
            color = 'blue'
        elif val == DEAD_END:
            color = 'red'
        else:
            color = None
        if color:
            self.drop_bread_crumb(color)
    
    def is_exit(self, row, col):
        return (row == 0 or
                row == self.rows_in_maze - 1 or
                col == 0 or
                col == self.columns_in_maze - 1)
    
    def __getitem__(self,idx):
        return self.maze_list[idx]
    
def search_from(maze, start_row, start_column):
        # try each of four directions from this point until we find a
        # way out.
        # base Case return values:
        # 1. We have run into an obstacle, return false
    maze.update_position(start_row, start_column)
    if maze[start_row][start_column] == OBSTACLE :
        return False
        # 2. We have found a square that has already been explored
    if maze[start_row][start_column] == TRIED or maze[start_row][start_column] == DEAD_END:
        return False
        # 3. We have found an outside edge not occupied by an obstacle
    if maze.is_exit(start_row,start_column):
        maze.update_position(start_row, start_column, PART_OF_PATH)
        return True
    maze.update_position(start_row, start_column, TRIED)
        # Otherwise, use logical short circuiting to try each direction
        # in turn (if needed)
    found = search_from(maze, start_row-1, start_column) or \
        search_from(maze, start_row+1, start_column) or \
        search_from(maze, start_row, start_column-1) or \
        search_from(maze, start_row, start_column+1)
    if found:
        maze.update_position(start_row, start_column, PART_OF_PATH)
    else:
        maze.update_position(start_row, start_column, DEAD_END)
    return found

def next_level():
    turtle.clearscreen()
    turtle.bgcolor("white")

    # แสดงข้อความ Next Level
    turtle.penup()
    turtle.goto(0, 0)
    turtle.color("red")
    turtle.write("Next Level", align="center", font=("Arial", 50, "bold"))
    turtle.hideturtle()

def End():
    turtle.clearscreen()
    turtle.bgcolor("white")

    # แสดงข้อความ Next Level
    turtle.penup()
    turtle.goto(0, 0)
    turtle.color("red")
    turtle.write("congratulations", align="center", font=("Arial", 50, "bold"))
    turtle.hideturtle()

def clear():
    turtle.clearscreen()
    turtle.bgcolor("white")

if __name__ == "__main__":
    
    maze_1 = Maze('maze.txt')
    maze_1.draw_maze()
    maze_1.update_position(maze_1.start_row, maze_1.start_col)
    search_from(maze_1, maze_1.start_row, maze_1.start_col)
    next_level()
    time.sleep(2)
    clear()

    maze_2 = Maze('maze2.txt')
    maze_2.draw_maze()
    maze_2.update_position(maze_2.start_row, maze_2.start_col)
    search_from(maze_2, maze_2.start_row, maze_2.start_col)
    next_level()
    time.sleep(2)
    clear()

    maze_3 = Maze('maze3.txt')
    maze_3.draw_maze()
    maze_3.update_position(maze_3.start_row, maze_3.start_col)
    search_from(maze_3, maze_3.start_row, maze_3.start_col)
    next_level()
    time.sleep(2)
    clear()

    maze_4 = Maze('maze4.txt')
    maze_4.draw_maze()
    maze_4.update_position(maze_4.start_row, maze_4.start_col)
    search_from(maze_4, maze_4.start_row, maze_4.start_col)
    next_level()
    time.sleep(2)
    clear()
    End()
    
    # maze_5 = Maze('maze5.txt')
    # maze_5.draw_maze()
    # maze_5.update_position(maze_5.start_row, maze_5.start_col)
    # search_from(maze_5, maze_5.start_row, maze_5.start_col)
    # next_level()
    # time.sleep(2)
    # clear()

    # maze_6 = Maze('maze6.txt')
    # maze_6.draw_maze()
    # maze_6.update_position(maze_6.start_row, maze_6.start_col)
    # search_from(maze_6, maze_6.start_row, maze_6.start_col)
    # next_level()
    # time.sleep(2)
    # clear()

    # maze_7 = Maze('maze7.txt')
    # maze_7.draw_maze()
    # maze_7.update_position(maze_7.start_row, maze_7.start_col)
    # search_from(maze_7, maze_7.start_row, maze_7.start_col)
    # next_level()
    # time.sleep(2)
    # clear()

    # maze_8 = Maze('maze8.txt')
    # maze_8.draw_maze()
    # maze_8.update_position(maze_8.start_row, maze_8.start_col)
    # search_from(maze_8, maze_8.start_row, maze_8.start_col)
    # End()



    