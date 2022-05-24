"""
Desenvolva um programa em 3 etapas. Tente concluir cada etapa separadamente. Somente a etapa 1 e 2 são “obrigatórias” dado 
tudo o que já aprendemos.
A primeira etapa consiste em construir quatro funções diferentes:
1ª Ler o nome, sobrenome e cargo de um funcionário e retornar essas informações dentro de um vetor.
2ª Exibir na tela as informações do funcionário que devem ser passadas por parâmetro.
3ª Ler e retornar um salário para esse funcionário.
4ª Calcular e exibir na tela o salário Líquido desse funcionário depois de calcular o Imposto de Renda.
O código deve rodar em um loop infinito e dar as opções para que seja possível escolher qual função eu desejo chamar.
A segunda etapa consiste em fazer validações para essas funções:

O imposto de renda só pode ser calculado se eu já chamei as funções de colocar as informações do funcionário (nome, 
sobrenome e cargo) e de inserir um salário para esse.

O código deve ter uma opção (opção 0) em que, ao selecioná-la, o código sai do loop e se encerra.

Se eu digitar um salário inválido (uma letra ou um símbolo), o código deve pedir para que eu coloque um valor válido.
 Não interessa quantas vezes eu digitar errado, o código precisa sempre pedir para colocar um valor válido até eu colocar.
 terceira etapa consiste em fazer uma classe Funcionário, onde os atributos são as informações já citadas (nome, sobrenome, 
 cargo e salário), e cada uma das funções criadas deve ser um método da classe.

O código principal deve criar uma instância do funcionário, e então entrar no loop, seguindo o mesmo processo de selecionar
 qual a opção desejada, e de acordo com a opção, chamar o método da classe passando os devidos parâmetros quando necessário.

"""
class Funcionario :
    def __init__(self, Name: str, SurName: str, Occupation: str, Wage: float) -> None:
        self.Name = Name
        self.SurName = SurName
        self.Occupation = Occupation
        self.Wage = Wage

    def setName(self, Name: str , SurName: str) -> None:
        self.Name = Name
        self.Surname = Surname

    def getName(self) -> str:
        return self.Name + " " + self.Surname

    def setOccupation(self, Occupation: str) -> None:
        self.Occupation = Occupation

    def getOccupation(self) -> str:
        return self.Occupation

    def setWage(self, Wage: float) -> None:
        self.Wage = Wage

    def getWage(self) -> float:
        return self.Wage

    def printFuncionario (self):

        print ('test')

    def funcionario_list(self):
        mylist = [self.Name, self.SurName, self.Occupation, self.Wage]
        return mylist

funcionario1 = Funcionario("Willian", "Mingardi", "developer", 5000.00)
funcionario1.printFuncionario()
print (funcionario1.funcionario_list())
