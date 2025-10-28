# ==========================
# Nível Básico: O Despertar do Herói
# ==========================

# ==========================
# 1. Classe Guerreiro
# ==========================
class Guerreiro:
    def __init__(self, nome, vida, forca):
        self.nome = nome
        self.vida = vida
        self.forca = forca
        self.arma = None  # Aqui vai receber um objeto Arma

    def atacar(self):
        dano_total = self.forca
        if self.arma:
            dano_total += self.arma.poder
        print(f"{self.nome} ataca causando {dano_total} de dano!")

    def __str__(self):
        info_arma = f", Arma: {self.arma.nome} (+{self.arma.poder})" if self.arma else ""
        return f"--- Status do Guerreiro ---\nNome: {self.nome}\nVida: {self.vida}\nForça: {self.forca}{info_arma}\n--------------------------"

# ==========================
# 2. Classe Mago
# ==========================
class Mago:
    def __init__(self, nome, vida, poder_magico):
        self.nome = nome
        self.vida = vida
        self.poder_magico = poder_magico

    def atacar(self):
        print(f"{self.nome} conjura uma magia com poder {self.poder_magico}!")

    def __str__(self):
        return f"--- Status do Mago ---\nNome: {self.nome}\nVida: {self.vida}\nPoder Mágico: {self.poder_magico}\n--------------------------"

# ==========================
# 3. Classe Arqueiro
# ==========================
class Arqueiro:
    def __init__(self, nome, vida, precisao):
        self.nome = nome
        self.vida = vida
        self.precisao = precisao

    def atacar(self):
        print(f"{self.nome} dispara uma flecha com precisão {self.precisao}!")

    def __str__(self):
        return f"--- Status do Arqueiro ---\nNome: {self.nome}\nVida: {self.vida}\nPrecisão: {self.precisao}\n--------------------------"

# ==========================
# 4. Classe Monstro
# ==========================
class Monstro:
    def __init__(self, nome, vida, dano):
        self.nome = nome
        self.vida = vida
        self.dano = dano

    def atacar(self):
        print(f"{self.nome} ataca causando {self.dano} de dano!")

    def __str__(self):
        return f"--- Status do Monstro ---\nNome: {self.nome}\nVida: {self.vida}\nDano: {self.dano}\n--------------------------"

# ==========================
# 7. Itens: Arma
# ==========================
class Arma:
    def __init__(self, nome, poder):
        self.nome = nome
        self.poder = poder

espada = Arma("Espada Longa", 15)
cajado = Arma("Cajado Mágico", 12)

# ==========================
# 8. Itens: Poção
# ==========================
class Pocao:
    def __init__(self, nome, cura):
        self.nome = nome
        self.cura = cura

pocao_vida = Pocao("Poção de Vida", 30)

# ==========================
# Testes de Criação e Ações
# ==========================

# Criando personagens e inimigo
meu_guerreiro = Guerreiro("Arthur", 100, 20)
meu_mago = Mago("Merlin", 80, 35)
meu_arqueiro = Arqueiro("Legolas", 90, 40)
goblin = Monstro("Goblin", 50, 10)

# Equipando o Guerreiro
meu_guerreiro.arma = espada

# ==========================
# Mostrar Status dos Personagens
# ==========================
print(meu_guerreiro)
print(meu_mago)
print(meu_arqueiro)
print(goblin)

# ==========================
# Testar Ataques
# ==========================
meu_guerreiro.atacar()
meu_mago.atacar()
meu_arqueiro.atacar()
goblin.atacar()

# ==========================
# Nível Intermediário: A Forja das Lendas
# ==========================

# ==========================
# Classe Base Personagem
# ==========================

class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self._vida = max(0, vida)

    #Getter
    @property
    def vida(self):
        return self._vida

    #Setter
    @vida.setter
    def vida(self, valor):
        if valor < 0:
            self._vida = 0
        else:
            self._vida = valor
            
    def atacar(self):
        pass
    
    def __str__(self):
        return f"Nome: {self.nome}\nVida: {self.vida}"
    
# ==========================
# 1. Classe Guerreiro herdando Personagem
# ==========================

class Guerreiro(Personagem):
    def __init__(self, nome, vida, forca):
        super().__init__(nome, vida)
        self.forca = forca
        self.arma = None

    def atacar(self):
        dano_total = self.forca
        if self.arma:
            dano_total += self.arma.poder
        print(f"{self.nome} ataca causando {dano_total} de dano!")

    def __str__(self):
        info_arma = f", Arma: {self.arma.nome} (+{self.arma.poder})" if self.arma else ""
        return f"--- Status do Guerreiro ---\nNome: {self.nome}\nVida: {self.vida}\nForça: {self.forca}{info_arma}\n--------------------------"
    
# ==========================
# 2. Classe Mago herdando Personagem
# ==========================

class Mago(Personagem):
    def __init__(self, nome, vida, poder_magico):
        super().__init__(nome, vida)
        self.poder_magico = poder_magico

    def atacar(self):
        print(f"{self.nome} conjura uma magia com poder {self.poder_magico}!")

    def __str__(self):
        return f"--- Status do Mago ---\nNome: {self.nome}\nVida: {self.vida}\nPoder Mágico: {self.poder_magico}\n--------------------------"
    
    # ==========================
# 3. Classe Arqueiro herdando Personagem
# ==========================
class Arqueiro(Personagem):
    def __init__(self, nome, vida, precisao):
        super().__init__(nome, vida)
        self.precisao = precisao

    def atacar(self):
        print(f"{self.nome} dispara uma flecha com precisão {self.precisao}!")

    def __str__(self):
        return f"--- Status do Arqueiro ---\nNome: {self.nome}\nVida: {self.vida}\nPrecisão: {self.precisao}\n--------------------------"
    
