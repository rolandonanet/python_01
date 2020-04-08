import math
import abc
import random

# 1 Linha: Crie a classe Linha que tem dois atributos, coordenada1 e coordenada2.
# Cada coordenada é uma tupla que carrega duas coordenadas cartesianas (x,y) que
# denotam pontos do segmento de reta. Faça métodos que calculem o comprimento
# do segmento de reta e sua inclinação.

class Line():
    def __init__ (self, coordinate1, coordinate2):
        self.coordinate1 = coordinate1
        self.coordinate2 = coordinate2
        print("Nova lina criada nas coordenadas", coordinate1, coordinate2)
    
    def getLineLenght(self):
        return ((self.coordinate1[0] - self.coordinate2[0])**2 + (self.coordinate1[1] - self.coordinate2[1])**2)**0.5

    def getLineAngle(self):
        return((self.coordinate1[1] - self.coordinate2[1]) / (self.coordinate1[0] - self.coordinate2[0]))

test = Line((10, 12), (12, 14))

print(test.getLineLenght())
print(test.getLineAngle())



# 2 Figuras: Crie a seguinte hierarquia de classes de figuras geométricas.
# a. A classe abstrata Figura deve ter o método abstrato area.
# b. A classe concreta Circulo é subclasse de Figura.
# c. A classe abstrata Poligono é subclasse de Figura e deve ter os
# atributos base e altura .
# d. As classes concretas Triangulo, Losango, Retangulo e Quadrado são
# subclasses de Poligono. Tente criar mais uma generalização aqui olhando as fórmulas
# da área.
# e. Os polígonos Retangulo e Quadrado devem implementar a interface
# Diagonal, que deve ter um método que calcula a diagonal.
# f. Crie uma classe Geometria com uma lista de Figuras com pelo menos
# uma figura de cada e imprima suas áreas, perímetros e diagonais.

class Diagonal(abc.ABC):
    @abc.abstractmethod
    def getDiagonal(height, width):
        return (height**2 + width**2)**0.5

class Shape:

    def __init__(self):
        print("Nova figura criada")

    def getArea(self):
        pass

    def getPerimeter(self):
        pass

class Polygon(Shape):

    def __init__(self):
        print("Novo poligono criado")


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius
        print("Novo círculo criado com raio:", radius)

    def getArea(self):
        return math.pi * (self.radius ** 2)

    def getPerimeter(self):
        return 2 * math.pi * self.radius


class Triangle (Polygon):

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        print("Novo triângulo criado com lado 1:", side1, "lado 2:", side2, "outro lado 3:", side3)

    def getArea(self):
        semi_perimeter = self.getPerimeter()/2
        return (semi_perimeter*(semi_perimeter - self.side1)*(semi_perimeter - self.side2)*(semi_perimeter - self.side3))**0.5

    def getPerimeter(self):
        return self.side1 + self.side2 + self.side3


class Rhombus(Polygon):

    def __init__(self, height, width):
        self.height = height
        self.width = width
        print("Novo losango criado com altura:", height, "largura:", width)

    def getSide(self):
        return ((self.height/2)**2 + (self.width/2)**2)**0.5

    def getArea(self):
        return self.height * self.width/2

    def getPerimeter(self):
        return self.getSide() * 4


class Rectangle(Polygon, Diagonal):

    def __init__(self, height, width):
        self.height = height
        self.width = width
        print("Novo retângulo criado com altura:", height, "largura:", width)

    def getArea(self):
        return self.height * self.width

    def getDiagonal(self):
        return Diagonal.getDiagonal(self.height, self.width)

    def getPerimeter(self):
        return self.height*2 + self.width*2


class Square(Polygon, Diagonal):

    def __init__(self, side):
        self.side = side
        print("Novo quadrado criado com lado:", side)
    
    def getArea(self):
        return self.side**2

    def getDiagonal(self):
        return Diagonal.getDiagonal(self.side, self.side)

    def getPerimeter(self):
        return self.side*4


class Geometry():
    def __init__(self, shapes):
        self.shapes = shapes
    
    def printInfo(self):
        for shape in self.shapes:
            print("Objeto encontrado:", type(shape).__name__)
            print("A área do objeto é:", shape.getArea())
            print("O perímetro do objeto é:", shape.getPerimeter())
            try:
                print("A diagonal do objeto é:", shape.getDiagonal())
            except(Exception):
                pass


shapes = [
    Circle(10), 
    Triangle(10, 11, 12),
    Rhombus(5,6),
    Rectangle(2,4),
    Square(10)
]

geometry = Geometry(shapes)

geometry.printInfo()



# 3 Jogo de Blackjack: Faça um joguinho simples em Python.
# Aqui estão os requisitos:
# - Você precisa criar um jogo de BlackJack (21) baseado em texto simples
# - O jogo precisa ter um jogador contra um croupier automatizado.
# - O jogador pode desistir ou bater.
# - O jogador deve ser capaz de escolher o seu valor de aposta.
# - Você precisa acompanhar o dinheiro total do jogador.
# - Você precisa alertar o jogador de vitórias, derrotas ou estouros, etc ...
# E o mais importante:
# Você deve usar OOP e classes em alguma parte do seu jogo. Você não pode
# simplesmente usar funções no seu jogo. Use classes para ajudá-lo a definir o deck e a
# mão do jogador. Há muitas maneiras certas de fazer isso, então explore bem!
# Regras do Jogo:
# https://en.wikipedia.org/wiki/Blackjack
# https://pt.wikipedia.org/wiki/Blackjack



