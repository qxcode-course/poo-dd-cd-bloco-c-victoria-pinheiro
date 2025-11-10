def dividir(num: int, den: int) -> float | str:
    if den == 0:
        raise Exception("Nao consigo dividir por zero") #continua sem quebrar o código
    return num / den

def processa(a: int, b: int, c: int, d: int) -> float:
    a = dividir(a, b)
    b = dividir(c, d)

def main():
    print(processa(4, 2, 3, 0))



