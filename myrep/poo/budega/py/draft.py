class Pessoa:
    def __init__(self, nome: str):
        self.nome = nome

    def __str__(self) -> str:
        return self.nome
    
class Budega:
    def __init__(self, num_caixas: int):
        self.caixas: list[Pessoa | None] = []
        for _ in range(num_caixas):
            self.caixas.append(None)
        self.espera: list[Pessoa] = []

    def enter(self, pessoa: Pessoa):
        self.espera.append(pessoa)

    def call(self, index: int):
        if index < 0 or index >= len(self.caixas):
            print("fail: caixa inexitente")
            return 
        if self.caixas[index] is not None:
            print("fail: caixa ocupado")  
            return
        if len(self.espera) == 0:
            print("fail: sem clientes")
            return
        self.caixas[index] = self.espera.pop[0]


    def finish(self, index: int):
        if index < 0 or index >= len(self.caixas):
            print("indice inexitente")
            return None
        if self.caixas[index] is None:
            print("caixa vazio")  
            return None
        cliente = self.caixas[index]
        self.caixas[index] = None
        return cliente

    def give_up(self, nome: str) -> Pessoa | None:
        for i, pessoa in enumerate(self.espera):
            if pessoa.nome == nome:
                return self.espera.pop(i)
            return None
                

    def __str__(self) -> str:
        caixas = ", ".join(["----" if x is None else str(x) for x in self.caixas])
        espera= ', '.join([str(x) for x in self.espera])
        return f"Caixas: [{caixas}]\nEspera: [{espera}]"
    

