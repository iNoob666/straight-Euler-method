import matplotlib.pyplot as plt
import math

def function(t, y):
    return 2.0 * t * y


def analytic(t):
    y = math.exp(t * t)
    return y


def methodOfEuler(h, yn, t):
    yNew = yn + h * function(t, yn)
    return yNew


def methodOfEulerModified(h, yn, t):
    yNew = yn + h / 2 * (function(t, yn) + function(t + h, yn + h * function(t, yn)))
    return yNew


def methodOfEulerImproved(h, yn, t):
    yNew = yn + h * function(t + h / 2, yn + h / 2 * function(t, yn))
    return yNew


x = [float(0)]

yEuler = [float(1)]
yEulerModified = [float(1)]
yEulerImproved = [float(1)]
yAnalytic = [float(1)]

h1Fault = [float(0)]
h2Fault = [float(0)]
h3Fault = [float(0)]
h = [0.1, 0.05, 0.025]

graphs = plt.figure(figsize=(20, 20))

for j in h:
    for i in range(len(x) - 1, len(x) + int(1 / j)):
        x.append(x[i] + j)
        yAnalytic.append(analytic(x[i + 1]))

        yEuler.append(methodOfEuler(j, yEuler[i], x[i]))
        h1Fault.append(abs(yEuler[i + 1] - yAnalytic[i + 1]))

        yEulerModified.append(methodOfEulerModified(j, yEulerModified[i], x[i]))
        h2Fault.append(abs(yEulerModified[i + 1] - yAnalytic[i + 1]))

        yEulerImproved.append(methodOfEulerImproved(j, yEulerImproved[i], x[i]))
        h3Fault.append(abs(yEulerImproved[i + 1] - yAnalytic[i + 1]))

    x.append(float(0))

    yEuler.append(float(1))
    yEulerModified.append(float(1))
    yEulerImproved.append(float(1))
    yAnalytic.append(float(1))

    h1Fault.append(float(0))
    h2Fault.append(float(0))
    h3Fault.append(float(0))

n1 = int(1/h[0])
n2 = int(1/h[1])
n3 = int(1/h[2])

step = graphs.add_subplot(3, 2, 1)
step.set_title("Euler")
line1, line2, line3 = step.plot(x[0: n1+1], yEuler[0: n1+1], 'r',
                                x[n1+2: n1+n2+3], yEuler[n1+2: n1+n2+3], 'g',
                                x[n1+n2+4: len(x)-2], yEuler[n1+n2+4: len(x)-2], 'k')
plt.legend((line1, line2, line3), ("h = 0.1", "h = 0.05", "h = 0.025"), loc="best")
plt.grid()

step = graphs.add_subplot(3, 2, 3)
step.set_title("Euler modified")
line1, line2, line3 = step.plot(x[0: n1+1], yEulerModified[0: n1+1], 'r',
                                x[n1+2: n1+n2+3], yEulerModified[n1+2: n1+n2+3], 'g',
                                x[n1+n2+4: len(x)-2], yEulerModified[n1+n2+4: len(x)-2], 'k')
plt.legend((line1, line2, line3), ("h = 0.1", "h = 0.05", "h = 0.025"), loc="best")
plt.grid()

step = graphs.add_subplot(3, 2, 5)
step.set_title("Euler improved")
line1, line2, line3 = step.plot(x[0: n1+1], yEulerImproved[0: n1+1], 'r',
                                x[n1+2: n1+n2+3], yEulerImproved[n1+2: n1+n2+3], 'g',
                                x[n1+n2+4: len(x)-2], yEulerImproved[n1+n2+4: len(x)-2], 'k')
plt.legend((line1, line2, line3), ("h = 0.1", "h = 0.05", "h = 0.025"), loc="best")
plt.grid()

step = graphs.add_subplot(3, 2, 2)
step.set_title("Euler fault")
line1, line2, line3 = step.plot(x[0: n1+1], h1Fault[0: n1+1], 'r',
                                x[n1+2: n1+n2+3], h1Fault[n1+2: n1+n2+3], 'g',
                                x[n1+n2+4: len(x)-2], h1Fault[n1+n2+4: len(x)-2], 'k')
plt.legend((line1, line2, line3), ("h = 0.1", "h = 0.05", "h = 0.025"), loc="best")
plt.grid()

step = graphs.add_subplot(3, 2, 4)
step.set_title("Euler modified fault")
line1, line2, line3 = step.plot(x[0: n1+1], h2Fault[0: n1+1], 'r',
                                x[n1+2: n1+n2+3], h2Fault[n1+2: n1+n2+3], 'g',
                                x[n1+n2+4: len(x)-2], h2Fault[n1+n2+4: len(x)-2], 'k')
plt.legend((line1, line2, line3), ("h = 0.1", "h = 0.05", "h = 0.025"), loc="best")
plt.grid()

step = graphs.add_subplot(3, 2, 6)
step.set_title("Euler improved fault")
line1, line2, line3 = step.plot(x[0: n1+1], h3Fault[0: n1+1], 'r',
                                x[n1+2: n1+n2+3], h3Fault[n1+2: n1+n2+3], 'g',
                                x[n1+n2+4: len(x)-2], h3Fault[n1+n2+4: len(x)-2], 'k')
plt.legend((line1, line2, line3), ("h = 0.1", "h = 0.05", "h = 0.025"), loc="best")
plt.grid()

plt.savefig("example.png")
plt.show()
