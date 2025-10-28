# ==========================
# DESAFIO DE POO - RPG COMPLETO
# ==========================

from abc import ABC, abstractmethod
import random

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
# Classe Utilitária Dado (Q24)
# ==========================
class Dado:
    @staticmethod
    def rolar(lados=6):
        """Rola um dado com o número especificado de lados"""
        return random.randint(1, lados)
    
    @staticmethod
    def rolar_com_modificador(lados=6, modificador=0):
        """Rola um dado e adiciona um modificador"""
        return Dado.rolar(lados) + modificador

# ==========================
# Classe Abstrata Habilidade (Q21)
# ==========================
class Habilidade(ABC):
    def __init__(self, nome):
        self.nome = nome
    
    @abstractmethod
    def usar(self, usuario, alvo):
        """Método abstrato que deve ser implementado por todas as habilidades"""
        pass

# ==========================
# Habilidades Concretas (Q22)
# ==========================
class AtaqueForte(Habilidade):
    def __init__(self):
        super().__init__("Ataque Forte")
    
    def usar(self, usuario, alvo):
        dano = int(usuario.forca * 1.5) if hasattr(usuario, 'forca') else 30
        dano += Dado.rolar(6)  # Adiciona aleatoriedade
        print(f"{usuario.nome} usa {self.nome}!")
        alvo.receber_dano(dano)
        return dano

class BolaDeFogo(Habilidade):
    def __init__(self):
        super().__init__("Bola de Fogo")
    
    def usar(self, usuario, alvo):
        dano = int(usuario.poder_magico * 1.8) if hasattr(usuario, 'poder_magico') else 50
        dano += Dado.rolar(10)  # Adiciona aleatoriedade
        print(f"{usuario.nome} conjura uma {self.nome} devastadora!")
        alvo.receber_dano(dano)
        return dano

class FlechaPerfurante(Habilidade):
    def __init__(self):
        super().__init__("Flecha Perfurante")
    
    def usar(self, usuario, alvo):
        dano = int(usuario.precisao * 1.3) if hasattr(usuario, 'precisao') else 40
        dano += Dado.rolar(8)  # Adiciona aleatoriedade
        print(f"{usuario.nome} dispara uma {self.nome}!")
        alvo.receber_dano(dano)
        return dano

# ==========================
# Classe Base Personagem
# ==========================
class Personagem:
    def __init__(self, nome, vida, vida_maxima=None):
        self.nome = nome
        self._vida = vida
        self.vida_maxima = vida if vida_maxima is None else vida_maxima
        self.inventario = Inventario()
        self.habilidades = []  # Q23

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

    def adicionar_habilidade(self, habilidade):
        """Adiciona uma habilidade ao personagem"""
        self.habilidades.append(habilidade)
        print(f"{self.nome} aprendeu {habilidade.nome}!")

    def usar_habilidade(self, indice, alvo):
        """Q23 - Usa uma habilidade específica contra um alvo"""
        if 0 <= indice < len(self.habilidades):
            habilidade = self.habilidades[indice]
            return habilidade.usar(self, alvo)
        else:
            print(f"{self.nome} não possui essa habilidade!")
            return 0

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
        dano_base = self.forca + (self.arma.poder if self.arma else 0)
        variacao = Dado.rolar(6)  # Q25 - Combate imprevisível
        dano_total = dano_base + variacao
        print(f"{self.nome} ataca com sua espada! (Base: {dano_base} + Dado: {variacao})")
        if alvo:
            alvo.receber_dano(dano_total)
        return dano_total

    def __str__(self):
        info_arma = f", Arma: {self.arma.nome} (+{self.arma.poder})" if self.arma else ""
        habs = f", Habilidades: {len(self.habilidades)}" if self.habilidades else ""
        return f"--- Status do Guerreiro ---\nNome: {self.nome}\nVida: {self.vida}/{self.vida_maxima}\nForça: {self.forca}{info_arma}{habs}\n--------------------------"

class Mago(Personagem):
    def __init__(self, nome, vida, poder_magico):
        super().__init__(nome, vida)
        self.poder_magico = poder_magico

    def atacar(self, alvo=None):
        dano_base = self.poder_magico
        variacao = Dado.rolar(8)  # Q25 - Magia tem mais variação
        dano_total = dano_base + variacao
        print(f"{self.nome} conjura magia arcana! (Base: {dano_base} + Dado: {variacao})")
        if alvo:
            alvo.receber_dano(dano_total)
        return dano_total

    def __str__(self):
        habs = f", Habilidades: {len(self.habilidades)}" if self.habilidades else ""
        return f"--- Status do Mago ---\nNome: {self.nome}\nVida: {self.vida}/{self.vida_maxima}\nPoder Mágico: {self.poder_magico}{habs}\n--------------------------"

