class Guerreiro:
    def __init__(self, nome, vida, forca):
        self.nome = nome
        self.vida = vida
        self.forca = forca

    def atacar(self):
        print(f"{self.nome} atacou com {self.forca} de força!")

guerreiro1 = Guerreiro("Thorin", 100, 20)
guerreiro1.atacar()
