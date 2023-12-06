def calculo_impostotot(salario):

        if(salario > 2000 and salario <= 3000):
                resto = salario - 2000
                resultado = resto * 0.08
                return resultado
        elif(salario > 3000 and salario < 4500):
                resto = salario - 3000
                resultado = (1000 * 0.08) + (resto * 0.18)
                return resultado
        else:
                resto = salario - 4500
                resultado =  (1000 * 0.08) + (1500 * 0.18) + (resto * 0.28) 
                return resultado


salario = float(input())

if salario <= 2000.00:
        print('Isento')


else:
       print(f'R$ {calculo_impostotot(salario):.2f}')
    
