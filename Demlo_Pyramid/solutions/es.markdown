Este es un problema matematico, donde elevando al cuadrado secuencias de 1 se te dan los numeros demlo. 

* 1 = 1<sup>2</sup>
* 121 = 11<sup>2</sup>
* 12321 = 111<sup>2</sup>

y asi sucesivametne

Como sabemos, al usar strings, la multiplicacion hace que le string se repita n veces, por lo que utilizando en un ciclo for la expresion (int('1'*i))**2) imprimira la piramide de manera corecta.


```
import sys


def demlo_pyramid_maker(n: int):
    if n != 0:
        for i in range(1, n + 1):
            print((int('1'*i))**2)


if __name__ == '__main__':

    levels = int(input())

    demlo_pyramid_maker(levels)


```
