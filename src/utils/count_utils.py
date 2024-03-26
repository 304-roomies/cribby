
def count_runs_hand(hand):

    # for
    # sorted =
    return


def count_run_pegging(cards):
    # Grab the last 7 cards since the max run possible is of length 7
    to_check = cards[3:]

    # Need to only check if the most recent card played is in a run
    last_card = cards[-1]

    max_run = 0
    # is_run = False

    # We will start with the last 3 cards played, and continue until we reach 7 cards since that is the max run possible
    for i in range(3, min(7, len(cards)) + 1):

        to_check = cards[-i:]  # Check if the last i cards form a run

        to_check.sort(key=lambda x: x.face)

        # If highest card - lowest card == # of Cards - 1, then there is a run.
        if to_check[-1].face - to_check[0].face == len(to_check) - 1:
            max_run = len(to_check)
            # is_run = True

    return max_run


def count_sets():

    return
