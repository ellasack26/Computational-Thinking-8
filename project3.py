from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 =-200
y1 =210
x2 =-200
y2 =120
x3 =-200
y3 =0
x4 =-200
y4 =-150


# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("soccerfield")
t1 = create_sprite("soccerball",x1,y1)
t2 = create_sprite("fish",x2,y2)
t3 = create_sprite("corgi",x3,y3)
t4 = create_sprite("balloon",x4,y4)


# # Section 3 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - explain here which sprites are faster or slower
# X4 will always lose and X1 an d X2 will take turns winning randomly.
for i in range(60):
    x1 +=random.randint(5,10)
    x2 +=random.randint(3,8)
    x3 +=4
    x4 +=2

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.1)


# # Section 4 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
s5 = create_sprite("turtle",-200,-200)
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    s5.write("Player 1 wins!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
    s5.write("player 2 wins!")
elif x3 >= x2 and x3 >= x1 and x3 >= x4:
    s5.write("player 3 wins!")
elif x4 >= x2 and x4 >= x1 and x4 >= x3:
    s5.write("player 4 wins!")


turtle.exitonclick()