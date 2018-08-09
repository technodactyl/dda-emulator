import decimal
from random import randint

def make_grid():
    grid = []
    for i in range(50):
        pixel_row = []
        for j in range(50):
            pixel_row.append("-")
        grid.append(pixel_row)
    return grid

screen = make_grid()

def dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    adx = abs(dx)
    ady = abs(dy)
    if (adx > ady):
        L = adx
    elif (ady > adx):
        L = ady
    else:
        h = randint(1,2)
        if(h == 1):
            L = adx
        else:
            L = ady
    plotx = x1
    ploty = y1
    xinc = dx/L
    yinc = dy/L
    rplotx = plotx
    rploty = ploty
    i=1
    while(True):
#        print("Iteration " + str(i))
#        print("Point: ", end="\t")
#        print(str(plotx), end="\t")
#        print(str(ploty))
#        print("Pixel: ", end="\t")
#        print(str(rplotx - 1), end="\t")
#        print(str(rploty - 1))
        screen[49 - (rploty-1)][rplotx-1] = "o"
#        print("Plotted!")
        if(rplotx == x2 and rploty == y2):
            break
        else:
            pass
        plotx = plotx + xinc
        ploty = ploty + yinc
#        print("New Point: ", end="\t")
#        print(str(plotx), end="\t")
#        print(str(ploty))
        rplotx = int((decimal.Decimal(plotx)).quantize(decimal.Decimal('1'), rounding=decimal.ROUND_HALF_UP))
        rploty = int((decimal.Decimal(ploty)).quantize(decimal.Decimal('1'), rounding=decimal.ROUND_HALF_UP))
#        print("Rounded Point: ", end="\t")
#        print(str(rplotx), end="\t")
#        print(str(rploty))
#        print("New Pixel: ", end="\t")
#        print(str(rplotx - 1), end="\t")
#        print(str(rploty - 1))
#        print("_________________________")
        i += 1

xa = input("Give x-coordinate of first point: ")
ya = input("Give y-coordinate of first point: ")
xb = input("Give x-coordinate of second point: ")
yb = input("Give y-coordinate of second point: ")

dda(int(xa), int(ya), int(xb), int(yb))

for r in screen:
    print(*r)
