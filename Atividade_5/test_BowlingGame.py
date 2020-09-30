from BowlingGame import roll, score


def test_score_0_gutter_game():
    for _ in range(20):
        roll(0)

    assert(score()) == 0
