continuar = True
print('Bienvenido a la calculadora\nOperacion a realizar:')
while continuar:
    operacion = int(input('1. Suma\n2. Resta\n3. Multiplicacion\n4. Division\n'))
    num1 = float(input('Digite el primer digito: '))
    num2 = float(input('Digite el segundo digito: '))

    if operacion == 1:
        print(f'El resultado de la suma es:{num1+num2}')
    elif operacion == 2:
        print(f'El resultado de la resta es: {num1-num2}')
    elif operacion == 3:
        print(f'El resultado de la multiplicacion es: {num1*num2}')
    else:
        print(f'El resultado de la division es: {num1/num2}')

    continuar = bool(input('Si desea realizar continuar en la calculadora, digite algun numero. De lo contrario oprima enter\n'))    




