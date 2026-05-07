from utils import *

# Section 1 - setup
# TODO - set a background using set_background()
set_background("mall")
# TODO - create at least two variables and set their starting value. ex: cookies = 0
#My game you press the space button to get money and once you have enough money you can buy some clothes
Money=0
Clothes=20

# OPTIONAL: use this invisible alien to say a message
m1 = create_sprite("alien", -250,200)
m1.hideturtle()
m2 = create_sprite("balloon", -250,230)
m2.hideturtle()

# Section 2 - controls
# TODO - define an action. ex: def my_control()
#if you press space it adds more money to the money variable so you can get clothes.
def get_money():
    # This adds 2 to the money variable and money appears in a random spot
    global Money
    Money += 1
    x=random.randint(-200,200)
    y=random.randint(-200,200)
    s1=create_sprite("money",x,y)
    time.sleep(0.1)
    s1.hideturtle()


# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")
window.onkeypress(get_money, "space")
#You press C to buy some clothes if you have enough money
# # TODO - make a second control
def buy_clothes():
    global Money, Clothes
    if Money>=Clothes:
        Money-=20
        y=(-250)
        x=random.choice([-250,-200,-150,-50,0,50,100,150,200,250])
        create_sprite("shopping_bag",x,y)
window.onkeypress(buy_clothes, "c")



# Section 3 - game loop
window.listen()
for i in range(1000000000):
    
    # TODO - put any automatic actions here


    # OPTIONAL - use the message sprite to say a message
    m1.clear()
    m1.color("white")
    m1.write(f"Money is {Money}",font=("Arial",20,"normal"))
    m2.clear()
    m2.color("white")
    m2.write(f"Cost:20",font=("Arial",20,"normal"))

    time.sleep(0.01)
    window.update()