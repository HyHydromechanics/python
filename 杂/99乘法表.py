print("99乘法表")
for i in range(1, 10):
    for f in range(1, i+1):
        print(str(f) + "×" + str(i) + "=" + str(i*f) + "\t", end="")
    print("")
print("\n")

print("99除法表-保留一位小数")
for a in range(1, 10):
    for b in range(1, a+1):
        step1 = str(b/a)
        print(str(b) + "/" + str(a) + "=" + step1[0:3] + "\t", end="")
    print("")
print("\n")

print("1~9的平方")
for c in range(1,10):
    step2 = str(c**2)
    print(str(c)+ "的平方是" + step2 + "\t")
print("\n")
