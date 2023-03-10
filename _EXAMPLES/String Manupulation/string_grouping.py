# this separates numbers and alphabets
a = 'absc123iop984'


def answer(string):
    alphabets = ''
    result = ''
    for char in string:
        if char.isdigit():
            result += char
        else:
            alphabets += char

    return (alphabets, result)


print(answer(a))
