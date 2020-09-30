from BowlingGame import Game


def test_score_0_gutter_game():
    g = Game()
    for _ in range(20):
        g.roll(0)

    assert(g.get_score()) == 0


def test_all_one_game():
    g = Game()
    for _ in range(20):
        g.roll(1)

    assert(g.get_score()) == 20
