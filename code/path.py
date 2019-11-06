import math
import kinematic as kine


mypathX = []
mypathY = []
mypathZ = []

NUMERO_PUNTOS = 10.0

xi = float(input("dame x inicial "))
xf = float(input("dame x final "))
yi = float(input("dame y inicial "))
yf = float(input("dame y final "))
zi = float(input("dame z inicial "))
zf = float(input("dame z final "))

incrementoX = (xf - xi)/NUMERO_PUNTOS
incrementoY = (yf - yi)/NUMERO_PUNTOS
incrementoZ = (zf - zi)/NUMERO_PUNTOS
print(incrementoX)
print(incrementoY)
print(incrementoZ)
print ('')


# Puntos de X
if xi == xf:
    i = 0
    while i <= NUMERO_PUNTOS:
        mypathX.append(xi)
        i += 1
else:
    if xi < xf:
        xi = xi + incrementoX
        while xi <= xf:
            mypathX.append(xi)
            xi = xi + incrementoX
    else:
        xi = xi + incrementoX
        while xi >= xf:
            mypathX.append(xi)
            xi = xi + incrementoX

for p in mypathX:
    print (p)
print("")

# Puntos de Y
if yi == yf:
    i = 0
    while i <= NUMERO_PUNTOS:
        mypathY.append(yi)
        i += 1
else:
    if yi < yf:
        yi = yi + incrementoY
        while yi <= yf:
            mypathY.append(yi)
            yi = yi + incrementoY
    else:
        yi = yi + incrementoY
        while yi >= yf:
            mypathY.append(yi)
            yi = yi + incrementoY

for p in mypathY:
    print(p)
print("")

# Puntos de Z
if zi == zf:
    i = 0
    while i <= NUMERO_PUNTOS:
        mypathZ.append(zi)
        i += 1
        print ('hola')
else:
    if zi < zf:
        zi = zi + incrementoZ
        while zi <= zf:
            mypathZ.append(zi)
            zi = zi + incrementoZ
    else:
        zi = zi + incrementoZ
        while zi >= zf:
            mypathZ.append(zi)
            zi = zi + incrementoZ

for p in mypathZ:
    print(p)
print("")

# Calculo de los angulos para cada punto

angulos = []    #lista con los angulos que hay que dar
n = 0
while n < NUMERO_PUNTOS:
    [alpha1, alpha2, alpha3] = kine.inverseKine(mypathX[n], mypathY[n], mypathZ[n])
    angulos.append(alpha1)
    angulos.append(alpha2)
    angulos.append(alpha3)
    n = n + 1

for p in angulos:
    print(p)
print("")


# Funcion de movimiento en linea recta
def moveToPoint(self):
    pathX = []
    pathY = []
    pathZ = []

    self.vectorAngles[0] = self.m0.position
    print(Pata.vectorAngles[0])
    self.vectorAngles[1] = self.m1.position
    print(Pata.vectorAngles[1])
    self.vectorAngles[2] = self.m2.position
    print(Pata.vectorAngles[2])
    self.getFK_pos(self.vectorAngles)

    xi = self.vectorPosition[0]
    xf = float(input("dame x final "))
    yi = self.vectorPosition[1]
    yf = float(input("dame y final "))
    zi = self.vectorPosition[2]
    zf = float(input("dame z final "))

    incrementoX = math.fabs(xf - xi) / Pata.NUMERO_PUNTOS
    incrementoY = math.fabs(yf - yi) / Pata.NUMERO_PUNTOS
    incrementoZ = math.fabs(zf - zi) / Pata.NUMERO_PUNTOS

    # Puntos de X
    if xi < xf:
        xi = xi + incrementoX
        while xi <= xf:
            pathX.append(xi)
            xi = xi + incrementoX
    else:
        xi = xi - incrementoX
        while xi >= xf:
            pathX.append(xi)
            xi = xi - incrementoX

    for p in pathX:
        print(p)
    print("")

    # Puntos de Y
    if yi < yf:
        yi = yi + incrementoY
        while yi <= yf:
            pathY.append(yi)
            yi = yi + incrementoY
    else:
        yi = yi - incrementoY
        while yi >= yf:
            pathY.append(yi)
            yi = yi - incrementoY

    for p in pathY:
        print(p)
    print("")

    # Puntos de Z
    if zi < zf:
        zi = zi + incrementoZ
        while zi <= zf:
            pathZ.append(zi)
            zi = zi + incrementoZ
    else:
        zi = zi - incrementoZ
        while zi >= zf:
            pathZ.append(zi)
            zi = zi - incrementoZ

    for p in pathZ:
        print(p)
    print("")

    # Calculo de los angulos para cada punto

    angles = []  # lista con los angulos que hay que dar
    n = 0
    while n < Pata.NUMERO_PUNTOS:
        [alpha0, alpha1, alpha2] = Pata.getIK_angles([pathX[n], pathY[n], pathZ[n]], self.ElbowPos.ElbUp)
        angles.append(alpha0)
        angles.append(alpha1)
        angles.append(alpha2)
        n = n + 1

    for p in angles:
        print(p)
    print("")

