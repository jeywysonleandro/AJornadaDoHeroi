class Mago:
    def __init__(self, nome, vida, poder_magico):
        self.nome = nome
        self.vida = vida
        self.poder_magico = poder_magico

    def conjurar_magia(self):
        print(f"{self.nome} lançou uma magia com poder {self.poder_magico}!")
    
    def __str__(self):
        return f"Mago: {self.nome}, Vida: {self.vida}, Poder Mágico: {self.poder_magico}"

mago1 = Mago("Gandalf", 80, 50)
mago1.conjurar_magia()
print(mago1)