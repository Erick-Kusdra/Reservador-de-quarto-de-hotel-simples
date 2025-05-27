
class Quarto:
    def __init__(self, maximo, luxo, ocupado):
        self.maximo = maximo
        self.luxo = luxo
        self.ocupado = ocupado
    def __str__(self):
        tipo = "luxo" if self.luxo else "Simples"
        return f"quarto de {tipo}, com limite de {self.maximo} pessoas"

quarto1 = Quarto(3, False, False)
quarto2 = Quarto(4,False, False)
quarto3 = Quarto(3, True, False)
quarto4 = Quarto(4, True, False)

quartos = [quarto1, quarto2, quarto3, quarto4]

reserva = int(input("Para quantas pessoas deseja um quarto"))
luxo_input = input("Quarto de luxo (s/n)?").lower()
luxuoso = luxo_input == "s"

for i in quartos:
    if not i.ocupado and reserva <= i.maximo and i.luxo == luxuoso:
        print(f"Vá para o {i}")
        i.ocupado = True
        break