class Player():
  def __init__(self, name, money):
    self.name = name
    self.cur_hand = []
    self.money = money
    self.betting = 0

  def getName(self):
    return self.name

  def getMoney(self):
    return self.money
  
  def setMoney(self, money):
    self.money = money

  def setCurHand(self, cur_hand):
    self.cur_hand = cur_hand

  def getCurHand(self):
    return self.cur_hand

  def getPoint(self):
    if sum(self.cur_hand) <= 11 and 1 in self.cur_hand:
      return sum(self.cur_hand) + 10
    return sum(self.cur_hand)

  def addBet(self, ammount):
    print("Aumentando", self.name, "aposta para ", ammount)
    self.money -= ammount
    self.betting += ammount

  def gainBetMoney(self, money):
    self.money += money

  def ressetBet(self):
    self.betting = 0

  def getBet(self):
    return self.betting

  def addCard(self, card):
    self.cur_hand.append(card)

  def cleanHand(self):
    self.cur_hand = []


class Deck():
  def __init__(self, deck=[]):
    self.deck = 4 * [x for x in range(1,11)]
    self.deck = self.deck + (12 * [10])
    self.shuffleCards()

  def drawCard(self, player_name):
    to_return = self.deck[0]
    self.deck.pop(0)
    print("Jogador", player_name, "puxou", to_return)
    return to_return

  def shuffleCards(self):
    random.shuffle(self.deck)

  def getDeck(self):
    return self.deck


class Game():
  def __init__(self, player, dealer, bet):
    self.player = player
    self.dealer = dealer
    self.generateInitialBet(bet)
    self.deck = Deck()
    for __ in range(2):
      self.player.addCard(self.deck.drawCard(self.player.getName()))
      self.dealer.addCard(self.deck.drawCard(self.dealer.getName()))
    self.showScore()
   

  def generateInitialBet(self, bet):
    if self.player.getMoney() < bet:
      bet = self.player.getMoney()
    if self.dealer.getMoney() < bet:
      bet = self.dealer.getMoney()
    
    self.player.addBet(bet)
    self.dealer.addBet(bet)


  def drawStage(self):

    while input("Puxar uma carta? ") in positive:
      self.player.addCard(self.deck.drawCard(self.player.getName()))
      if(player.getPoint() >= 21):
        return
      self.showScore()

  
    while dealer.getPoint() < player.getPoint():
      self.dealer.addCard(self.deck.drawCard(self.dealer.getName()))
      if(dealer.getPoint() >= 21):
        return 
      self.showScore()

  def checkStartWinner(self):
    
    if(self.player.getPoint() == 21):
      print("Jogador", self.player.getName(), "ganhou!")
      self.player.gainBetMoney(self.player.getBet()*2)
      return True

    if(self.dealer.getPoint() == 21):
      print("Jogador", self.dealer.getName(), "ganhou!")
      self.dealer.gainBetMoney(self.dealer.getBet()*2)
      return True

    return False

  def checkWinner(self):

    if(self.dealer.getPoint() > 21 or ((not self.player.getPoint() > 21) and (self.player.getPoint() == 21 or self.player.getPoint() > self.dealer.getPoint()))):
      print("Jogador", self.player.getName(), "ganhou!")
      self.player.gainBetMoney(self.player.getBet()*2)
    elif self.player.getPoint() == self.dealer.getPoint():
      print("Empate!")
      self.player.gainBetMoney(self.player.getBet())
      self.dealer.gainBetMoney(self.dealer.getBet())
    else:
      print("Jogador", self.dealer.getName(), "ganhou!")
      self.dealer.gainBetMoney(self.dealer.getBet()*2)

  def showScore(self):
    print("Total apostado:", self.player.getBet())
    print("Dinheiro jogador ", self.player.getName(),"R$",self.player.getMoney())
    print("Dinheiro jogador ", self.dealer.getName(),"R$",self.dealer.getMoney())
    print("Mão do jogador", self.player.getName(), ":", self.player.getCurHand())
    print("Mão do jogador", self.dealer.getName(), ":", self.dealer.getCurHand())
    print(self.player.getName(), "tem", self.player.getPoint())
    print(self.dealer.getName(), "tem", self.dealer.getPoint())
    
  
  def finish(self):
    self.player.ressetBet()
    self.player.cleanHand()
    self.dealer.ressetBet()
    self.dealer.cleanHand()


name = input("Nome do jogador: ")
money = float(input("Quanto dinheiro deseja começar com: "))

player = Player(name, money)
dealer = Player("Croupier", 10000.0)

option_continue = True
positive = ["sim", "yes", "true", "s", "y"]


while player.getMoney() > 0 and option_continue:

  bet = float(input("Aposta inicial: "))

  game = Game(player, dealer, bet)

  if not game.checkStartWinner():

    dealing_stage = True

    game.drawStage()

    game.showScore()

    game.checkWinner()

  print("Total apostado:", player.getBet())
  print("Dinheiro jogador ", player.getName(),"R$",player.getMoney())
  print("Dinheiro jogador ", dealer.getName(),"R$",dealer.getMoney())

  game.finish()

  option_continue = input("Continuar? ") in positive

print("Obrigado por jogar blackjack!")
print("Seu dinheiro final:", player.getMoney())
