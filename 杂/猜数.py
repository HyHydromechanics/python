import random
sercet = random.randint(0,10)
print('你好')
temp = input('我刚刚想了一个数，是0-4以内的数字，来猜猜吗')
guess = int(temp)
while guess != sercet:
    temp = input('对不起，你错了，以后我会给你一点提示')
    guess = int(temp)
    if guess == sercet:
        print('哦！')
        print('恭喜，答对了')
    else:
        if guess > sercet:
            print('这个数字有点大了')
        else:
            print('这个数字有点小了')
print("游戏结束！")
print("还想试试吗")
