# ==========================
# DESAFIO DE POO - RPG
# ==========================

# ==========================
# Classes de Itens
# ==========================
class Arma:
    def __init__(self, nome, poder):
        self.nome = nome
        self.poder = poder

class Pocao:
    def __init__(self, nome, cura):
        self.nome = nome
        self.cura = cura

# ==========================
# Classe Inventário
# ==========================
class Inventario:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)
        print(f"{item.nome} adicionado ao inventário!")

    def usar_pocao(self, personagem):
        # Busca a primeira poção no inventário
        for item in self.itens:
            if isinstance(item, Pocao):
                cura_real = min(item.cura, personagem.vida_maxima - personagem.vida)
                personagem.vida += cura_real
                self.itens.remove(item)
                print(f"{personagem.nome} usou {item.nome} e recuperou {cura_real} de vida!")
                return
        print(f"{personagem.nome} não tem poções disponíveis!")

    def mostrar_itens(self):
        if not self.itens:
            print("Inventário vazio.")
        else:
            print("Itens no inventário:")
            for item in self.itens:
                if isinstance(item, Arma):
                    print(f"- Arma: {item.nome} (+{item.poder})")
                elif isinstance(item, Pocao):
                    print(f"- Poção: {item.nome} (Cura: {item.cura})")

# ==========================
# Classe Base Personagem
# ==========================
class Personagem:
    def __init__(self, nome, vida, vida_maxima=None):
        self.nome = nome
        self._vida = vida
        self.vida_maxima = vida if vida_maxima is None else vida_maxima
        self.inventario = Inventario()

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):
        if valor < 0:
            self._vida = 0
        elif valor > self.vida_maxima:
            self._vida = self.vida_maxima
        else:
            self._vida = valor

    def receber_dano(self, dano):
        self.vida -= dano
        print(f"{self.nome} recebeu {dano} de dano! Vida restante: {self.vida}")

    def esta_vivo(self):
        return self.vida > 0

    def atacar(self, alvo=None):
        pass

    def __str__(self):
        return f"Nome: {self.nome}\nVida: {self.vida}/{self.vida_maxima}"

# ==========================
# Classes de Heróis
# ==========================
class Guerreiro(Personagem):
    def __init__(self, nome, vida, forca):
        super().__init__(nome, vida)
        self.forca = forca
        self.arma = None

    def atacar(self, alvo=None):
        dano_total = self.forca + (self.arma.poder if self.arma else 0)
        print(f"{self.nome} ataca causando {dano_total} de dano!")
        if alvo:
            alvo.receber_dano(dano_total)

    def __str__(self):
        info_arma = f", Arma: {self.arma.nome} (+{self.arma.poder})" if self.arma else ""
        return f"--- Status do Guerreiro ---\nNome: {self.nome}\nVida: {self.vida}/{self.vida_maxima}\nForça: {self.forca}{info_arma}\n--------------------------"

class Mago(Personagem):
    def __init__(self, nome, vida, poder_magico):
        super().__init__(nome, vida)
        self.poder_magico = poder_magico

    def atacar(self, alvo=None):
        print(f"{self.nome} conjura magia com poder {self.poder_magico}!")
        if alvo:
            alvo.receber_dano(self.poder_magico)

    def __str__(self):
        return f"--- Status do Mago ---\nNome: {self.nome}\nVida: {self.vida}/{self.vida_maxima}\nPoder Mágico: {self.poder_magico}\n--------------------------"

class Arqueiro(Personagem):
    def __init__(self, nome, vida, precisao):
        super().__init__(nome, vida)
        self.precisao = precisao

    def atacar(self, alvo=None):
        print(f"{self.nome} dispara uma flecha com precisão {self.precisao}!")
        if alvo:
            alvo.receber_dano(self.precisao)

    def __str__(self):
        return f"--- Status do Arqueiro ---\nNome: {self.nome}\nVida: {self.vida}/{self.vida_maxima}\nPrecisão: {self.precisao}\n--------------------------"

# ==========================
# Classe Monstro
# ==========================
class Monstro(Personagem):
    def __init__(self, nome, vida, dano):
        super().__init__(nome, vida)
        self.dano = dano

    def atacar(self, alvo=None):
        print(f"{self.nome} ataca causando {self.dano} de dano!")
        if alvo:
            alvo.receber_dano(self.dano)

    def __str__(self):
        return f"--- Status do Monstro ---\nNome: {self.nome}\nVida: {self.vida}/{self.vida_maxima}\nDano: {self.dano}\n--------------------------"

    @classmethod
    def goblin_padrao(cls):
        return cls("Goblin Padrão", 50, 10)

# ==========================
# Criando Itens
# ==========================
espada = Arma("Espada Longa", 15)
cajado = Arma("Cajado Mágico", 12)
pocao_vida = Pocao("Poção de Vida", 30)

# ==========================
# Testes e Demonstração
# ==========================
print("="*50)
print("CRIANDO PERSONAGENS")
print("="*50)

# Criando heróis
meu_guerreiro = Guerreiro("Arthur", 100, 20)
meu_mago = Mago("Merlin", 80, 35)
meu_arqueiro = Arqueiro("Legolas", 90, 40)

# Equipando o guerreiro
meu_guerreiro.arma = espada

# Adicionando itens ao inventário
meu_guerreiro.inventario.adicionar_item(pocao_vida)

# Criando monstros
goblin1 = Monstro.goblin_padrao()
goblin2 = Monstro.goblin_padrao()

print("\n" + "="*50)
print("STATUS INICIAL")
print("="*50)
print(meu_guerreiro)
print(meu_mago)
print(meu_arqueiro)
print(goblin1)
print(goblin2)

print("\n" + "="*50)
print("BATALHA!")
print("="*50)
meu_guerreiro.atacar(goblin1)
meu_mago.atacar(goblin1)
meu_arqueiro.atacar(goblin1)
goblin2.atacar(meu_guerreiro)

print("\n" + "="*50)
print("USANDO POÇÃO")
print("="*50)
meu_guerreiro.inventario.usar_pocao(meu_guerreiro)

print("\n" + "="*50)
print("VERIFICANDO SOBREVIVÊNCIA")
print("="*50)
print(f"{meu_guerreiro.nome} está vivo? {meu_guerreiro.esta_vivo()}")
print(f"{goblin1.nome} está vivo? {goblin1.esta_vivo()}")

print("\n" + "="*50)
print("STATUS FINAL")
print("="*50)
print(meu_guerreiro)
print(meu_mago)
print(meu_arqueiro)
print(goblin1)
print(goblin2)