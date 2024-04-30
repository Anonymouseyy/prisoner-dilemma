from game import *
from algos import *

game = simulate(tit_for_tat, tit_for_two_tats)
print([(game.p1_previous_moves[i], game.p2_previous_moves[i]) for i in range(game.current_round-1)])
