print("Welcome to my short pop culture 2023 music game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play")
print("Remember no cheating:)")
score = 0

answer = input("What is Nicki Minaj's most recent song? ")
if answer.lower() == "barbie world":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is Ice Spice's most recent song? ")
if answer.lower() == "deli":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is Beyoncé's most recent album? ")
if answer.lower() == "renaissance":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/3)*100) + "%.")
