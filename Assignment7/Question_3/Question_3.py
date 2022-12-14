import sys
import math
 
w,h = [int(i) for i in input().split()]
input() 
x0 = [int(i) for i in input().split()]
y0 = [int(i) for i in input().split()]
 
# x0 y0 will be used to store the previous position
# and x y the current position
x = x0
y = y0

x_s = range(w)
y_s =  range(h)

def narrow(x0, y0, x, y, x_s, y_s, indx):
    print("narrow : x0={}, y0={}, x={}, y={}, indx={}".format(x0, y0, x, y, indx), file=sys.stderr)
    if len(x_s) != 1:
        if indx == "UNKNOWN":
            pass
        elif indx == "SAME":
            x_s = [i for i in x_s if math.abs(x0-i) == math.abs(x-i)]
        elif indx == "WARMER":
            x_s = [i for i in x_s if math.abs(x0-i) > math.abs(x-i)]
        else:
            x_s = [i for i in x_s if math.abs(x0-i) < math.abs(x-i)]

    else:
        if indx == "UNKNOWN":
            pass
        elif indx == "SAME":
            y_s = [i for i in y_s if math.abs(y0-i) == math.abs(y-i)]
        elif indx == "WARMER":
            y_s = [i for i in y_s if math.abs(y0-i) > math.abs(y-i)]
        else:
            y_s = [i for i in y_s if math.abs(y0-i) < math.abs(y-i)]
    print(x_s, file=sys.stderr)
    print(y_s, file=sys.stderr)
    return x_s, y_s
 
 
while 1:
    indx = input()
    x_s = narrow(x0, y0, x, y, x_s, y_s, indx)
    y_s = narrow(x0, y0, x, y, x_s, y_s, indx)
    x0 = x
    y0 = y
    if len(x_s) != 1:
        if (x0 == 0 and len(x_s) != w):
            x = (3*x_s[0] + x_s[-1])//2 - x0
        elif (x0 == w-1 and len(x_s) != w):
            x = (x_s[0] + 3*x_s[-1])//2 - x0
        else:
            x = x_s[0] + x_s[-1] - x0
        
        if x == x0:
            x = x+1
        x = min(max(x, 0), w-1)
 
    else:
        if x != x_s[0]:
            x = x0 = x_s[0]
            print(x, y)
            indx = input()

        if len(y_s) == 1:
            y = y_s[0]

        else:
            if (y0 == 0 and len(y_s) != h):
                y = (3*y_s[0] + y_s[-1])//2 - y0
            elif (y0 == h-1 and len(y_s) != h):
                y = (y_s[0] + 3*y_s[-1])//2 - y0
            else:
                y = y_s[0] + y_s[-1] - y0
            y = min(max(y, 0), h-1)
    
    print(x, y)