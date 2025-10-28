for i in range(40)
o range permite definir o valor de partida e o fim
list(range(20, 0, -1)) -> Esta escrito "conte de 20 a 0 diminuindo de 1 em 1"
ele gera [20, 19, 18, 17...]
se for list(range(0, 10, 2)) -> Esta escrito "conte de 0 a 10 pulando de 2 em 2"
ele gera [0, 2, 4, 6, 8]


def __str__(self) -> str:
    self.caixas = [Pessoa("Maria"), None, Pessoa("Joao")]
        caixas = ",".join([str(x) for x in self.caixas]) #"faça uma ação para cada elemento desse vetor"
        espera = ",".join([str(x) for x in self.caixas])
