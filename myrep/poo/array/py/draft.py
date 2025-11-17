class Foo:
    def __init__(self, x: int):
        self.x = x
    
    def __str__(self):
        return f"Foo({self.x})"
    
print(">>>>>Lista Vazia")
lista_vazia: list[int] = []
print(lista_vazia)

print(">>>>>Lista Preenchida")
lista_preenchida: list[int] = [1, 2, 3, 4, 5]
print(lista_preenchida)

print(">>>>>Lista de Objetos")
lista_preenchida_objetos: list[Foo] = [Foo(1), Foo(2), Foo(3), Foo(4), Foo(5)]
print([str(x) for x in lista_preenchida_objetos]) #transformando cada elemento do vetor em uma str

print(">>>>>Número de objetos na lista")
print(len(lista_preenchida))

print(">>>>>Incluindo à sequência")
lista_preenchida.append(6)
print(lista_preenchida)

print(">>>>>Retirando o numero inserido")
lista_preenchida.pop()
print(lista_preenchida)

print(">>>>>Inserindo Número à lista")
lista_preenchida.insert(0, 10)
print(lista_preenchida)

print(">>>>>Retirando Número inserido")
lista_preenchida.pop(2)
print(lista_preenchida)

print(">>>>>Join")
print(", ".join([str(x) for x in lista_preenchida]))

print(">>>>>Range")
n = 10
sequencia = list(range(n + 1))
print(sequencia)

print(">>>>>Números Aleatórios")
import random
aleatorio = [random.randint(0, 10) for _ in range(10)]
print(aleatorio)

print(">>>>>Índice da sequencia")
print(sequencia[3])

print(">>>>>For range")
for x in sequencia:
    print(x)

print(">>>>>For indexado")
for i in range(len(sequencia)):
    print(i, sequencia[i])

#buscar manualmente
x = 5
seq = -1
for i, v in enumerate(sequencia):
    if v == x:
        seq = i
        break

print(">>>>>Buscando com index")
print(sequencia.index(5))

print(">>>>>Numeros pares da sequencia")
pares = [v for v in sequencia if v % 2 == 0]
print(pares)


print(">>>>>Buscando e retirando")
x = 5
if x in sequencia:
    sequencia.remove(x)
print(sequencia)

print(">>>>>Retirando todos os valores X")
x = 2
sequencia = [v for v in sequencia if v != x]
print(sequencia)
