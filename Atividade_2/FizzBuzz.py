def fizzBuzz(x):
    if type(x) is not int:
        return "TypeError: must be int"
    elif x%5 == 0 and x%3 == 0:
        return "FizzBuzz"
    elif x%5 == 0:
        return "Buzz"
    elif x%3 == 0:
        return "Fizz"
    elif x<0:
        return "Error: negative number"
    else:
        return x

for i in range(100):
    print(fizzBuzz(i))