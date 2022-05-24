programa 
{
	funcao inicio()
	{
		const inteiro MAIORIDADE = 18
		
		inteiro idade, anos
		
		escreva("Digite sua idade: ")
		leia(idade)

		anos = MAIORIDADE - idade 

		se (anos > 0)
		{
			escreva("Falta(m) ", anos, " ano(s) para você atingir a maioridade\n")
		}
		senao 
		{
			escreva("Você já atingiu a maioridade\n")
		}
	}
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 334; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */