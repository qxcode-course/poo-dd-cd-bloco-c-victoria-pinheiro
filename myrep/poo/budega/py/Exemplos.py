class Pessoa:
    def __init__(self, nome: str):
        self.nome = nome

    def __str__(self) -> str:
        return self.nome
    
class Budega:
    def __init__(self, num_caixas: int):
        self.caixas: list[Pessoa | None] = [None for _ in range(num_caixas)]
        self.espera: list[Pessoa] = []

    def enter(self, pessoa: Pessoa):
        self.espera.append(pessoa)

    def arrive(self, pessoa: Pessoa):
        self.enter(pessoa)

    def call(self, index: int):
        if index < 0 or index >= len(self.caixas):
            print("fail: caixa inexistente")
            return 
        if self.caixas[index] is not None:
            print("fail: caixa ocupado")  
            return
        if len(self.espera) == 0:
            print("fail: sem clientes")
            return
        self.caixas[index] = self.espera.pop(0)


    def finish(self, index: int):
        if index < 0 or index >= len(self.caixas):
            print("fail: caixa inexistente")
            return None
        if self.caixas[index] is None:
            print("fail: caixa vazio")  
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
        caixas = ", ".join(["-----" if x is None else str(x) for x in self.caixas])
        espera= ', '.join([str(x) for x in self.espera])
        return f"Caixas: [{caixas}]\nEspera: [{espera}]"
    
def main():
    budega: Budega | None = None

    while True:
        try:
            line: str = input()
        except EOFError:
            break

        if line is None:
            continue

        print("$" + line)
        args: list[str] = line.split()
        if len(args) == 0:
            continue

        if args[0] == "end":
            break
        if args[0] == "show":
            if budega is None:
                print("fail: mercado nao iniciado")
            else: 
                print(budega)

        elif args[0] == "init":
            caixas = int(args[1])
            budega = Budega(caixas)

        elif args[0] == "enter" or args[0] == "arrive":
            if budega is None:
                print("fail: mercado nao iniciado")
                continue
            nome = args[1]
            pessoa = Pessoa(nome)
            budega.arrive(pessoa)

        elif args[0] == "call":
            if budega is None:
                print("fail: mercado nao iniciado")
                continue
            index = int(args[1])
            budega.call(index)

        elif args[0] == "finish":
            if budega is None:
                print("fail: mercado nao iniciado")
                continue
            index = int(args[1])
            budega.finish(index)
        elif args[0] == "giveup":
            if budega is None:
                print("fail: mercado nao iniciado")
                continue
            nome = args[1]
            budega.give_up(nome)
        else:
            print("fail: comando invalido")
            

main()



