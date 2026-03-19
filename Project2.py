extrovert_points=0
introvert_points=0
ambivert_points=0

print("Hello, and welcome to the personality quiz that will decide wether you are an extrovert, introvert, or both.")
print("I am just going to ask you a few questions that will figure out what type of personality you have.")
input("press enter to see your first question.")
print(r"----------^----------^----------^----------^----------^----------^----------^----------^----------^----------^")
answer1=input("What is your typical weekend? A: hanging out with a small group of friends and being quiet and on a screen the whole time, B: by yourself at your house reading or watching a movie, or C: hanging out with a big/small group of friends and going somewhere fun?    ")
if answer1 == "A" or answer1 == "a":
    ambivert_points += 1
elif answer1 == "B" or answer1 == "b":
    introvert_points += 1
elif answer1 == "C" or answer1 == "c":
    extrovert_points += 1
print(r"----------^----------^----------^----------^----------^----------^----------^----------^----------^----------^")
answer2=input("What do you like to do before bed? A: Call with friends, B: Read a book in bed, or C: Watch a movie while occasionally texting with friends.    ")
if answer2==input == "A" or answer2 == "a":
    extrovert_points += 1
elif answer2==input == "B" or answer2 == "b":
    introvert_points += 1
elif answer2==input == "C" or answer2 == "c":
    ambivert_points += 1
print(r"----------^----------^----------^----------^----------^----------^----------^----------^----------^----------^")
answer3=input("How do you feel about public speaking? A: Absolutely hate it, B: Not your favorite but will do it if I have to, or C: I love speaking and talking in front of everyone!    ")
if answer2==input == "A" or answer3 == "a":
    introvert_points += 1
elif answer2==input == "B" or answer3 == "b":
    ambivert_points += 1
elif answer2==input == "C" or answer3 == "c":
    extrovert_points += 1
print(r"----------^----------^----------^----------^----------^----------^----------^----------^----------^----------^")
answer4=input("Do you prefer A: Working in a big group (4-6 people), B: working in a small group (2-3 people), or C: Working alone?    ")
if answer2==input == "A" or answer4 == "a":
    extrovert_points += 1
elif answer2==input == "B" or answer4 == "b":
    ambivert_points += 1
elif answer2==input == "C" or answer4 == "c":
    introvert_points += 1
print(r"----------^----------^----------^----------^----------^----------^----------^----------^----------^----------^")
answer5=input("When you are working what do you prefer? A: Loud environment with people talking, B: quiet environment but with music playing, or C: it being completely quiet.    ")
if answer2==input == "A" or answer5 == "a":
    extrovert_points += 1
elif answer2==input == "B" or answer5 == "b":
    ambivert_points += 1
elif answer2==input == "C" or answer5 == "c":
    introvert_points += 1
print(r"----------^----------^----------^----------^----------^----------^----------^----------^----------^----------^")
if extrovert_points > introvert_points and extrovert_points > ambivert_points:
    print("You are an extrovert! You like to hangout with people and you thrive on being around people.")
elif introvert_points > extrovert_points and introvert_points > ambivert_points:
    print("You are a introvert! You like to be alone and have your quite time.")
elif ambivert_points > introvert_points and ambivert_points > extrovert_points:
    print("You are a ambivert! which means you are a mixture of introvert and extrovert. You like to hangout around people but also like time")
print(f"Your score is {introvert_points} for your introvert points, {extrovert_points} for your extrovert points, and {ambivert_points} for your ambivert (which is both extrovert and introvert)")