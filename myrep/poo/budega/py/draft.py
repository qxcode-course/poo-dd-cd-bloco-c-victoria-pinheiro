class Pessoa:
    def __init__(self, nome: str):
        self.nome = nome
    
    def __str__(self) -> str:
        return self.nome

    def enter(self, pessoa: Pessoa):  #pessoa indo para a fila
        self.espera.append(pessoa)

    def call(self, index: int):  #chamando a pessoa
        if index < 0 or index >= len(self.caixa):
            print("indice inexistente")
            return
        if self.caixas[index] is not None:
            print("Caixa ocupado")
            return
        self.caixas[index] = self.espera[0]
        del self.espera[0]         #deletando a pessoa que ja foi chamada


class Budega:
    def __init__(self, num_caixas: int):
        self.caixas: list[Pessoa | None] = []
        for _ in range(num_caixas):             #laço que vai rodar o tanto de caixas que for inserido
            self.caixas.append(None)
        self.espera: list[Pessoa | None] = []
    

    def __str__(self) -> str:
        self.caixas = [Pessoa("Maria"), None, Pessoa("Joao")]

        caixas = ",".join([str(x) for x in self.caixas]) #"faça uma ação para cada elemento desse vetor"
        espera = ",".join([str(x) for x in self.caixas])

pessoa = Pessoa("Maria")
print(pessoa)

budega = Budega(5)
budega.caixas[2] = pessoa
budega.espera.append