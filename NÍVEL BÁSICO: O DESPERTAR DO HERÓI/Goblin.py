class Monstro:
    def __init__(self, nome, vida, dano):
        self.nome = nome
        self.vida = vida
        self.dano = dano

    def atacar(self):
        print(f"{self.nome} atacou causando {self.dano} de dano!")

Monstro1 = Monstro("Goblin", 50, 10)
Monstro1.atacar()