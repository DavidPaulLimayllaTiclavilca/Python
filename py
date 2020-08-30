

def run():
    suma_total = 0
    
    primera_opcion = input('''
Presiona [s] para sumar
Presiona [r] para restar
 ''')

    if primera_opcion == 's':
        print('''Puede sumar los números que desee.
Para cerrar el programa sume [0].''')
        sumar = True
        while sumar == True:
            
            numero = float(input('''SUMAR
            '''))
            if numero == 0:
                print('programa cerrado')
                return sumar == False
            if numero != 0:
                suma_total = suma_total + numero 
                print('programa abierto')
                print(suma_total)
                
    if primera_opcion == 'r':
        print('''Puede restar los números que desee.
Para cerrar el programa sume [0].''')
        restar = True
        while restar == True:
            
            numero = float(input('''RESTAR
            '''))
            if numero == 0:
                print('programa cerrado')
                return restar == False
            if numero != 0:
                suma_total = numero - suma_total
                print('programa abierto')
                print(suma_total)

            




if __name__ == '__main__':
    run()
    
