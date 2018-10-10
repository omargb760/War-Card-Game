"""
Omar Gonzalez
omargb22@gmail.com
file type : .py
Language: python

The purpose of this program is to create a popular card game named war, where each player draws a card from the deck, and the player witht he hiighest card wins.
This program is intended to be for object_orientied practice and it is referencing "The Self Taught Programer Book by Cory Althoff"

ReadME: To play the game
game=Game()
game.playgame()
"""
#------------------------------------------------class for Cards--------------------------------------------------------------#
class Card:
	"""
	docstring for Card:
	:param v: value of the card 2-9,jack=10, queen= 11, king=12, & ace=13
	:param s: suit of the card, 0=spades,heart=1,diamonds=2,& clubs=3
	:param c2: Object type Card parameter for comparason purpose
	methods:
	will crate a card object, when given a value(v) and a suite(s).
	will compare two Card objects when 2 cards are passed with <,> or ==.
	"""
	#2 class variables which are suits[], and value[]
	suits =["spades","hearts", "diamonds","clubs"] # contains the type of card
	values=[None, None, "2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"] #contains the value of the card

	#Initializing Card class
	def __init__ (self,v,s):
		"""Suit plus value are ints"""
		self.value=v
		self.suit=s
	# Magic Method, Less then
	def __lt__(self,c2):
		if self.value < c2.value:
			return True
		# If both card contains the same value, check which is the grater suite
		if self.value == c2.value:
			if self.suit <c2.suit:
				return True
			else:
				return False
		return False
	#Magic Method, Greater then.
	def __gt__(self, c2):
		if self.value > c2.value:
			return True
		# If both card contains the same value, check which is the grater suite
		if self.value == c2.value:
			if self.suit > c2.suit:
				return True
			else:
				return False
		return False
	#Magic Method, look up value and suite.
	def __repr__(self):
		v = self.values[self.value] + " of " + self.suits[self.suit]
		return v
#------------------------------------------------class for Deck--------------------------------------------------------------#
from random import shuffle

class Deck:
	"""
	docstring for Deck:
	:No parameters
	This class is resposible for shuffing and creating deck of cards.
	Pass in cards and it removes and returns a card from the cards list, or returns none if it is empty.
	"""
	def __init__(self):
		self.cards=[] #card list initialized to empty
		#When you call Deck, this diuble for loop will create Card Object representing all 52-card deck
		for i in range(2, 15): #2 to 15 because the first value of the deck of cards is 2 and the last card is 14 (ace)
			for j in range(4): # 4 because there is 4 suites in a deck of card
				self.cards.append(Card(i,j)) #append each card to list card
		shuffle(self.cards) #shuffe deck from random module

	def rm_card(self): #this method removes and returns a card from the cards list, or returns none if it is empty.
		if len(self.cards) == 0:
			return
		return self.cards.pop()

#------------------------------------------------class for Player--------------------------------------------------------------#
class Player:
 	"""
 	docstring for Player:
 	:param name: name of the player
 	Purpose: creates a player.
 	:3intance variables:
 		-'win' keeps track of how many time each player wins,
 		-'name' name of the player
 		-'card' keeps track of the card that the player is currently holding
 	"""
 	def __init__ (self, name):
 		self.wins = 0
 		self.card = None
 		self.name = name

#------------------------------------------------class for Game--------------------------------------------------------------#

class Game:
	"""
	docstring for Game:
	-create Game Object and program will ask for names for player 1&2.
	-method: play_game() starts the game.
	-method: winner() takes two player objects and looks at the number of rounds they've won and returns the player who won the most rounds.
	"""
	def __init__(self):
		name1 = input ("p1 name ")
		name2 = input ("p2 name ")
		self.deck = Deck()
		self.p1 = Player(name1)
		self.p2 = Player(name2)

	def wins(self, winner):
		w = "{} wins this round"
		w = w.format(winner)
		print(w)

	def draw(self,p1n,p1c,p2n,p2c):
		d = "{} drew {} and {} drew {}"
		d = d.format (p1n, p1c, p2n, p2c)
		print(d)

	def play_game(self):
		cards= self.deck.cards
		print("-------Beginning War!--------")
		while len(cards)>=2:
			m = "q to quit. Any " + "key to play:"
			response = input(m)
			if response == "q":
				break

			p1c = self.deck.rm_card()
			p2c = self.deck.rm_card()
			p1n = self.p1.name
			p2n = self.p2.name
			self.draw(p1n, p1c, p2n, p2c)
			if p1c > p2c:
				self.p1.wins += 1
				self.wins(self.p1.name)
			else:
				self.p2.wins += 1
				self.wins(self.p2.name)

		win = self.winner(self.p1, self.p2)

		print("War is over. {} wins ".format(win))

	def winner(self, p1, p2):
		if p1.wins > p2.wins:
			return p1.name
		if p1.wins < p2.wins:
			return p2.name
		return "It was a tie!"
