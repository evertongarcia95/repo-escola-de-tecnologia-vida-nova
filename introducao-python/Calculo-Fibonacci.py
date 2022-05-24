n = input ("digite a quantidade de números de fibonacci que voce quer calcular""\n\n")
anterior = 0
proximo = 0

while (proximo < n):
    print(proximo)
    proximo = proximo + anterior
    anterior = proximo - anterior
    if (proximo == 0):
        proximo = proximo + 1



    
