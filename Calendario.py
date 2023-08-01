from calendar import *
año = int(input("Digite el año a ver: "))
print(calendar(año, 2, 1, 8, 3))

# 2 = dos caracteres por dias (lunes, martes,  miercoles, etc)
# 1 = una linea (o fila) por cada semana
# 8 = ocho filas por cada mes
# 3 = tres columnas por todos los meses del año