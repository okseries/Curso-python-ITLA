import saludar
import modulo_calculadora


op = input("Elija una opcion: (1: suma, 2: resta): ")


if op == '1':
    a = float(input('Prime numero: '))
    b = float(input('Segundo numero: '))
    modulo_calculadora.suma(a,b)

