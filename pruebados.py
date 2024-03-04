import random

def binario_a_decimal(binario):
    decimal = 0
    for i in range(len(binario)):
        if binario[i] == '1':
            decimal += 2**(len(binario) - 1 - i)
    return decimal

def limpiar(numeros_binarios):
    numeros_binarios.clear()

def funcion_a_evaluar(numero):
    resultado = -30 * numero**2 - 23 * numero + 5
    return resultado

def numeroAleatorio():
    numero = random.randint(1, 8)
    return numero

def intercambiar_ultimos_digitos(numero1, numero2, cruzamiento):
    print(f"numero generado {cruzamiento}")
    numero1 = list(numero1)
    numero2 = list(numero2)
    numero1[-cruzamiento:], numero2[-cruzamiento:] = numero2[-cruzamiento:], numero1[-cruzamiento:]
    return ''.join(numero1), ''.join(numero2)

def actualizar_valores_matriz(numeros_binarios_cruzados, parejas):
    for pareja in parejas:
        if len(pareja) == 2:
            cruzamiento = numeroAleatorio()
            _, binario1, _, _ = pareja[0]
            _, binario2, _, _ = pareja[1]
            numeros_binarios_cruzados.append(binario1)
            numeros_binarios_cruzados.append(binario2)

def mostrar_matriz(numeros_binarios_cruzados):
    print("\nMatriz de números binarios:")
    guard = False
    for fila in numeros_binarios_cruzados:
        print(" ".join(fila))

def main():
    numeros_binarios = []
    numeros_binarios_cruzados = []
    numero = 8
    resultados = []
    while True:
        if not numeros_binarios:
            for _ in range(8):
                binario = ''.join(random.choice('01') for _ in range(8))
                numeros_binarios.append(binario)
            for i in range(numero):
                if len(numeros_binarios) < numero:
                    binario = ''.join(random.choice('01') for _ in range(8))
                    numeros_binarios.append(binario)

                binario = numeros_binarios[i]
                es_negativo = random.choice(['0', '1'])
                tiene_decimal = random.choice(['0', '1'])

                numero_decimal = binario_a_decimal(binario)
                if es_negativo == '1':
                    numero_decimal = -numero_decimal
                if tiene_decimal == '1':
                    numero_decimal += 0.5

                resultados.append((i+1, binario, numero_decimal, funcion_a_evaluar(numero_decimal)))
        else:
            resultados.clear()
            numeros_binarios.clear()

            for binario in numeros_binarios_mutados:
                numeros_binarios.append(binario)

            for i in range(numero):
                if len(numeros_binarios) < numero:
                    binario = ''.join(random.choice('01') for _ in range(8))
                    numeros_binarios.append(binario)

                binario = numeros_binarios[i]
                es_negativo = random.choice(['0', '1'])
                tiene_decimal = random.choice(['0', '1'])

                numero_decimal = binario_a_decimal(binario)
                if es_negativo == '1':
                    numero_decimal = -numero_decimal
                if tiene_decimal == '1':
                    numero_decimal += 0.5

                resultados.append((i+1, binario, numero_decimal, funcion_a_evaluar(numero_decimal)))

            numeros_binarios_cruzados.clear()
            numeros_binarios_mutados.clear()

        print("\nResultados de la conversión binario a decimal:")
        print("{:<10} {:<15} {:<15} {:<15}".format("Jerarquía", "Número binario", "Número decimal", "Resultado"))
        for jerarquia, binario, decimal, resultado in resultados:
            print("{:<10} {:<15} {:<15} {:<15.2f}".format(jerarquia, binario, decimal, resultado))

        random.shuffle(resultados)
        parejas = [resultados[i:i+2] for i in range(0, len(resultados), 2)]

        print(f"\nParejas formadas:")
        for index, pareja in enumerate(parejas, 1):
            print(f"\nPareja {index}:")
            print("{:<10} {:<15} {:<15} {:<15}".format("Jerarquía", "Número binario", "Número decimal", "Resultado"))
            for p in pareja:
                jerarquia, binario, decimal, resultado = p
                print("{:<10} {:<15} {:<15} {:<15.2f}".format(jerarquia, binario, decimal, resultado))

            if len(pareja) == 2:
                cruzamiento = numeroAleatorio()
                binario1, binario2 = intercambiar_ultimos_digitos(pareja[0][1], pareja[1][1], cruzamiento)
                print(f"\nnumero generado {cruzamiento}")
                print(f"Pareja {index} después del intercambio:")
                print("{:<10} {:<15} {:<15} {:<15}".format("Jerarquía", "Número binario", "Número decimal", "Resultado"))
                print("{:<10} {:<15} {:<15} {:<15.2f}".format(pareja[0][0], binario1, pareja[0][2], pareja[0][3]))
                print("{:<10} {:<15} {:<15} {:<15.2f}".format(pareja[1][0], binario2, pareja[1][2], pareja[1][3]))
                numeros_binarios_cruzados.append(binario1)
                numeros_binarios_cruzados.append(binario2)

        filas = len(numeros_binarios_cruzados)
        columnas = len(numeros_binarios_cruzados[0])
        matriz_binaria = [[0] * columnas for _ in range(filas)]

        for i in range(filas):
            for j in range(columnas):
                matriz_binaria[i][j] = int(numeros_binarios_cruzados[i][j])

        print("Matriz binaria:")
        for fila in matriz_binaria:
            print(fila)

        for i in range(2):
            num1 = random.randint(0,7)
            num2 = random.randint(0,numero-1)

            if matriz_binaria[num2][num1]==0:
                matriz_binaria[num2][num1]=1
            elif matriz_binaria[num2][num1]==1:
                matriz_binaria[num2][num1]=0

        print("Matriz binaria después de la mutación:")
        for fila in matriz_binaria:
            print(fila)

        numeros_binarios_mutados =[]
        num =""

        for fila in matriz_binaria:
            fila_como_cadena = ''.join(map(str, fila))
            numeros_binarios_mutados.append(fila_como_cadena)

        matriz_binaria.clear()

        continuar = input("\n¿Desea continuar con el ciclo? (s/n): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    main()
