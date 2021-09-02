import turtle
from tkinter import *
import time
import random

Bank_account = 0


class turtle_s:

    def __init__(self, color):
        self.color = color
        self.turt = turtle.Pen()
        self.turt.shape('turtle')
        self.turt.color(color)


red_turtle = turtle_s('red')
blue_turtle = turtle_s('blue')
yellow_turtle = turtle_s('yellow')

turtle_list = [red_turtle, blue_turtle, yellow_turtle]


## Turtle Game Setup
def turtle_stuff():

    turtle.screensize(canvwidth=500, canvheight=500)
    turtle.bgcolor('black')

    for color_turtle in turtle_list:

        if turtle_list.index(color_turtle) % 3 == 0:

            color_turtle.turt.penup()
            color_turtle.turt.setpos(-300, -250)
            color_turtle.turt.left(90)

        elif turtle_list.index(color_turtle) % 3 == 1:

            color_turtle.turt.penup()
            color_turtle.turt.setpos(300, -250)
            color_turtle.turt.left(90)

        else:

            color_turtle.turt.penup()
            color_turtle.turt.setpos(0, -250)
            color_turtle.turt.left(90)


    def turtle_move():

        for color_turtle in turtle_list:

            color_turtle.turt.speed(random.randrange(1, 5))

            if color_turtle == red_turtle:

                start = time.time()

                color_turtle.turt.goto(-300, 250)

                end = time.time()

                red_time_dif = end - start

                print("Red Turtle: {}".format(round(red_time_dif, 5)))

            elif color_turtle == blue_turtle:

                start = time.time()

                color_turtle.turt.goto(300, 250)

                end = time.time()

                blue_time_dif = end - start

                print("Blue Turtle: {}".format(round(blue_time_dif, 5)))


            else:

                start = time.time()

                color_turtle.turt.goto(0, 250)

                end = time.time()

                yellow_time_dif = end - start

                print("Yellow Turtle: {}".format(round(yellow_time_dif, 5)))


        def result():

            if red_time_dif > blue_time_dif and yellow_time_dif:

                if user_turtle_bet.lower() == "red":

                    print("Red turtle wins!\nYou win {} coins!".format(user_bet_amount))
                    Bank_account += user_bet_amount

                else:

                    print("Red turtle wins!\nYou lost {} coins!".format(user_bet_amount))
                    Bank_account -= user_bet_amount

            if blue_time_dif > red_time_dif and yellow_time_dif:

                if user_turtle_bet.lower() == "blue":

                    print("Blue turtle wins!\nYou win {} coins!".format(user_bet_amount))
                    Bank_account += user_bet_amount

                else:

                    print("Blue turtle wins!\nYou lost {} coins!".format(user_bet_amount))
                    Bank_account -= user_bet_amount

            if yellow_time_dif > red_time_dif and blue_time_dif:

                if user_turtle_bet.lower() == "yellow":

                    print("Yellow turtle wins!\nYou win {} coins!".format(user_bet_amount))
                    Bank_account += user_bet_amount

                else:

                    print("Yellow turtle wins!\nYou lost {} coins!".format(user_bet_amount))
    turtle_move()





def enter_input():
    global turtle_bet
    global bet_amount

    turtle_bet = user_turtle_bet.get()
    bet_amount = user_bet_amount.get()
    turtle_stuff() # trigger the turtle code



## Tkinter Entry Setup
tk = Tk()

user_turtle_bet = StringVar()
user_bet_amount = StringVar()

user_turtle_label = Label(tk, text="Turtle Bet", font=('Times', 13, 'bold'))
user_turtle_entry = Entry(tk, textvariable=user_turtle_bet, font=('Times', 13, 'normal'))

user_amount_label = Label(tk, text="Bet Amount", font=('Times', 13, 'bold'))
user_amount_entry = Entry(tk, textvariable=user_bet_amount, font=('Times', 13, 'normal'))

enter_button = Button(tk, text="ENTER", command=enter_input)

user_turtle_label.grid(row=0, column=0)
user_turtle_entry.grid(row=0, column=1)
user_amount_label.grid(row=1, column=0)
user_amount_entry.grid(row=1, column=1)
enter_button.grid(row=2, column=1)

tk.mainloop()










