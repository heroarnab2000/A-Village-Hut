from graphics import *
import time
import math

def Line(x1, y1, x2, y2):

    if x1 == x2:
        dy = abs(y2 - y1)
        end = dy
    elif y1 == y2:
        dx = abs(x2 - x1)
        end = dx

    xk, yk = x1, y1
    pt = Point(xk, yk)
    pt.draw(win)

    for k in range(2, int(end)):
        if x1 == x2:
            yk += 1
        elif y1 == y2:
            xk += 1
        
        time.sleep(0.001)

        pt = Point(xk, yk)
        pt.setOutline('blue')
        pt.draw(win)

def roof():

    radius = int(math.sqrt((x1-cx)**2 + (y1-cy)**2))
    print("The radius of the circle is ", radius, " units\n")

    xr, yr = cx, abs((radius - abs(cy)))

    x0, y0, xk, yk, i = xr, yr, 0, radius, 0

    Pk = (5/4 - radius)
    check = 1
    xcheck = 0

    while yk <= (int(radius*0.25) + radius):

        if Pk < 0:
            xk += 1
            xr += 1
            Pk += 2*(xk) + 1
        else:
            xk += 1
            yk += 1
            xr += 1
            yr += 1
            i += 2
            Pk += 2*(xk) + 1 - 2*(yk)

        check += 2
        if yk >= (int(radius*0.15) + radius) and check % 3 == 0:
            xr -= 1
            xcheck += 1

        time.sleep(0.001)

        pt1 = Point(xr, yr)
        pt2 = Point(2*x0-xr, yr)
        pt3 = Point(x0+yk -2*radius+xcheck, y0-xk+ radius)
        pt4 = Point(x0+yk -i-xcheck, y0-xk+ radius)

        if xk == 1:
            startx, starty = pt3.x, pt3.y+1
            endx, endy = pt4.x+2, pt4.y+1

        pt1.setOutline('blue')
        pt2.setOutline('blue')
        pt3.setOutline('blue')
        pt4.setOutline('blue')

        pt1.draw(win)
        pt2.draw(win)
        pt3.draw(win)
        pt4.draw(win)

    rad = startx - cx
    colx1, colx2 = startx - int(0.1667 * rad), endx + int(0.1667 * rad)
    coly = starty - rad

    Line(startx, starty, endx, endy)
    Line(colx1, starty, colx1, coly)
    Line(colx2, starty, colx2, coly)
    Line(startx, coly, endx, coly)
    Line(startx, coly, startx, coly+int(0.1667 * rad))
    Line(endx, coly, endx, coly+int(0.1667 * rad))
    Line(startx, coly-int(0.1667 * rad), endx+2, coly-int(0.1667 * rad))

    win.getMouse()
    win.close()


win = GraphWin('A Village Hut', 600, 500)
t1 = Text(Point(300, 50), "Drawing a village Hut")
t2 = Text(Point(300, 75), "Mark the centre of the ceiling and a point on the roof")
t1.draw(win)
t2.draw(win)

c = win.getMouse()
c.draw(win)

p1 = win.getMouse()
p1.draw(win)

cx = int(c.x)
cy = int(c.y)
x1 = int(p1.x)
y1 = int(p1.y)

print(f"\nCenter is: ({cx},{cy}) and Point is: ({x1},{y1})\n")

roof()