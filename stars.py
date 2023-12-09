from random import randint
stars = []
star = ' * '
space = ' '

for i in range(100):
    rand_1 = randint(0, 50)
    for i in range(rand_1):
        rand_2 = randint(0,15)
        spaces = space * rand_2
        stars.append(spaces)
        stars.append(star)
    print(*stars, sep=' ')
    stars.clear()


