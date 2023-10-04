Entero = 123
Flotante = 1.23
Boleano = True
Cadena = "Hola Como Estas"

cadena_int = str(Entero)
cadena_float = str(Flotante)
cadena_boolean = str(Boleano)

Resultado = Cadena + " " + cadena_int + " " + cadena_float + " " +cadena_boolean


print(Resultado)

#En Python 3, los enteros no tienen un límite superior en términos de valor, lo que significa que pueden crecer tanto como lo permita la memoria de la máquina


#En la mayoría de las máquinas, el valor máximo representable para un flotante de precisión doble (float64) es aproximadamente 1.8 x 10^308

n = int(input("Ingresa un número entero n: "))

suma = n * (n + 1)

print(f"La suma de los primeros {n} números pares es: {suma}")