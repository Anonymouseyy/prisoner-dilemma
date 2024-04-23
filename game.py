class PrisonersDilemma:
    def __init__(self, rounds=200, both_split_points=3, both_steal_points=1, one_split_points=0, one_steal_points=-5):
        self.current_round = 1
        self.total_rounds = rounds

        self.p1_score = 0
        self.p2_score = 0
        self.winner = None

        self.both_split_points = both_split_points
        self.both_steal_points = both_steal_points
        self.one_split_points = one_split_points
        self.one_steal_points = one_steal_points

    def determine_winner(self):
        if self.p1_score == self.p2_score:
            return -1
        elif self.p1_score > self.p2_score:
            return 1
        elif self.p2_score > self.p1_score:
            return 2

    def process_moves(self, p1, p2):
        if p1 == "steal" and p2 == "steal":
            self.p1_score += self.both_steal_points
            self.p2_score += self.both_steal_points
        elif p1 == "split" and p2 == "split":
            self.p1_score += self.both_split_points
            self.p2_score += self.both_split_points
        elif p1 == "steal" and p2 == "split":
            self.p1_score += self.one_steal_points
            self.p2_score += self.one_split_points
        elif p1 == "split" and p2 == "steal":
            self.p1_score += self.one_split_points
            self.p2_score += self.one_steal_points

        self.current_round += 1

        if self.current_round >= self.total_rounds:
            return self.winner()

