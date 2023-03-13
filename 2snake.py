import turtle
import random
import tkinter
from tkinter import messagebox
import tkinter as tk
from tkinter import *

################################### Mainīgās vērtības ###################################

WIDTH = 600
HEIGHT = 800
DELAY = 400 #Millisikundes starp frame update
FOOD_SIZE = 10

################################### Kustības Offset ###################################

offset = {
    "up": (0,20),
    "down": (0,-20),
    "right": (20,0),
    "left": (-20,0)
}

################################### Snake Kustība ###################################

def go_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"

def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"

def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"

def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"


################################### Snake 2 Izveide ###################################
def go_up2():
    global snake2_direction
    if snake2_direction != "down":
        snake2_direction = "up"

def go_right2():
    global snake2_direction
    if snake2_direction != "left":
        snake2_direction = "right"

def go_down2():
    global snake2_direction
    if snake2_direction != "up":
        snake2_direction = "down"

def go_left2():
    global snake2_direction
    if snake2_direction != "right":
        snake2_direction = "left"




def game_loop():
    global winner, winscore, loser, losescore, highplayer
    stamper.clearstamps() #Izdzēšu uzzīmēto snake
    stamper2.clearstamps()

    new_head=snake[-1].copy()
    new_head[0]+= offset[snake_direction][0] # x koordinātas
    new_head[1]+= offset[snake_direction][1] # y koordinātas

    new_head2=snake2[-1].copy()
    new_head2[0]+= offset[snake2_direction][0]
    new_head2[1]+= offset[snake2_direction][1]
      
    ################################### Highscore Pārbaude ###################################

    if score1 > score2:
        winner = player1
        winscore = score1
        loser = player2
        losescore = score2
    else:
        winner = player2
        winscore = score2
        loser = player1
        losescore = score1 

    ################################### Parbaude Vai Snake Sadursme ###################################

    if new_head[0] < - WIDTH / 2 or new_head[0] > WIDTH / 2 \
       or new_head[1] < - HEIGHT / 2 or new_head[1] > HEIGHT / 2 or new_head2[0] < - WIDTH / 2 or new_head2[0] > WIDTH / 2 \
       or new_head2[1] < - HEIGHT / 2 or new_head2[1] > HEIGHT / 2:
       messagebox.showinfo("Game Over",f"{winner} win! Score:  {winscore}   {loser} lose! Score: {losescore}")
       reset()
    else: #Pievieno jauno galvu

        #Pievieno jauno galvu
        snake.append(new_head)#Iekavās ko gribam pievienot
        snake2.append(new_head2)#Iekavās ko gribam pievienot

        if not food_collision():#Izdzēšam asti
            snake.pop(0) #0, un astes koordinātas
        if not food_collision2():#Izdzēšam asti
            snake2.pop(0) #0, un astes koordināta

        for segment in snake:
            stamper.goto(segment[0],segment[1])
            stamper.stamp()

        for segment in snake2:
            stamper2.goto(segment[0],segment[1])
            stamper2.stamp()
        #Update Screen
        screen.title(f"Snake Game,     {player1} score: {score1}     {player2} score: {score2}             Highscore: {highplayer} score: {highscore}")
        screen.update()


        turtle.ontimer(game_loop,DELAY)


################################### Distances Aprekinasana ###################################

def get_distance(galva, ediens):
    x1, y1 = galva
    x2, y2 = ediens
    distance = ((x2-x1)**2+(y2-y1)**2)**0.5
    return distance


################################### Food Sadursme ###################################

def food_collision():
    global food_pos, score1, food_pos1, food_pos2
    if get_distance(snake[-1], food_pos) < 20:
        score1 += 1
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    if get_distance(snake[-1], food_pos1) < 20:
        score1 += 2
        food_pos1 = get_random_food_pos1()
        food1.goto(food_pos1)
        return True
    if get_distance(snake[-1], food_pos2) < 20:
        score1 += 3
        food_pos2 = get_random_food_pos2()
        food2.goto(food_pos2)
    return False


def food_collision2():
    global food_pos, score2, food_pos1, food_pos2
    if get_distance(snake2[-1], food_pos) < 20:
        score2 += 1
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    if get_distance(snake2[-1], food_pos1) < 20:
        score2 += 2
        food_pos1 = get_random_food_pos1()
        food1.goto(food_pos1)
        return True
    if get_distance(snake2[-1], food_pos2) < 20:
        score2 += 3
        food_pos2 = get_random_food_pos2()
        food2.goto(food_pos2)
    return False


