import turtle, math , random

wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Tank Wars")
wn.setup(700, 700)
wn.tracer(0)



turtle.register_shape("Green tank left side.gif")
turtle.register_shape("coins.gif")
turtle.register_shape("Green tank right side.gif")
turtle.register_shape("horizontal_enemy.gif")
turtle.register_shape("The exit door.gif")
turtle.register_shape("vertical_enemy left side.gif")
turtle.register_shape("vertical_enemy right side.gif")
turtle.register_shape("horizontal_enemy facing up.gif")

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)
        
class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("coins.gif")
        self.color("purple")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x,y)
        
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()


class Player1(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("The exit door.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        
    def is_collsion(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt(( a ** 2 ) + ( b ** 2))

class Horizontal_enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("horizontal_enemy.gif")
        self.color("green")
        self.penup()
        self.speed(0)
        self.point = 50
        self.goto(x,y)
        self.direction = (["up","down"])
        
        
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
            self.shape("horizontal_enemy facing up.gif")
        elif self.direction == "down":
            dx = 0
            dy = -24
            self.shape("horizontal_enemy.gif")
        else:
            dx = 0 
            dy = 0
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy
        
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
        else:
            self.directions = random.choice("up","down")
        turtle.ontimer(self.move, t = random.randint(100, 300))
            
    def is_collsion(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt(( a ** 2 ) + ( b ** 2))
        
            
class Vertical_enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("vertical_enemy left side.gif")
        self.color("yellow")
        self.penup()
        self.speed(0)
        self.point = 50
        self.goto(x,y)
        self.direction = random.choice(["left","right"])
        
        
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()
    
    def is_collsion(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt(( a ** 2 ) + ( b ** 2))
    
    def move(self):
        if self.direction == "left":
            dx = 24
            dy = 0
            self.shape("vertical_enemy left side.gif")
        elif self.direction == "right":
            dx = -24
            dy = 0
            self.shape("vertical_enemy right side.gif")
        else:
            dx = 0
            dy = 0
            
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy
        
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
        else:
            self.direction = random.choice(["left","right"])
        turtle.ontimer(self.move, t =random.randint(100,300))


class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("Green tank right side.gif")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold = 0
        self.shapesize(stretch_wid=5,stretch_len=5)

    def go_up(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)

    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
        
    def go_right(self):
        move_to_x = player.xcor() -24
        move_to_y = player.ycor()
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
            self.shape("Green tank left side.gif")

    def go_left(self):
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()
        
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
            self.shape("Green tank right side.gif")
    
    def is_collsion(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt(( a ** 2 ) + ( b ** 2))
        
        if distance < 5:
            return True
        else:
            return False
        

level = [""]
level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXX",
    "XTH TX V  XX  XQ    XX X",
    "X    X  X   T X  X    VX",
    "XT XXX  XXX  XXXXXX T XX",
    "X     T   T  T   V X  XX",
    "XXXXXX  XXXX  XXX  XT  X",
    "X     T  V   T  X   X  X",
    "X PXXXXH  XXX     XXv  X",
    "X T   V  XV  T XT    XXX",
    "XXXXXXXXXXXXXXXXXXXXXXXX",
]
horizontal_enemys = []
vertical_enemys = []
treasures = []

level.append(level_1)


def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            Character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)
            if Character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x,screen_y))
            elif Character == "P":
                player.goto(screen_x, screen_y)
            elif Character == "Q":
                player1.goto(screen_x, screen_y)
            elif Character == "H":
                horizontal_enemys.append(Horizontal_enemy(screen_x,screen_y))
            elif Character == "V":
                vertical_enemys.append(Vertical_enemy(screen_x,screen_y))
            elif Character == "T":
                treasures.append(Treasure(screen_x,screen_y))
                
                


pen = Pen()
player = Player()
player1 = Player1()


walls = []

setup_maze(level[1])
print(walls)

turtle.listen()
turtle.onkey(player.go_left, "d")
turtle.onkey(player.go_right, "a")
turtle.onkey(player.go_down, "s")
turtle.onkey(player.go_up, "w")

for Vertical_enemy in vertical_enemys:
    turtle.ontimer(Vertical_enemy.move, t =250)

for Horizontal_enemy in horizontal_enemys:
    turtle.ontimer(Horizontal_enemy.move, t =250)

while True:
    for Treasure in treasures:
        if player.is_collsion(Treasure):
            player.gold += Treasure.gold
            print("Player Gold: {}".format(player.gold))
            Treasure.destroy()
            treasures.remove(Treasure)
               
    for Vertical_enemy in vertical_enemys:
        if player.is_collsion(Vertical_enemy):
            print("Player Dies!")

    for Horizontal_enemy in horizontal_enemys:
        if player.is_collsion(Horizontal_enemy):
            print("Player Dies!")
            

        
   
    wn.update()
