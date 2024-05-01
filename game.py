import random


class PrisonersDilemma:
    def __init__(self, both_split_points=3, both_steal_points=1, one_split_points=0, one_steal_points=5, noise=0):
        self.current_round = 1
        self.noise = noise

        self.p1_score = 0
        self.p2_score = 0
        self.winner = None

        self.p1_previous_moves = []
        self.p2_previous_moves = []

        self.both_split_points = both_split_points
        self.both_steal_points = both_steal_points
        self.one_split_points = one_split_points
        self.one_steal_points = one_steal_points

    def win(self):
        if self.p1_score == self.p2_score:
            self.winner = -1
        elif self.p1_score > self.p2_score:
            self.winner = 1
        elif self.p2_score > self.p1_score:
            self.winner = 2

        return self.winner

    def process_moves(self, p1, p2):
        # Introduce random noise
        if random.random() < self.noise:
            p1 = not p1
        if random.random() < self.noise:
            p2 = not p2

        self.p1_previous_moves.append(p1)
        self.p2_previous_moves.append(p2)

        # True if steal, False if split
        if p1 and p2:
            self.p1_score += self.both_steal_points
            self.p2_score += self.both_steal_points
        elif not p1 and not p2:
            self.p1_score += self.both_split_points
            self.p2_score += self.both_split_points
        elif p1 and not p2:
            self.p1_score += self.one_steal_points
            self.p2_score += self.one_split_points
        elif not p1 and p2:
            self.p1_score += self.one_split_points
            self.p2_score += self.one_steal_points

        self.current_round += 1


def simulate(game, player1, player2, rounds=200):
    """
    :param game: A PrisonersDilemma game object
    :param player1: Function that takes a list of all previous moves, the first list being its own moves
                    and the second being the opponent's moves, and returns a move
    :param player2: Function that takes a list of all previous moves, the first list being its own moves
                    and the second being the opponent's moves, and returns a move
    :param rounds: Number of rounds to be played
    :return: A finished Prisoner's Dilemma game object
    """

    for _ in range(rounds):
        p1_move = player1(game.p1_previous_moves, game.p2_previous_moves)
        p2_move = player2(game.p2_previous_moves, game.p1_previous_moves)
        game.process_moves(p1_move, p2_move)

    game.win()
    return game
