def sumall(*args):
    sumis = 0
    for num in args:
        sumis += num
    return sumis


print(sumall(2, 5))
