from SillyPascal import sillyPascal


def test_starts_with_a_letter():
    assert sillyPascal("a1234") == True
    assert sillyPascal("1234") == False


def test_contains_only_letters_or_digits():
    assert sillyPascal("a1234") == True
    assert sillyPascal("a12^34") == False


def test_string_length():
    assert sillyPascal("Otavio") == True
    assert sillyPascal("a12345678") == False
    assert sillyPascal("") == False


def test_null_string():
    assert sillyPascal(None) == False
