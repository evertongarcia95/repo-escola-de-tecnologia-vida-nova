programa {
	funcao inicio() {
        real valorDigitado
        real soma

        soma = 0
        
        escreva("Digite um valor para a soma: ")
        leia(valorDigitado)
		faca 
		{
			soma = soma + valorDigitado
		
		    escreva("\nValor total: ", soma, "\n")
		
		    escreva("Digite um valor para a soma: ")
            leia(valorDigitado)	
		}
		enquanto (valorDigitado != 0)

		escreva("\nResultado: ", soma)
		
	}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 428; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */