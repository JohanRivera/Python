clave = 'p4ssw0rd'
intentos = 0
while intentos < 3:
    if input(f'Intento {intentos + 1}, digite la clave: ').lower() == clave:
        intentos = 4
    else: 
        print(f'Intento {intentos +1 } fallido, le quedan {2-intentos} intentos')
        intentos+=1 
if intentos == 3:
    print('Ha superado el numero de intentos posibles, buena suerte a la proxima')
else:
    print('Clave correcta, puede ingresar')
