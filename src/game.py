from entity.Board import Board
from exceptions.WinnerFoundException import WinnerFoundException
from utils.count_utils import *


# Return an ordered list of players, ex. [Player 2, Player 0, Player 1]
def choose_player_order(board):
    cards = []        # Represents the cards randomly selected for players
    pairs = {}        # The pairs between player and random card selected

    for player in board.players:
        card = board.deck.get_card()

        print("Card ", card)
        print("Player ", player)
        cards.append(card)
        pairs[card] = player

    cards.sort(key=lambda x: x.face)

    new_order = [pairs[card] for card in cards]

    board.update_players(new_order)
    for i, player in enumerate(board.players, start=1):
        print(f"{i}. {player.name}")  # Display the new player order
    board.deck.shuffle()     # Repopulate the deck


def deal_cards(board):

    # First clear all hands in case not empty
    for player in board.players:
        player.hand.clear()

    # Deal cards
    if board.GAME_MODE == 0:
        cards_to_deal = 6 if board.num_players == 2 else 5
    elif board.GAME_MODE == 1:
        cards_to_deal = 8

    for i in range(cards_to_deal):  # Standard
        for player in board.players:
            player.hand.append(board.deck.get_card())

    # print(player.hand for player in board.players)


def select_hands(board):

    for player in board.players:
        selected_cards = []
        print(f"\n{player.name}'s Turn")

        if board.GAME_MODE == 0:

            # Determine how many cards chosen for crib
            num_cards_to_select = 2 if board.num_players == 2 else 1

            print(
                f"Select {'a card' if board.num_players == 3 else 'two cards'} for " +
                f"{'your' if board.players[board.dealer] == player else 'opponents'} crib: \n")

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
                selected_cards.append(player.hand[card - 1])

            player.hand = [                                        # Remove cards from current players crib
                card for card in player.hand if card not in selected_cards]

            board.players[board.dealer].crib.extend(                 # Add to dealers crib
                selected_cards)

        print("New Hands:")
        for player in board.players:
            print(player.hand)


def get_cut_card(board):
    if board.GAME_MODE == 0:
        board.cut_card = board.deck.get_card()
        print(f"Cut Card is: {str(board.cut_card)}")
    else:
        cut = board.deck.get_card()
        print("Do you want to keep this card? y/n")
        res = input()
        board.cut_card = cut if res == "y" else board.deck.get_card()
        if board.cut_card.name == 'Jack':
            print(f"+1 to {board.dealer.name}: Jack Cut")
            if board.add_points(board.dealer, 2):
                # This will propagate to the game loop and end the game
                raise WinnerFoundException(board.winner)


def play(board):

    total_cards = len(board.players[0].hand) * len(board.players)
    cards_played = []
    curr_player_idx = (board.dealer + 1) % board.num_players
    in_hand = set()
    total = 0
    can_play = [True for i in range(board.num_players)]

    while (len(cards_played) < total_cards):
        print("\nCurr Total: ", total)

        if all(value is False for value in can_play):   # If no more players can play a card

            last_player = board.players[last_played_idx]
            print(f"+1 to {last_player.name}: Last Card")
            if board.add_points(last_player, 1):
                # This will propagate to the game loop and end the game
                raise WinnerFoundException(board.winner)
            curr_player_idx = (last_played_idx + 1) % board.num_players

            # Reinitialize list to all true
            can_play = [True for i in range(board.num_players)]

            total = 0

        # Keeps track of whether a player has a card they can play in their hand
        has_valid_card = False
        curr_player = board.players[curr_player_idx]

        print(f"\n{curr_player.name}'s Turn")

        in_hand.clear()

        # Display cards
        for i, hand_card in enumerate(curr_player.hand, start=1):
            if hand_card in cards_played:
                continue
            if hand_card.value + total <= 31:  # Keep track of the cards a player can play this round
                has_valid_card = True
            in_hand.add(i)
            print(f"====\n{i}. {hand_card}\n====")

        if not has_valid_card:

            print("GO\n")

            can_play[curr_player_idx] = False
            curr_player_idx = (curr_player_idx + 1) % board.num_players
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

            if total + card_played.value < 31:  # Only add the card to total if it doesn't exceed 31

                # Add card to cards played
                cards_played.append(card_played)

                total += card_played.value

                # Store player as last played in case no one else can play
                last_played_idx = curr_player_idx

                # Add any points from a possible run
                points_from_run = count_run_pegging(cards_played)
                print(f"+{points_from_run} to {curr_player.name}: Run")
                if board.add_points(curr_player, points_from_run):
                    # This will propagate to the game loop and end the game
                    raise WinnerFoundException(board.winner)
                # Reinitialize list to all true
                can_play = [True for i in range(board.num_players)]

                curr_player_idx = (curr_player_idx + 1) % board.num_players

            elif total + card_played.value == 31:

                print(f"+2 to {curr_player.name}: 31 Hit")

                if board.add_points(curr_player, 1):
                    # This will propagate to the game loop and end the game
                    raise WinnerFoundException(board.winner)

                total = 0

                # Reinitialize list to all true
                can_play = [True for i in range(board.num_players)]

                curr_player_idx = (curr_player_idx + 1) % board.num_players

            else:
                print("Card value exceeds 31")


# TODO: counts the points for the hands and then the cribs


def count_points(board):
    return


def end_round(board):

    board.deck.shuffle()  # Reupdate deck
    board.update_dealer()  # Get next dealer


def main():

    # Keeps track of points, players, dealer, etc.
    board = Board(0, ["Dylan", "Andrew", "Connor"])

    choose_player_order(board)
    try:

        while True:

            print("New Round")

            deal_cards(board)

            select_hands(board)

            get_cut_card(board)

            play(board)

            print("\Play over\n")

            count_points(board)    # TODO

            end_round(board)
    except WinnerFoundException as e:

        print(f"================\nGame Over!\n{e.winner} has won!!!")


if __name__ == "__main__":
    main()
