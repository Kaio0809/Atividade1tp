import conversores as c

def teste():
    y = 10

    print(f"{y} graus Celcius são {c.celsius_para_fahrenheit(y)} graus Fihrenheit")
    print(f"{y} graus Fihrenheit são {c.fahrenheit_para_celsius(y)} graus Celcius")
    print(f"{y} Metros são {c.metro_para_pes(y)} pes")
    print(f"{y} pes são {c.pes_para_metro(y)} Metros")
    print(f"{y} Milhas são {c.milhas_para_quilometro(y)} Km")
    print(f"{y} Km são {c.quilometro_para_milhas(y)} Milhas")
    print(f"{y} Dias são {c.dia_para_horas(y)} horas")

teste() 