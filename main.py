from game import *
from algos import *

game = PrisonersDilemma(noise=0.1)
game = simulate(game, tit_for_tat, random_moves)
print(game.winner)
print(game.p1_score, game.p2_score)
print([(game.p1_previous_moves[i], game.p2_previous_moves[i]) for i in range(game.current_round-1)])
