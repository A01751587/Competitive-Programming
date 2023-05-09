# Problema: occ11nssf32
# OmegaUp

import sys

# Asociado a un archivo, se lee su contenido completo read()
s = (int(x) for x in sys.stdin.read().split())

n = next(s)
suma = 0
for _ in range(n):
    suma += next(s)
print(suma)