################################### Food Possision ###################################

def get_random_food_pos():
    x = random.randint(- WIDTH/2 + FOOD_SIZE, WIDTH/2 - FOOD_SIZE)
    y = random.randint(- HEIGHT/2 + FOOD_SIZE, HEIGHT/2 - FOOD_SIZE)
    return (x, y)

def get_random_food_pos1():
    x1 = random.randint(- WIDTH/2 + FOOD_SIZE, WIDTH/2 - FOOD_SIZE)
    y1 = random.randint(- HEIGHT/2 + FOOD_SIZE, HEIGHT/2 - FOOD_SIZE)
    return (x1, y1)

def get_random_food_pos2():
    x2 = random.randint(- WIDTH/2 + FOOD_SIZE, WIDTH/2 - FOOD_SIZE)
    y2 = random.randint(- HEIGHT/2 + FOOD_SIZE, HEIGHT/2 - FOOD_SIZE)
    return (x2, y2)

################################### Reset Izveide ###################################

def reset():
    global snake, snake_direction, score1, food_pos, snake2, snake2_direction, highscore, score1, score2, highplayer, winner, food_pos1, food_pos2 
    snake= [[40,0],[40,-20],[40,-40],[40,-60]]
    snake_direction = "up"
    score1 = 0

    food_pos = get_random_food_pos() #dabujam random x un y
    food.goto(food_pos)
    food_pos1 = get_random_food_pos1()
    food1.goto(food_pos1)
    food_pos2 = get_random_food_pos2()
    food2.goto(food_pos2)
    
    
    if winscore > highscore:
        highscore = winscore
        highplayer = winner
    

    snake2 = [[-40,0],[-40,20],[-40,40],[-40,60]]
    snake2_direction = "down"
    score2 = 0
    game_loop()


################################### Set standarts ###################################

player1 = "player1" 
player2 = "player2"
highscore = 0
score1 = 0
score2 = 0
highplayer = "none"
winner = "none"
winscore = 0
loser = "none"
losescore = 0



################################### Ekrāna Izveide ###################################

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake")
screen.bgcolor("#1e0394")
screen.tracer(0) #Disablojām automātisko animāciju

################################### Event Handle Izveide ###################################
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")

screen.onkey(go_up2, "w")
screen.onkey(go_right2, "d")
screen.onkey(go_down2, "s")
screen.onkey(go_left2, "a")

################################### Snake Izveide ###################################

stamper = turtle.Turtle()
stamper.shape("square")
stamper.color("lime")
stamper.penup()

stamper2 = turtle.Turtle()
stamper2.shape("square")
stamper2.color("#f505cd")
stamper2.penup()


################################### Food Izveide ###################################
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(FOOD_SIZE / 20)
food.penup()

food1 = turtle.Turtle()
food1.shape("triangle")
food1.color("black")
food1.shapesize(FOOD_SIZE / 20)
food1.penup()

food2 = turtle.Turtle()
food2.shape("square")
food2.color("green")
food2.shapesize(FOOD_SIZE / 20)
food2.penup()


messagebox.showinfo("Spēles Info", "KUSTĪBA\nSpēlētāja 1 kustība ir ar up, down, left, right bultām\nSpēlētāja 2 kustība ir ar W,S,D,A pogām\nPUNKTI\nAplis dod 1 punktu\nTrijstūris dod 2 punktus,\nKvadrāts dod 3 punktus!\nVeiksmi spēlē!")

################################### Spēlētāja izveide ###################################

def show_entry_fields():
    print("Player1:  %s\nPlayer2: %s" % (e1.get(), e2.get()))
def start():
    global player1, player2
    player1 = e1.get()
    player2 = e2.get()
    
    reset()
    master.protocol("WM_DELETE_WINDOW")

master = tk.Tk()
master.eval('tk::PlaceWindow . center')
master.title("Ievadiet Spēlētāja vārdus")
tk.Label(master, 
         text="Player1", font=('Modern', 20, 'bold')).grid(row=0)
tk.Label(master, 
         text="Player2", font=('Modern', 20, 'bold')).grid(row=1) 


e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)



tk.Button(master, 
          text='Quit', 
          command=quit and master.quit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, 
          text='Start', command=start).grid(row=3, 
                                                       column=3, 
                                                       sticky=tk.W, 
                                                       pady=4)


tk.mainloop()




turtle.done()