import random
from IPython.display import clear_output


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += 2*self.bet
        self.bet = 0
    
    def lose_bet(self):
        self.total -= self.bet
        self.bet = 0


class Card:
	suit = ''
	rank = ''
	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank
		
	def __str__(self):
		return self.rank +" of "+ self.suit
		

class Deck:
	deck = []

	def __init__(self):
	    
	    for suit in suits:
	        for rank in ranks:
	            self.deck.append(Card(suit,rank))
	    
	def shuffle(self):
	    random.shuffle(self.deck)



class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
    	if card.rank == 'Ace':
    		self.aces += values[card.rank]
    	self.value+=values[card.rank]
    	self.cards.append(card)
    
    def adjust_for_ace(self):
       	if self.value>21 and self.aces>=11:
       		acenum = self.aces / 11
       		while self.value>21 and acenum != 0:
	       		self.value -= 10
	       		self.aces -= 10
	       		acenum -= 1
        else:
          pass

def take_bet(chips):
	global playing
	if chips.total == 0:
		print("You connot play as you don't have chips")
		playing = False
		return
	while True:
		try:
			chips.bet = int(input("The Bet is:"))
			if chips.bet > chips.total:
				print("You don't have that amount of chips availabel.")
				continue
		except:
			print("Please give a number.")
		else:
			break

def hit(deck,hand):
    newcard = deck.deck[0]
    deck.deck.remove(newcard)
    hand.add_card(newcard)
    if hand.value > 21:
    	hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    action = input("Hit or Stand? :")
    if action == 'hit':
    	hit(deck,hand)
    	if player.value > 21:
    		playing = False
    else:
    	playing = False


def show_some(player,dealer):
    clear_output();
    print("Dealer's cards:")
    print("--------------------")
    sum=0
    print("Hidden card,")
    for card in dealer.cards[1:]:
        print (card.__str__() + ', ')
        sum+=values[card.rank]
    print("--------------------")
    print(f"Total : {sum}")


    print("\nPlayer's cards:")
    print("--------------------")
    for card in player.cards:
        print (card.__str__() + ', ')
    print("--------------------")
    print(f"Total : {player.value}")
        
def show_all(player,dealer):
    clear_output();
    print("Dealer's cards:")
    print("--------------------")
    for card in dealer.cards:
        print (card.__str__() + ', ')
    print("--------------------")
    print(f"Total : {dealer.value}")



    print("\nPlayer's cards:")
    print("--------------------")
    for card in player.cards:
        print (card.__str__() + ', ')
    print("--------------------")
    print(f"Total : {player.value}")

def player_busts(chips):
	print("YOU LOSE!")
	chips.lose_bet()
    
def player_wins(chips):
	print("YOU WIN!")
	chips.win_bet()

def dealer_busts(chips):
	print("YOU WIN!")
	chips.win_bet()
    
def dealer_wins(chips):
	print("YOU LOSE!")
	chips.lose_bet()
    
def push(chips):
	print("PUSH!")
	playing = False
	pass


# Set up the Player's chips
chips = Chips()

while True:
    print("New Game!")

    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()


    player = Hand()
    dealer = Hand()

    hit(deck,player)
    hit(deck,player)

    hit(deck,dealer)
    hit(deck,dealer)
        
    
    
    
    # Prompt the Player for their bet
    take_bet(chips)
    if playing == False:
    	break
    
    # Show cards (but keep one dealer card hidden)
    show_some(player,dealer)

    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player)
        
        
        # Show cards (but keep one dealer card hidden)
        show_some(player,dealer)

    if player.value > 21:
    	show_all(player,dealer)
    	player_busts(chips)

    else:
	

	    while dealer.value < 17: # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
		    hit(deck,dealer)
	    
		    # Show all cards
		    show_some(player,dealer)
	    
	    show_all(player,dealer)
	    # Run different winning scenarios
	    if dealer.value > 21:
	    	dealer_busts(chips)
	    else: 
	        if dealer.value > player.value:
	            dealer_wins(chips)
	        if dealer.value < player.value:
	            player_wins(chips)
	        if dealer.value ==  player.value:
	            push(chips)

    # Inform Player of their chips total 
    print(f"Your chips are: {chips.total}")
    # Ask to play again
    again = input("New Game? (y/n): ")
    if again == 'n':
    	break
    else:
    	playing = True