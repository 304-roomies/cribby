from entity.Board import Board


def main():

    board = Board(0, ["Dylan", "Andrew", "Connor"])

    board.choose_player_order()
    gameloop:
    while True:

        print("New Round")

        board.deal_cards()

      #   board.select_hands()

        board.get_cut_card()

        board.pegging()

        print("\nPegging over\n")

        # board.count_cards()    # TODO

        board.end_round()

    winner = board.get_winner()

    print(f"================\nGame Over!\n {player} ")


if __name__ == "__main__":
    main()
