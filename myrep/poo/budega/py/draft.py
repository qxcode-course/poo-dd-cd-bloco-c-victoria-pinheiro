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

