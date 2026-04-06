# Section 1 - Your code
from utils import *
player_name = input("What is your name?    ")

set_background("underwater2")

s1 = create_sprite("turtle", 200, 0)
s2 = create_sprite("beta_fish", -200, 0)

s1.color("white")
s2.color("white")
time.sleep(5)

s1.write("Where are we?",font = ("cursive", 10, "normal"))
window.update()
time.sleep(1)

s1.clear()
window.update()
time.sleep(1)

s2.write("UNDER THE SEAAAA!",font = ("cursive", 10, "normal"))
window.update()
time.sleep(1)

s2.clear()
window.update()
time.sleep(1)

s1.write(f"I'm looking for {player_name}",font = ("cursive", 10, "normal"))
window.update()
time.sleep(1)

s1.clear()
s1.write("Have you seen them?",font = ("cursive", 10, "normal"))
window.update()
time.sleep(1)

s1.color("white")
s2.color("white")
time.sleep(5)

s1.write("No idk where they are",font = ("cursive", 10, "normal"))
window.update()
time.sleep(1)

s1.clear()
window.update()
time.sleep(1)

s2.write("yea same lowkenuenly",font = ("cursive", 10, "normal"))
window.update()
time.sleep(1)

s2.clear()
window.update()
time.sleep(1)

s1.color("white")
s2.color("white")
time.sleep(5)

s1.write("well whatevs",font = ("cursive", 10, "normal"))
window.update()
time.sleep(1)

s1.clear()
window.update()
time.sleep(1)

s2.write("yea lets js chill broooooo",font = ("cursive", 10, "normal"))
window.update()
time.sleep(1)

s2.clear()
window.update()
time.sleep(1)

s1.color("white")
s2.color("white")
time.sleep(5)

s1.write("shakkkaaqaaaaa",font = ("cursive", 10, "normal"))
window.update()
time.sleep(1)

s1.clear()
window.update()
time.sleep(1)

s2.write("yeyeyayeyayeyayeqa!",font = ("cursive", 10, "normal"))
window.update()
time.sleep(1)

s2.clear()
window.update()
time.sleep(1)

######################################################################
# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()