####################
## Card Game: War ##
####################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you and the computer. If you don't know
# how to play "War", here are some basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of card face down,
# in front of him
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher card takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the higher
# card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for you.
# Ignore "double" wars.
#
# https://en.wikipedia.org/wiki/War (card_game)


from random import shuffle

# Two useful variables for creating Cards
SUITES = "H D S C".split()
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()

class Deck():
    """
    This is the Deck class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITES and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and shuffling the deck.
    """

    def __init__(self):
        self.card_deck = [(s, r) for s in SUITES for r in RANKS]

    def shuffle(self):
        shuffle(self.card_deck)

    def cut(self):
        return (self.card_deck[:26], self.card_deck[26:])


class Hand():
    """
    This is the Hand class. Each player has a Hand, and can add or remove cards
    from hand. There should be an add and remove card method here.
    """

    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards.".format(len(self.cards))

    def add(self, card_list):
        # self.cards.extend(card_list)
        for card in card_list:
            self.cards.insert(0, card)

    def remove(self):
        return self.cards.pop()

    def get_hand_length(self):
        return len(self.cards)



class Player():
    """
    This is the Player class, which takes in a name and an instance of Hand class
    object. The player can then play cards and check if they still ahave cards.
    """

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove()
        print("{} has played: {}\n".format(self.name, drawn_card))
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.remove())
            return war_cards

    def still_has_cards(self):
        """
        :return True if Player sitll has cards left to play
        """
        # return len(self.hand.cards) != 0
        return self.hand.get_hand_length() != 0



###############
## GAME PLAY ##
###############

def main():
    print("Welcome to WAR!! Let's begin ")

    # Create new Deck and split in half
    deck = Deck()
    deck.shuffle()
    half1, half2 = deck.cut()

    # Create both Players
    name = input("Enter your name to play: ")

    user = Player(name, half1)
    comp = Player("Computer", half2)

    total_round_count = 0
    war_round_count = 0

    while user.still_has_cards() and comp.still_has_cards():

        total_round_count += 1

        print("Time for a new round!")
        print("Here are the current standings: ")
        print("{} has the count: {}".format(user.name, str(len(user.hand.cards))))
        print("{} has the count: {}".format(comp.name, str(len(comp.hand.cards))))
        print("Play a card!\n")

        table_cards = []

        u_card = user.play_card()
        c_card = comp.play_card()

        table_cards.append(u_card)
        table_cards.append(c_card)

        if u_card[1] == c_card[1]:
            war_round_count += 1

            print("WAR Round!!")

            table_cards.extend(user.remove_war_cards())
            table_cards.extend(comp.remove_war_cards())

            if RANKS.index(u_card[1]) > RANKS.index(c_card[1]):
                user.hand.add(table_cards)
            else:
                comp.hand.add(table_cards)

        else:
            if RANKS.index(u_card[1]) > RANKS.index(c_card[1]):
                user.hand.add(table_cards)
            else:
                comp.hand.add(table_cards)

    print("Game Over!!")
    print("Total number of rounds played: {}".format(str(total_round_count)))
    print("Total number of WAR rounds played: {}".format(str(war_round_count)))




main()