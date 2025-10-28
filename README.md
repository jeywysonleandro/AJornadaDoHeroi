# 🎮 Sistema de RPG Completo - Python POO

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-concluído-success)
![Score](https://img.shields.io/badge/pontuação-450%2F450-brightgreen)

> Um sistema completo de RPG desenvolvido em Python aplicando todos os conceitos fundamentais de Programação Orientada a Objetos (POO). Das aulas 1 a 30.

---

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Conceitos de POO Aplicados](#-conceitos-de-poo-aplicados)
- [Estrutura do Código](#-estrutura-do-código)
- [Classes de Personagens](#-classes-de-personagens)
- [Sistema de Batalha](#-sistema-de-batalha)
- [Instalação e Uso](#-instalação-e-uso)
- [Exemplos de Código](#-exemplos-de-código)
- [Questões Implementadas](#-questões-implementadas)

---

## 🎯 Sobre o Projeto

Este projeto é um **RPG completo** que demonstra a aplicação prática de todos os pilares da POO:

- ✅ **Encapsulamento** - Proteção de atributos com `@property` e `@setter`
- ✅ **Herança** - Hierarquia de classes (Personagem → Guerreiro/Mago/Arqueiro)
- ✅ **Polimorfismo** - Métodos sobrescritos com comportamentos únicos
- ✅ **Abstração** - Classes abstratas e interfaces
- ✅ **Composição** - Personagens TÊM inventário e habilidades

---

## 🧩 Conceitos de POO Aplicados

### 1️⃣ Classes e Objetos
```python
# Definição de classe
class Arma:
    def __init__(self, nome, poder):
        self.nome = nome
        self.poder = poder

# Instanciação de objeto
espada = Arma("Espada Longa", 15)
```

### 2️⃣ Encapsulamento
```python
@property
def vida(self):
    return self._vida

@vida.setter
def vida(self, valor):
    if valor < 0:
        self._vida = 0  # Protege contra valores negativos
    elif valor > self.vida_maxima:
        self._vida = self.vida_maxima  # Limita ao máximo
    else:
        self._vida = valor
```

### 3️⃣ Herança
```python
class Personagem:
    # Classe base com atributos e métodos comuns
    pass

class Guerreiro(Personagem):
    # Herda tudo de Personagem + adiciona força
    def __init__(self, nome, vida, forca):
        super().__init__(nome, vida)
        self.forca = forca
```

### 4️⃣ Abstração
```python
from abc import ABC, abstractmethod

class Habilidade(ABC):
    @abstractmethod
    def usar(self, usuario, alvo):
        pass  # Obriga classes filhas a implementarem
```

### 5️⃣ Métodos Estáticos
```python
class Dado:
    @staticmethod
    def rolar(lados=6):
        return random.randint(1, lados)
```

---

## 🏗️ Estrutura do Código

```
📦 Sistema RPG
├── 🎲 Itens
│   ├── Arma (nome, poder)
│   └── Poção (nome, cura)
│
├── 🎒 Inventário
│   ├── adicionar_item()
│   ├── usar_pocao()
│   └── mostrar_itens()
│
├── 👤 Personagens
│   ├── Personagem (classe base)
│   ├── Guerreiro (força)
│   ├── Mago (poder mágico)
│   └── Arqueiro (precisão)
│
├── 👹 Monstros
│   ├── Monstro (genérico)
│   └── Orc (com crítico)
│
├── ⚔️ Habilidades
│   ├── Habilidade (abstrata)
│   ├── AtaqueForte
│   ├── BolaDeFogo
│   └── FlechaPerfurante
│
├── 🎲 Utilitários
│   └── Dado (rolar dados)
│
└── ⚔️ Sistema de Batalha
    └── Batalha (gerencia combate)
```

---

## 🦸 Classes de Personagens

### Comparação de Classes

| Classe | Atributo Principal | Dado de Ataque | Variação | Habilidade Especial |
|--------|-------------------|----------------|----------|---------------------|
| ⚔️ **Guerreiro** | Força | d6 | Média | Ataque Forte (1.5x) |
| 🔮 **Mago** | Poder Mágico | d8 | Alta | Bola de Fogo (1.8x) |
| 🏹 **Arqueiro** | Precisão | d4 | Baixa | Flecha Perfurante (1.3x) |

### Detalhes dos Heróis

#### ⚔️ Guerreiro
- **Ataque**: Força + Arma + d6
- **Estilo**: Balanceado e versátil
- **Força**: Dano físico alto
- **Equipamento**: Pode usar qualquer arma

```python
guerreiro = Guerreiro("Arthur", 120, 25)
guerreiro.arma = Arma("Espada Longa", 15)
guerreiro.adicionar_habilidade(AtaqueForte())
```

#### 🔮 Mago
- **Ataque**: Poder Mágico + d8
- **Estilo**: Alto risco/recompensa
- **Força**: Dano mágico devastador
- **Variação**: Maior imprevisibilidade

```python
mago = Mago("Merlin", 90, 40)
mago.adicionar_habilidade(BolaDeFogo())
```

#### 🏹 Arqueiro
- **Ataque**: Precisão + d4
- **Estilo**: Consistente e confiável
- **Força**: Dano preciso
- **Variação**: Menor aleatoriedade

```python
arqueiro = Arqueiro("Legolas", 100, 35)
arqueiro.adicionar_habilidade(FlechaPerfurante())
```

---

## 👹 Monstros

### Goblin Padrão
```python
goblin = Monstro.goblin_padrao()
# Vida: 50 | Dano: 10
```

### Orc com Crítico 💥
```python
orc = Orc.orc_padrao()
# Vida: 100 | Dano: 20 | Chance Crítico: 30%
# Crítico causa 2x de dano!
```

**Mecânica do Crítico:**
- Rola d100
- Se resultado ≤ chance_critico → **CRÍTICO!** (dano x2)
- Caso contrário → dano normal

---

## ⚔️ Sistema de Batalha

### Características

- 🎯 **Turnos Alternados** - Cada lado ataca por vez
- 🎲 **Aleatoriedade** - Dados adicionam imprevisibilidade
- 👥 **Combate em Equipe** - Múltiplos personagens de cada lado
- 🎯 **Seleção Inteligente** - Alvos escolhidos aleatoriamente entre os vivos
- 🏆 **Sistema de Vitória** - Detecta e anuncia o vencedor

### Tipos de Batalha

#### 1. Batalha Individual (1v1)
```python
heroi = Guerreiro("Conan", 100, 30)
monstro = Orc.orc_padrao()

batalha = Batalha(heroi, monstro)
batalha.iniciar()
```

#### 2. Batalha em Equipe (3v3)
```python
herois = [
    Guerreiro("Arthur", 120, 25),
    Mago("Merlin", 90, 40),
    Arqueiro("Legolas", 100, 35)
]

monstros = [
    Monstro.goblin_padrao(),
    Monstro.goblin_padrao(),
    Orc.orc_padrao()
]

batalha = Batalha(herois, monstros)
batalha.iniciar()
```

### Fluxo de Batalha

```
🔵 INÍCIO
   ↓
📊 Exibe Combatentes
   ↓
🔄 LOOP DE TURNOS
   ├─ Lado A ataca
   ├─ Verifica derrota Lado B
   ├─ Lado B ataca
   └─ Verifica derrota Lado A
   ↓
🏆 ANUNCIA VENCEDOR
   ↓
📊 Mostra Sobreviventes
   ↓
🔚 FIM
```

---

## 💻 Instalação e Uso

### Requisitos
- Python 3.8+
- Biblioteca `random` (built-in)
- Biblioteca `abc` (built-in)

### Executar

```bash
# Clone ou baixe o arquivo
python rpg_completo.py
```

### Saída Esperada

```
⚔️  BATALHA INICIADA! ⚔️

🔵 LADO A:
   - Arthur (Vida: 120)
   - Merlin (Vida: 90)
   - Legolas (Vida: 100)

🔴 LADO B:
   - Goblin Padrão (Vida: 50)
   - Goblin Padrão (Vida: 50)
   - Orc Guerreiro (Vida: 100)

--- TURNO 1 ---
Arthur ataca com sua espada! (Base: 40 + Dado: 3)
Goblin Padrão recebeu 43 de dano! Vida restante: 7

💥 Orc Guerreiro desfere um GOLPE CRÍTICO!
Arthur recebeu 52 de dano! Vida restante: 68

...

🏆 FIM DA BATALHA! 🏆
✨ VITÓRIA DO LADO A! ✨

Sobreviventes:
   - Arthur (Vida restante: 45)
   - Merlin (Vida restante: 23)
```

---

## 📝 Exemplos de Código

### Sistema de Inventário

```python
# Criar personagem
heroi = Guerreiro("Arthur", 100, 25)

# Adicionar itens
pocao = Pocao("Poção de Vida", 30)
espada = Arma("Espada Longa", 15)

heroi.inventario.adicionar_item(pocao)
heroi.inventario.adicionar_item(espada)

# Mostrar inventário
heroi.inventario.mostrar_itens()
# Output:
# - Poção: Poção de Vida (Cura: 30)
# - Arma: Espada Longa (+15)

# Usar poção
heroi.vida = 70  # Herói está machucado
heroi.inventario.usar_pocao(heroi)
# Output: "Arthur usou Poção de Vida e recuperou 30 de vida!"
# heroi.vida → 100
```

### Sistema de Habilidades

```python
# Criar personagem
mago = Mago("Gandalf", 100, 45)

# Adicionar habilidade
mago.adicionar_habilidade(BolaDeFogo())
# Output: "Gandalf aprendeu Bola de Fogo!"

# Usar habilidade
orc = Orc("Orc Bruto", 80, 20)
mago.usar_habilidade(0, orc)  # Índice 0 = primeira habilidade
# Output: "Gandalf conjura uma Bola de Fogo devastadora!"
#         "Orc Bruto recebeu 78 de dano! Vida restante: 2"
```

### Aleatoriedade com Dados

```python
# Rolar dado simples
resultado = Dado.rolar(20)  # d20: 1-20
print(f"Rolou: {resultado}")

# Rolar com modificador
resultado = Dado.rolar_com_modificador(20, 5)  # d20 + 5
print(f"Rolou: {resultado}")  # Exemplo: 15 + 5 = 20
```

---

## ✅ Questões Implementadas

### 📊 Resumo por Nível

| Nível | Questões | Pontos | Status |
|-------|----------|--------|--------|
| 🟢 **Básico** | Q1-Q10 | 100 | ✅ Completo |
| 🟡 **Intermediário** | Q11-Q20 | 150 | ✅ Completo |
| 🔴 **Avançado** | Q21-Q30 | 200 | ✅ Completo |
| **TOTAL** | **30** | **450** | **✅ 100%** |

### Detalhamento

#### 🟢 Nível Básico (Q1-Q10)
- ✅ Q1-Q2: Classes de Itens (Arma, Poção)
- ✅ Q3-Q5: Sistema de Inventário
- ✅ Q6-Q8: Classe Base Personagem
- ✅ Q9-Q10: Encapsulamento (@property)

#### 🟡 Nível Intermediário (Q11-Q20)
- ✅ Q11-Q13: Herança (Guerreiro, Mago, Arqueiro)
- ✅ Q14-Q16: Polimorfismo (métodos atacar)
- ✅ Q17-Q18: Classe Monstro
- ✅ Q19-Q20: Factory Methods (@classmethod)

#### 🔴 Nível Avançado (Q21-Q30)
- ✅ Q21: Classe Abstrata Habilidade (ABC)
- ✅ Q22-Q23: Sistema de Habilidades Especiais
- ✅ Q24: Classe Utilitária Dado (@staticmethod)
- ✅ Q25: Aleatoriedade em Combate
- ✅ Q26: Orc com Ataque Crítico
- ✅ Q27-Q28: Sistema de Batalha com Turnos
- ✅ Q29: Anúncio de Vencedor
- ✅ Q30: Batalha em Equipe

---

## 🎯 Recursos Implementados

### Sistema de Combate
- ⚔️ Ataques básicos
- 💥 Ataques críticos (Orc)
- 🎲 Aleatoriedade com dados
- 🎯 Seleção inteligente de alvos
- 🔄 Sistema de turnos

### Sistema de Progressão
- 📈 Atributos únicos por classe
- ⚡ Habilidades especiais
- 🎒 Sistema de inventário
- 💊 Poções de cura
- ⚔️ Sistema de equipamentos

### Mecânicas Avançadas
- 🛡️ Proteção de vida (não fica negativa)
- 💯 Limite de vida máxima
- 🎲 Múltiplos tipos de dados (d4, d6, d8, d10, d20, d100)
- 👥 Combate em equipe
- 🏆 Detecção automática de vitória

---

## 📚 Aprendizados do Projeto

### Conceitos de POO Dominados
1. **Classes e Objetos** - Estrutura fundamental
2. **Encapsulamento** - Proteção de dados
3. **Herança** - Reutilização de código
4. **Polimorfismo** - Comportamentos únicos
5. **Abstração** - Interfaces e contratos
6. **Composição** - Relacionamentos entre objetos
7. **Factory Methods** - Criação padronizada
8. **Métodos Estáticos** - Utilitários
9. **Property Decorators** - Getters e Setters
10. **Type Checking** - isinstance()

### Boas Práticas Aplicadas
- ✅ Nomes descritivos de variáveis
- ✅ Comentários explicativos
- ✅ Organização em seções
- ✅ Métodos pequenos e focados
- ✅ DRY (Don't Repeat Yourself)
- ✅ Responsabilidade única
- ✅ Código limpo e legível

---

## 🚀 Possíveis Expansões

### Ideias para Evolução
- [ ] Interface gráfica (Pygame/Tkinter)
- [ ] Sistema de experiência e níveis
- [ ] Mais classes de personagens
- [ ] Sistema de crafting
- [ ] Salvar/Carregar jogo
- [ ] Magias de área (AOE)
- [ ] Sistema de buff/debuff
- [ ] Modo história
- [ ] Multiplayer local

---

## 👨‍💻 Autor

Desenvolvido como projeto educacional de Programação Orientada a Objetos em Python.

**Conceitos:** POO, Python, Game Development, Design Patterns

---

## 📄 Licença

Este projeto é livre para uso educacional.

---

<div align="center">

### ⭐ Se este projeto te ajudou, deixe uma estrela!

**[⬆ Voltar ao topo](#-sistema-de-rpg-completo---python-poo)**

</div>
