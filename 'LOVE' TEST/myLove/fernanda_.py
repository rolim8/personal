
print('\n'.join([''.join([('Fernanda'[(x-y) % len('Fernanda')]
    if
        ((x*0.03)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0
    else
        ' ')for x in range(-50, 50)])for y in range(20, -20, -1)]))