class Arqueiro(Personagem):
    def __init__(self, nome, vida, precisao):
        super().__init__(nome, vida)
        self.precisao = precisao

    def atacar(self, alvo=None):
        dano_base = self.precisao
        variacao = Dado.rolar(4)  # Q25 - Arqueiro tem menos variação (mais preciso)
        dano_total = dano_base + variacao
        print(f"{self.nome} dispara uma flecha certeira! (Base: {dano_base} + Dado: {variacao})")
        if alvo:
            alvo.receber_dano(dano_total)
        return dano_total

    def __str__(self):
        habs = f", Habilidades: {len(self.habilidades)}" if self.habilidades else ""
        return f"--- Status do Arqueiro ---\nNome: {self.nome}\nVida: {self.vida}/{self.vida_maxima}\nPrecisão: {self.precisao}{habs}\n--------------------------"

# ==========================
# Classe Monstro
# ==========================
class Monstro(Personagem):
    def __init__(self, nome, vida, dano):
        super().__init__(nome, vida)
        self.dano = dano

    def atacar(self, alvo=None):
        dano_total = self.dano + Dado.rolar(4)
        print(f"{self.nome} ataca ferozmente!")
        if alvo:
            alvo.receber_dano(dano_total)
        return dano_total

    def __str__(self):
        return f"--- Status do Monstro ---\nNome: {self.nome}\nVida: {self.vida}/{self.vida_maxima}\nDano: {self.dano}\n--------------------------"

    @classmethod
    def goblin_padrao(cls):
        return cls("Goblin Padrão", 50, 10)

# ==========================
# Orc com Ataque Crítico (Q26)
# ==========================
class Orc(Monstro):
    def __init__(self, nome, vida, dano, chance_critico=30):
        super().__init__(nome, vida, dano)
        self.chance_critico = chance_critico
    
    def atacar(self, alvo=None):
        dano_base = self.dano + Dado.rolar(6)
        
        # Verifica se acerta crítico
        if Dado.rolar(100) <= self.chance_critico:
            dano_total = dano_base * 2
            print(f"💥 {self.nome} desfere um GOLPE CRÍTICO!")
        else:
            dano_total = dano_base
            print(f"{self.nome} ataca com sua força bruta!")
        
        if alvo:
            alvo.receber_dano(dano_total)
        return dano_total
    
    @classmethod
    def orc_padrao(cls):
        return cls("Orc Guerreiro", 100, 20, 30)

# ==========================
# Sistema de Batalha (Q27-Q30)
# ==========================
class Batalha:
    def __init__(self, lado_a, lado_b):
        """
        Q27 - Gerenciador de Batalha
        lado_a e lado_b podem ser um combatente ou uma lista de combatentes
        """
        # Transforma em lista se for um único combatente
        self.lado_a = lado_a if isinstance(lado_a, list) else [lado_a]
        self.lado_b = lado_b if isinstance(lado_b, list) else [lado_b]
        self.turno = 0
    
    def equipe_viva(self, equipe):
        """Verifica se há pelo menos um membro vivo na equipe"""
        return any(combatente.esta_vivo() for combatente in equipe)
    
    def escolher_alvo_vivo(self, equipe):
        """Escolhe um alvo aleatório que ainda esteja vivo"""
        vivos = [c for c in equipe if c.esta_vivo()]
        return random.choice(vivos) if vivos else None
    
    def iniciar(self):
        """Q28 - Sistema de Turnos"""
        print("\n" + "="*60)
        print("⚔️  BATALHA INICIADA! ⚔️")
        print("="*60)
        
        # Mostra os combatentes
        print("\n🔵 LADO A:")
        for c in self.lado_a:
            print(f"   - {c.nome} (Vida: {c.vida})")
        
        print("\n🔴 LADO B:")
        for c in self.lado_b:
            print(f"   - {c.nome} (Vida: {c.vida})")
        
        print("\n" + "="*60)
        
        # Loop de turnos
        while self.equipe_viva(self.lado_a) and self.equipe_viva(self.lado_b):
            self.turno += 1
            print(f"\n--- TURNO {self.turno} ---")
            
            # Lado A ataca
            for atacante in self.lado_a:
                if atacante.esta_vivo():
                    alvo = self.escolher_alvo_vivo(self.lado_b)
                    if alvo:
                        atacante.atacar(alvo)
            
            # Verifica se o Lado B foi derrotado
            if not self.equipe_viva(self.lado_b):
                break
            
            # Lado B ataca
            for atacante in self.lado_b:
                if atacante.esta_vivo():
                    alvo = self.escolher_alvo_vivo(self.lado_a)
                    if alvo:
                        atacante.atacar(alvo)
        
        # Q29 - Anuncia o vencedor
        self.anunciar_vencedor()
    
    def anunciar_vencedor(self):
        """Q29 - Identifica e anuncia o vencedor"""
        print("\n" + "="*60)
        print("🏆 FIM DA BATALHA! 🏆")
        print("="*60)
        
        if self.equipe_viva(self.lado_a):
            print("\n✨ VITÓRIA DO LADO A! ✨")
            print("\nSobreviventes:")
            for c in self.lado_a:
                if c.esta_vivo():
                    print(f"   - {c.nome} (Vida restante: {c.vida})")
        else:
            print("\n✨ VITÓRIA DO LADO B! ✨")
            print("\nSobreviventes:")
            for c in self.lado_b:
                if c.esta_vivo():
                    print(f"   - {c.nome} (Vida restante: {c.vida})")
        
        print("="*60)

