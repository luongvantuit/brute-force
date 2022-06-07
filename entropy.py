import string
import math


def verify_pwd(pwd: str):
    all_char = string.digits + string.ascii_letters + string.punctuation
    for i in pwd:
        if i not in all_char:
            return False
    return True


def entropy(pwd: str):
    has_digits = False
    has_ascii = False
    has_punctuation = False
    for i in pwd:
        if (i in string.digits):
            has_digits = True
        if (i in string.ascii_letters):
            has_ascii = True
        if (i in string.punctuation):
            has_punctuation = True
    l_pwd = 0
    if (has_digits):
        l_pwd += len(string.digits)
    if (has_ascii):
        l_pwd += len(string.ascii_letters)
    if (has_punctuation):
        l_pwd += len(string.punctuation)
    return len(pwd) * (math.log(l_pwd)/math.log(2)), l_pwd


if __name__ == '__main__':
    pwd = input('Enter your password:\n')
    if not verify_pwd(pwd):
        print('Password not valid')
    else:
        e, l_collection = entropy(pwd)
        print('Length of the password: %d\n' % len(pwd))
        print('Cardinality: %d\n' % l_collection)
        print('Entropy: %.2f\n' % e)
        print('Time guess: %.2fs\n' % ((l_collection ** len(pwd))/(2*10*6)))
