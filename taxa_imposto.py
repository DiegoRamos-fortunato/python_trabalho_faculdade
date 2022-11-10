def somador_de_imposto(t, c):
    Imposto = c + (c * t / 100)
    return Imposto
    

print (somador_de_imposto(5, 12))