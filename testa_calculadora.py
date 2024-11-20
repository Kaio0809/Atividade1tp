import calculadora as calc

def teste():
    operando_b = 10
    operando_a = 20

    print(calc.acumulador)
    print(f'Soma: {calc.soma(operando_a, operando_b)}')
    print(f'Soma acumulador: {calc.soma(operando_b)}')
    print(f'Subtração: {calc.sub(operando_a, operando_b)}')
    print(f'Subtração acumulador: {calc.sub(operando_b)}')
    print(f'Multiplicação: {calc.mult(operando_a, operando_b)}')
    print(f'Multiplicação acumulador: {calc.mult(operando_b)}')
    print(f'Divisão: {calc.div(operando_a, operando_b)}')
    print(f'Divisão acumulador: {calc.div(operando_b)}')
    print(f'Divisão por 0: {calc.div(operando_a, 0)}')

teste()