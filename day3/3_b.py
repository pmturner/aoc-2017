x = 0
y = 0
dx = 0
dy = -1
grid = {}
sum_value = 1
coord_check = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]

while sum_value < 277678:
    grid[(x,y)] = sum_value

    for check in coord_check:
        check_x, check_y = check

        if (x + check_x, y + check_y) in grid:
            sum_value += grid[(x + check_x, y + check_y)]

    if (x == y) or (x < 0 and x == -y) or (x > 0 and x == 1-y):
        dx, dy = -dy, dx
    x, y = x + dx, y + dy

print(sum_value)
    