import re


def sillyPascal(identificador):
    if identificador == None:
        return False
    elif re.match("^[a-zA-Z]+[a-zA-Z0-9]*$", identificador) and 1 <= len(identificador) <= 6:
        return True
    else:
        return False
