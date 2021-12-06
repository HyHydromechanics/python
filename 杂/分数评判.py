number = input
number = input('write your number')
while number == int(number):
    if 100 >= number >= 90:
        print("A")
        print('next')
    elif 90 > number >= 70:
            print("B")
            print('next')
    if 70 > number >= 60:
        print("C")
        print('next')
    elif 60 > number >= 0:
            print("D")
            print('next')
    if number > 100 or number < 0:
            print('error')
print('over')
print('next')
