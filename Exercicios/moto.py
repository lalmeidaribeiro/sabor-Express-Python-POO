'''
     07° Lista de exercícios:

        1- Crie uma Classe Pai (Veiculo): Implemente uma classe chamada Veiculo com um construtor que aceita dois parâmetros, 
        marca e modelo. A classe deve ter um atributo protegido _ligado inicializado como False por padrão.
        2- Construa o Método Especial str: Adicione um método especial str à classe Veiculo que retorna uma mensagem formatada 
        com a marca, modelo e o estado de ligado/desligado do veículo.
        3- Crie uma Classe Filha (Carro): Agora, crie uma classe chamada Carro que herda da classe Veiculo. No construtor da classe
        Carro, inclua um novo atributo chamado portas que indica a quantidade de portas do carro.
        4- Implemente o Método Especial str na Classe Filha: Adicione um método especial str à classe Carro que estenda o método da 
        classe pai (Veiculo) e inclua a informação sobre a quantidade de portas do carro.
        5- Crie uma Classe Filha (Moto): Similarmente, crie uma classe chamada Moto que também herda de Veiculo. Adicione um novo atributo 
        chamado tipo ao construtor, indicando se a moto é esportiva ou casual.
        6- Implemente o Método Especial str na Classe Filha (Moto): Adicione um método especial str à classe Moto que estenda o método da 
        classe pai (Veiculo) e inclua a informação sobre o tipo da moto.
'''
from projeto.exercicios.veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self._tipo = tipo 
  
    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f"Marca: {self.marca} | Modelo: {self.modelo} | Tipo: {self._tipo} | Status: {status}"