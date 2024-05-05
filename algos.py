# https://plato.stanford.edu/entries/prisoner-dilemma/strategy-table.html
import random


def unconditional_cooperate(self_moves, opp_moves):
    return False


def unconditional_steal(self_moves, opp_moves):
    return True


def tit_for_tat(self_moves, opp_moves):
    if not opp_moves:
        return False

    return opp_moves[-1]


def aggressive_tit_for_tat(self_moves, opp_moves):
    if not opp_moves:
        return True

    return opp_moves[-1]


def tit_for_two_tats(self_moves, opp_moves):
    if len(opp_moves) < 2:
        return False

    return opp_moves[-2] and opp_moves[-1]


def random_moves(self_moves, opp_moves):
    return random.random() > 0.5


def trigger(self_moves, opp_moves):
    if not opp_moves:
        return False

    return True in opp_moves
