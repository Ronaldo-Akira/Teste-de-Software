from FizzBuzz import fizzBuzz

def test_not_a_integer():
    assert fizzBuzz("Otavio") == "TypeError: must be int"
    assert fizzBuzz(3.2) == "TypeError: must be int"

def test_negative_integer():
    assert fizzBuzz(-1) == "Error: negative number"

def test_multiple_three():
    assert fizzBuzz(3) == "Fizz"
    assert fizzBuzz(6) == "Fizz"

def test_multiple_five():
    assert fizzBuzz(5) == "Buzz"
    assert fizzBuzz(10) == "Buzz"

def test_multiple_five_and_three():
    assert fizzBuzz(15) == "FizzBuzz"

def test_not_multiples_five_or_three():
    assert fizzBuzz(1) == 1
    assert fizzBuzz(28) == 28