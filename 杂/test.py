height = 180
weight = 65
exponent = height/(weight*weight)
print("您的体重是" + str(weight))
print("您的身高是" + str(height))
if exponent < 18.5:
    print("您太轻了")
if exponent >= 18.5 < 29.9:
    print("您有点重")
if exponent >= 29.9:
    print("您太肥了")
