from ImpostoRenda import calculaIR


def test_less_than_1000():
    assert(calculaIR(875)) == 0


def test_between_1000_2000():
    assert(calculaIR(1468.80)) == 70.32
    assert(calculaIR(2000)) == 150


def test_greater_than_2000():
    assert(calculaIR(2100)) == 170


def test_greater_than_3000():
    assert(calculaIR(4700)) == 690
