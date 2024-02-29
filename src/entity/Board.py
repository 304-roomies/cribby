from .Player import Player
from .Deck import Deck
from .Card import Card


class Board:

    def __init__(self, mode, players):
        # 0 = Standard, 1 = Performance, 2 = Menos
        self.GAME_MODE = mode
        self.players = self.init_players(
            players)    # List of strings with names
        self.deck = Deck()
        self.num_players = len(players)
        self.winner = None
        # Tracks the index of the current dealer in players array
        self.dealer = 0

    def init_players(self, players):
        return [Player(name=player) for player in players]

    def get_winner():
        return

    # Return an ordered list of players, ex. [Player 2, Player 0, Player 1]

    def choose_player_order(self):
        cards = []        # Represents the cards randomly selected for players
        pairs = {}        # The pairs between player and random card selected

        for player in self.players:
            card = self.deck.get_card()

            print("Card ", card)
            print("Player ", player)
            cards.append(card)
            pairs[card] = player

        cards.sort(key=lambda x: x.value)

        self.players = [pairs[card] for card in cards]
        print(pairs)

        print(self.players)

        self.deck.shuffle()     # Repopulate the deck

        return self.players

    def deal_cards(self):

        # First clear all hands in case not empty
        for player in self.players:
            player.hand.clear()

        # Deal cards
        if self.GAME_MODE == 0:
            cards_to_deal = 6 if self.num_players == 2 else 5
        elif self.GAME_MODE == 1:
            cards_to_deal = 8

        for i in range(cards_to_deal):  # Standard
            for player in self.players:
                player.hand.append(self.deck.get_card())

        # print(player.hand for player in self.players)

    def select_hands(self):

        for player in self.players:
            selected_cards = []

            num_cards_to_select = 2 if self.num_players == 2 else 1

            print(f"\n{player.name}'s Turn")
            print(
                f"Select {'a' if self.num_players == 3 else 'two'} card{'' if self.num_players == 3 else 's'} for " +
                f"{'your' if self.players[self.dealer] == player else 'opponents'} crib: \n")

            # Display cards
            for i, hand_card in enumerate(player.hand, start=1):
                print(f"====\n{i}. {hand_card}\n====")

            # Select cards
            for i in range(1, num_cards_to_select + 1):
                card = 0
                while card not in range(1, 7):
                    print("Please enter a valid card")
                    try:
                        card = int(input(f"Card {i}: "))
                    except:
                        continue
                selected_cards.append(player.hand[card + 1])

            player.hand = [                                        # Remove cards from current players crib
                card for card in player.hand if card not in selected_cards]

            self.players[self.dealer].crib.extend(                 # Add to dealers crib
                selected_cards)

        print("New Hands:")
        for player in self.players:
            print(player.hand)

    def get_cut_card(self):
        if self.GAME_MODE == 0:
            self.cut_card = self.deck.get_card()
        else:
            cut = self.deck.get_card()
            print("Do you want to keep this card? y/n")
            res = input()
            self.cut_card = cut if res == "y" else self.deck.get_card()

    def pegging(self):

        # TODO: Fix the tracking of cards played per player in pegging

        total_cards = len(self.players[0].hand) * len(self.players)
        cards_played = []
        curr_player_idx = (self.dealer + 1) % self.num_players
        in_hand = set()
        total = 0
        can_play = [True for i in range(self.num_players)]

        while (len(cards_played) < total_cards):
            print("\nCurr Total: ", total)

            if all(value is False for value in can_play):

                last_player = self.players[last_played_idx]
                print(f"Last Card!\n1 point to {last_player.name}")
                curr_player_idx = (last_played_idx + 1) % self.num_players

                # Reinitialize list to all true
                can_play = [True for i in range(self.num_players)]

                total = 0

            # Keeps track of whether a player has a card they can play in their hand
            has_valid_card = False
            curr_player = self.players[curr_player_idx]

            print(f"\n{curr_player.name}'s Turn")

            in_hand.clear()

            # Display cards
            for i, hand_card in enumerate(curr_player.hand, start=1):
                if hand_card in cards_played:
                    continue
                if hand_card.value + total <= 31:
                    has_valid_card = True
                in_hand.add(i)
                print(f"====\n{i}. {hand_card}\n====")

            if not has_valid_card:

                print("GO\n")

                can_play[curr_player_idx] = False
                curr_player_idx = (curr_player_idx + 1) % self.num_players
                continue

            try:
                card = int(input("Select a Card to Play:\n"))

            except:                 # Integer not inputted, catch exception
                print("\nPlease Choose a Valid Card\n")
                continue

            if card not in in_hand:  # Card selected not valid
                print("\nPlease Choose a Valid Card\n")

            else:                   # Card selected valid, proceed to next player
                card_played = curr_player.hand[card - 1]

                if total + card_played.value <= 31:  # Only add the card to total if it doesn't exceed 31

                    cards_played.append(card_played)

                    total += card_played.value

                    last_played_idx = curr_player_idx

                    if total == 31:
                        print(f"31 hit!\n2 points to {curr_player.name}")
                        total = 0

                        # Reinitialize list to all true
                        can_play = [True for i in range(self.num_players)]

                    curr_player_idx = (curr_player_idx + 1) % self.num_players

                else:
                    print("Card value exceeds 31")

    def end_round(self):

        self.deck.shuffle()

        self.dealer = (self.dealer + 1) % self.num_players
