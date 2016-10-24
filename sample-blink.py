import parallel
import time

def cycle(x, y):
        return x % y < y / 2

p = parallel.Parallel("/dev/parport0")
i = 0

while True:
    i += 1

    r = cycle(i, 100)
    y = cycle(i, 230)
    g = cycle(i, 470)

    v = 0
    if r: v += 1
    if y: v += 2
    if g: v += 4
    p.setData(v)
    time.sleep(0.01)
