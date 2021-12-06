import random
score = 0
print("WASD is the way you move;'+'represents you position,'*'means the enemy's position;type quit to quit the game！")
print("Game Start！！！")
userX = 0
userY = 0
targetX = random.randint(0, 9)
targetY = random.randint(0, 9)
while True:
    for one in range(0, 10):
        xz = ""
        outStr = ""
        for two in range(0, 10):
            if userX == targetX and userY == targetY:
                targetX = random.randint(0, 9)
                targetY = random.randint(0, 9)
                score += 1
                print("Your score:%d" % score)
            if userX == one and userY == two:
                xz = "+"
            elif targetX == one and targetY == two:
                xz = "*"
            else:
                xz = "-"
            outStr += xz
        print(outStr)
    move = input("Please move or quit：").upper()
    if move == "QUIT":
        break
    elif move == "S" and userX < 9:
        userX += 1
    elif move == "W" and userX > 0:
        userX -= 1
    elif move == "D" and userY < 9:
        userY += 1
    elif move == "A" and userY > 0:
        userY -= 1
    # print(move)
print("Game end, your final score is：{}".format(score))
