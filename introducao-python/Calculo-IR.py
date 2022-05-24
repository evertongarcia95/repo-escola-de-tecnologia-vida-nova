salariobruto = float(input("digite o salario cáuculo do imposto")) 
while True:
     if salariobruto < 1903.98 :
          imposto = 0
     elif salariobruto > 1903.99 and salariobruto < 2826.65:
          imposto = 7.5
     elif salariobruto > 2826.66 and salariobruto < 3751.05:
          imposto = 15.0
     elif salariobruto > 3751.06 and salariobruto < 4664.68:
          imposto = 22.5
     elif salariobruto < 4664.69: 
          imposto = 27.5

     salarioliquido = salariobruto - (salariobruto * (imposto /100))

     print (salarioliquido)

     aumento = float (input ("qual o valor do aumento?"))
     salariobruto += aumento 