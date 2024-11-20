import matematica as m
from matematica.estatistica import media

def teste():
    n1 = 10
    n2 = 20

    print(f"A soma de {n1} e {n2} é {m.soma(n1,n2)}")
    print(f"A Subtração de {n1} e {n2} é {m.sub(n2,n1)}")
    print(f"A área de um círculo com área {m.soma(n1,n2)} é {m.area_circulo(m.soma(n1,n2))}")
    print(f"A área de um retangulo de base {n1} e altura {n2} é {m.area_retangulo(n1,n2)}")
    print(f'A média entre 10,12,15 é {media.media_simples([10,12,15])}')
    

teste()
