class Guerreiro:
    def __init__(self, nome, vida, forca):
        self.nome = nome
        self.vida = vida
        self.forca = forca

    def atacar(self):
        print(f"{self.nome} atacou com {self.forca} de força!")

    def __str__(self):
        return f"Guerreiro: {self.nome}, Vida: {self.vida}, Força: {self.forca}"

guerreiro1 = Guerreiro("Thorin", 100, 20)
guerreiro1.atacar()
print(guerreiro1)
