#input
Y = int(input("Y: "))
X = int(input("X: "))

#processing
if Y==0 and X==0:
    msj="Esta en el origen"
if Y>0 and X>0:
    msj="cuadrante 1"

if Y>0 and X<0:
    msj="cuadrante 2"

if Y<0 and X<0:
    msj="cuadrante 3"
if Y<0 and X>0:
    msj="cuadrante 4"

print(msj)