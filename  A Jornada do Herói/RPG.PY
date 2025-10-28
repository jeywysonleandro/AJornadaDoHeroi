# Nível Básico: O despertar do Herói

class Guerreiro:
    def __init__(self, nome, vida, forca):
        self.nome = nome
        self.vida = vida
        self.forca = forca

    def atacar(self):
        print(f"{self.nome} atacou com {self.forca} de força!")

# 2. O mago

class Mago:
    def __init__(self, nome, vida, poder_magico):
        self.nome = nome
        self.vida = vida
        self.poder_magico = poder_magico

    def conjurar_feitico(self):
        print(f"{self.nome} conjura uma magia com poder {self.poder_magico}!")

#3. O Arqueiro

class Arqueiro:
    def __init__(self, nome, vida, precisao):
        self.nome = nome
        self.vida = vida
        self.precisao = precisao
    
    def disparar_flecha(self):
        print(f"{self.nome} dispara uma flecha com precisão {self.precisao}!")

# 4. O Primeiro Inimigo

class Monstro:
    def __init__(self, nome, vida, dano):
        self.nome = nome
        self.vida = vida
        self.dano = dano

    def atacar(self):
        print(f"{self.nome} ataca causando {self.dano} de dano!")

# Criando o primeiro inimigo: Goblin
goblin = Monstro("Goblin", 50, 10)

# 5. Status do Personagem

class Guerreiro:
    def __init__(self, nome, vida, forca):
        self.nome = nome
        self.vida = vida
        self.forca = forca

    def atacar(self):
        print(f"{self.nome} ataca com {self.forca} de força!")

    def __str__(self):
        return f"--- Status do Guerreiro ---\nNome: {self.nome}\nVida: {self.vida}\nForça: {self.forca}\n--------------------------"
