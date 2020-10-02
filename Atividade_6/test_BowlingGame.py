from BowlingGame import Game


def roll_many(pins, n, g):
    for _ in range(n):
        g.roll(pins)


def test_bowling_initial_values():
    # mutant
    g = Game()
    assert(g.score()) == 0


def test_bowling_plays_different_than_21():
    # mutant
    g = Game()
    assert(len(g.rolls)) == 21


def test_two_strikes():
    g = Game()
    roll_strike(g)
    g.roll(3)
    g.roll(3)
    assert(g.score()) == 22
    roll_strike(g)
    roll_many(0, 16, g)
    assert(g.score()) == 32


def test_strike():
    g = Game()
    roll_strike(g)
    g.roll(5)
    roll_many(0, 18, g)
    assert(g.score()) == 20


def test_score_0_gutter_game():
    g = Game()
    roll_many(0, 20, g)
    assert(g.score()) == 0


def test_all_one_game():
    g = Game()
    roll_many(1, 20, g)
    assert(g.score()) == 20


def test_two_spares():

    g = Game()
    roll_spare(g)
    g.roll(5)
    g.roll(0)
    roll_spare(g)
    g.roll(7)
    g.roll(0)
    roll_many(0, 12, g)
    assert(g.score()) == 44


def test_spare():
    g = Game()
    roll_spare(g)
    g.roll(3)
    roll_many(0, 17, g)
    assert(g.score()) == 16


def test_perfect_game():
    g = Game()
    roll_many(10, 12, g)
    assert(g.score()) == 300


def roll_strike(g):
    g.roll(10)


def roll_spare(g):
    g.roll(5)
    g.roll(5)
