def func(time):
    litter = 5
    if time == 1:
        return 1
    if time == 0:
        return 0
    else:
        return func(time - 1, ) + func(time - 2) * litter


print(func(30))
