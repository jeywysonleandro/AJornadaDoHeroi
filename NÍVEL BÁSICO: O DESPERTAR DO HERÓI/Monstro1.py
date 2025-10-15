class Monstro:
    def __init__(self, nome, vida, dano):
        self.nome = nome
        self.vida = vida
        self.dano = dano

    def atacar(self):
        print(f"{self.nome} atacou causando {self.dano} de dano!")

    def __str__(self):
        return f"Monstro: {self.nome}, Vida: {self.vida}, Dano: {self.dano}"

Monstro1 = Monstro("Goblin", 50, 10)
Monstro1.atacar()
print(Monstro1)