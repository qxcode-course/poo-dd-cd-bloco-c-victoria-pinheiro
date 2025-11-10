#compras: list[str] = ["batata", "fandangos", "uva", "picles", "uva"] #lista so tem um argumento


nomes: dict[int, str] = {} # dicionário tem que er dois argumentos 
# chave = valor
nomes[1] = "one"
nomes[2] = "two"
nomes[3] = "three"
nomes[4] = "four"
nomes[5] = "six"

def pegar_valores
valores: dict[str, int] = {}
valores["one"] = 1
valores["two"] = 2
valores["three"] = 3
valores["four"] = 4
valores["six"] = 6

nomes: dict[int, str] = {     #outra forma de escrever o dicionário
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five"
}
if valor in nomes:
    return nomes[valor]
raise Exception(f"Nao existe {valor} na lista de valores")

def somar(a: str, b: str) -> str:
    return nomes pegar_valor(a) + pegar_valor(b)

print(somar("five", "seven"))
print(somar("three", "two"))


