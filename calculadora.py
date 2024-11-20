
acumulador = 0.0 

def soma(b,  a = None):
    global acumulador

    if a is None:
        acumulador = acumulador + b
    else:
        acumulador =  a + b
    return acumulador

def sub(b, a = None):
    global acumulador

    if a is None:
        acumulador = acumulador - b
    else:
        acumulador =  a - b
    return acumulador

def mult(b, a = None):
    global acumulador

    if a is None:
        acumulador = acumulador*b
    else:
        acumulador =  a * b
    return acumulador

def div(b, a = None):
    if b == 0:
        return "Erro de Divisão por zero!"
    global acumulador

    if a is None:
        acumulador = acumulador / b
    else:
        acumulador =  a / b
    return acumulador