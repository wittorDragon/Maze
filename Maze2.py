import os
import time
import keyboard
import turtle

class maze:
    def __init__(self) -> None:
        self.maze = [
                    ["X", "X", "X", "X", "X", "X", "X"],
                    ["X", " ", " ", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", "X", " ", " "],
                    ["X", " ", "X", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", " ", " ", "X"],
                    ["X", " ", "X", "X", "X", "X", "X"],
                    ]
                 
        self.ply = pos(5, 1)
        self.end = pos(2, 6)
        self.maze[self.ply.y][self.ply.x] = "R"
        self.maze[self.end.y][self.end.x] = "E"
    
    def isInBound(self, y, x):
        if y>=0 and x>=0 and y<len(self.maze) and x<len(self.maze[0]):
            return True
        else:
            return False
    # def turtle(self):
    #     from turtle import
    #     return
    # P = turtle.Turtle()

    
    def print(self):
        os.system("cls")
        print("\n\n\n")
        for row in self.maze:
            for col in row:
                print(col," ", end="")
            print("")
        print("\n\n\n")
    
    def printEND(self):
        os.system("cls")
        print("\n\n\n")
        print(">>>>> Congraturation!!! <<<<<")
        print("\n\n\n")
        keyboard.wait("")

        
    def printNext(self):
        # os.system("cls")
        print("\n\n\n")
        print(">>>>> Next Level <<<<<")
        print("\n\n\n")


        
    def find_path(self):# อัลกอริทึม BFS (Breadth-First Search)
        from Queue import Queue  

        queue = Queue()
        queue.enqueue((self.ply, []))  

        visited = set()  
        visited.add((self.ply.y, self.ply.x))

        while not queue.isEmpty():
            current_pos, path = queue.dequeue()

        
            if self.maze[current_pos.y][current_pos.x] == "E":
                return path

        
            directions = [("up", -1, 0), ("down", 1, 0), ("left", 0, -1), ("right", 0, 1)]

            for direction, dy, dx in directions:
                next_y, next_x = current_pos.y + dy, current_pos.x + dx

                if self.isInBound(next_y, next_x) and (next_y, next_x) not in visited:
                    if self.maze[next_y][next_x] in [" ", "E"]:
                        queue.enqueue((pos(next_y, next_x), path + [direction]))
                        visited.add((next_y, next_x))

        return []  


    def move_up(self):
        next_move = pos(self.ply.y-1, self.ply.x)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True
    
    def move_down(self):
        next_move = pos(self.ply.y+1, self.ply.x)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True

    def move_left(self):
        next_move = pos(self.ply.y, self.ply.x-1)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True

    def move_right(self):
        next_move = pos(self.ply.y, self.ply.x+1)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True

class pos:
    def __init__(self) -> None:
        self.y = None
        self.x = None
    
    def __init__(self, y, x) -> None:
        self.y = y
        self.x = x

if __name__ == '__main__':
    
    print("move_up 'W'")
    print("move_down 'S'")
    print("move_left 'A'")
    print("move_right 'D'")
    print("move_Auto 'M'")
    
    m = maze()
    m.print()
    path = m.find_path()


    while True:
        if keyboard.is_pressed("q"):
            print("Quit Program")
            break
        if keyboard.is_pressed("w"):
            if m.move_up():
                m.print()
            else:
                break
        if keyboard.is_pressed("s"):
            if m.move_down():
                m.print()
            else:
                break
        if keyboard.is_pressed("a"):
            if m.move_left():
                m.print()
            else:
                break
        if keyboard.is_pressed("d"):
            if m.move_right():
                m.print()
            else:
                break
            
        if keyboard.is_pressed("m"):
            for step in path:
                if step == "up":
                    m.move_up()
                elif step == "down":
                    m.move_down()
                elif step == "left":
                    m.move_left()
                elif step == "right":
                    m.move_right()
                m.print()  # แสดงผลเขาวงกต
                time.sleep(0)  # หน่วงเวลาเล็กน้อย
            m.printNext()
            time.sleep(2)

# print("move_up 'W'")
# print("move_down 'S'")
# print("move_left 'A'")
# print("move_right 'D'")
# print("move_Auto 'M'")