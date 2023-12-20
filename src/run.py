from entity.Board import Board



def main():
   

   board = Board(0, 6, ["Dylan", "Andrew", "Connor", "Bob", "Joe", "Poop"])

   board.choose_player_order()

if __name__ == "__main__":
    main()