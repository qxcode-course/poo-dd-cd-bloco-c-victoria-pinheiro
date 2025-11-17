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


--------------------------------------------------------------------------
BUDEGA

espera: list[str] = []

espera.append("joao")
espera.append("maria")
espera.append("bruxa")

del espera[1]

espera = ['maria'] + espera

del espera[0]

espera.append("lobo")
espera.append("caçador")

del espera[2]

espera.insert(2, "lobo") #insert é para colocar no mesmo lugar de antes (primeiro digita o índice que quer que ele fique e depois o que quer colocar la)

texto = ", ".join(espera)

print(texto)

texto.split("-")

#list comprehension (gera uma lista a partir da outra)

[len (elem) for elem in espera] #for elem in epera ("a cada elemento -escolhe qualquer nome que quiser- em espera")
                     #e antes desse for elem in espera,  diz o que vai acontecer com ele
                     #len (x) ("vou gerar tamanho de elemento")

[elem(0) for elem in espera] #vai pegar a primeira letra de cada objeto na lista