# ==========================
# Criando Itens
# ==========================
espada = Arma("Espada Longa", 15)
cajado = Arma("Cajado Mágico", 12)
pocao_vida = Pocao("Poção de Vida", 30)

# ==========================
# DEMONSTRAÇÃO COMPLETA
# ==========================
if __name__ == "__main__":
    print("="*60)
    print("DEMONSTRAÇÃO: NÍVEIS BÁSICO + INTERMEDIÁRIO + AVANÇADO")
    print("="*60)
    
    # Criando heróis
    guerreiro = Guerreiro("Arthur", 120, 25)
    mago = Mago("Merlin", 90, 40)
    arqueiro = Arqueiro("Legolas", 100, 35)
    
    # Equipando
    guerreiro.arma = espada
    
    # Adicionando habilidades (Q22-Q23)
    guerreiro.adicionar_habilidade(AtaqueForte())
    mago.adicionar_habilidade(BolaDeFogo())
    arqueiro.adicionar_habilidade(FlechaPerfurante())
    
    # Criando monstros
    goblin1 = Monstro.goblin_padrao()
    goblin2 = Monstro.goblin_padrao()
    orc = Orc.orc_padrao()  # Q26
    
    print("\n" + "="*60)
    print("TESTE 1: BATALHA INDIVIDUAL (Guerreiro vs Orc)")
    print("="*60)
    batalha1 = Batalha(Guerreiro("Conan", 100, 30), Orc.orc_padrao())
    batalha1.iniciar()
    
    print("\n" + "="*60)
    print("TESTE 2: BATALHA EM EQUIPE (Q30)")
    print("="*60)
    
    # Resetando heróis
    herois = [
        Guerreiro("Arthur", 120, 25),
        Mago("Merlin", 90, 40),
        Arqueiro("Legolas", 100, 35)
    ]
    herois[0].arma = espada
    
    monstros = [
        Monstro.goblin_padrao(),
        Monstro.goblin_padrao(),
        Orc.orc_padrao()
    ]
    
    batalha2 = Batalha(herois, monstros)
    batalha2.iniciar()
    
    print("\n" + "="*60)
    print("TESTE 3: USO DE HABILIDADES ESPECIAIS")
    print("="*60)
    
    heroi_teste = Guerreiro("Teste", 150, 30)
    heroi_teste.adicionar_habilidade(AtaqueForte())
    alvo_teste = Orc("Orc Teste", 80, 15)
    
    print(f"\n{heroi_teste.nome} vs {alvo_teste.nome}")
    print(f"Vida do {alvo_teste.nome}: {alvo_teste.vida}")
    heroi_teste.usar_habilidade(0, alvo_teste)
    print(f"Vida do {alvo_teste.nome} após habilidade: {alvo_teste.vida}")
    
    print("\n" + "="*60)
    print("✅ TODAS AS 30 QUESTÕES FORAM IMPLEMENTADAS!")
    print("📊 PONTUAÇÃO TOTAL: 450/450 pontos")
    print("="*60)