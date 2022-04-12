led.plot_brightness(0, 2, 100)
led.plot_brightness(1, 2, 100)
led.plot_brightness(2, 2, 100)
led.plot_brightness(3, 2, 100)
led.plot_brightness(4, 2, 100)
a = [1, 0]
b = [1, 1]
c = [2, 0]
d = [2, 1]
led.plot(a[0], a[1])
led.plot(b[0], b[1])
led.plot(c[0], c[1])
led.plot(d[0], d[1])
led.plot(a[0], 2 + (2 - a[1]))
led.plot(b[0], 2 + (2 - b[1]))
led.plot(c[0], 2 + (2 - c[1]))
led.plot(d[0], 2 + (2 - d[1]))