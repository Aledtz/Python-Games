print("Welcome to My Dragonball Quiz!")

playing = input("Would you like to play? ")

if playing != "Yes".lower():
    quit()

print("Okay! Let's play!!")
score = 0

answer = input("Who is Goku's first son? ")
if answer == "Gohan".lower():
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the name of the saiyan's home planet? ")
if answer == "Planet Vegeta".lower():
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Who is the prince of all saiyans? ")
if answer == "Vegeta".lower():
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What technique does Goku need to borrow energy in order to execute? ")
if answer == "Spirit Bomb".lower():
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Who is Universe 7's God of Destruction? ")
if answer == "Beerus".lower():
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


print("You got " + str(score) + " questions correct!")
print("You got " + str((score) / 5 * 100) + "%")