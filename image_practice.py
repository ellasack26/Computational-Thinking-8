# Section 1 - Your code
from utils import *
set_background("Wall_of_china")

s1 = create_sprite("poop_emoji", 150, 100)
s2 = create_sprite("Blobfish", -100, 130)
s2 = create_sprite("shrek", -100, -110)
s2 = create_sprite("flower2", 100, -100)

message1 = create_sprite("alien",-250,200)
message1.color("pink")
message1.write("Hello there",font = ("Arial", 40, "normal"))
message1.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()