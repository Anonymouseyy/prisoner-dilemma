import random


def tit_for_tat(self_moves, opp_moves):
    if not opp_moves:
        return False

    return opp_moves[-1]


def tit_for_two_tats(self_moves, opp_moves):
    if len(opp_moves) < 2:
        return False

    return opp_moves[-2] and opp_moves[-1]


def random_moves(self_moves, opp_moves):
    return random.random() > 0.5
