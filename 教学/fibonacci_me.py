# F(n)=F(n - 1)+F(n - 2) （n ≥ 2，n ∈ N*）

def fibonacci_me(nums):
    fibs = [0, 1]
    fibs_1 = [fibs - 2]
    fibs_2 = [fibs - 1]
    for i in range(nums - 2):
        fibs.append(list[int | fibs_1] + list[int | fibs_2])

    print(fibs)


fibonacci_me(30)
