class Arqueiro:
    def __init__(self, nome, vida, precisao):
        self.nome = nome
        self.vida = vida
        self.precisao = precisao

    def atirar_flecha(self):
       print(f"{self.nome} disparou uma flecha com precisão {self.precisao}!")

arqueiro1 = Arqueiro("Legolas", 90, 85)
arqueiro1.atirar_flecha()
