def brute_force(pwd="123456"):
    common_pwds_dictionary = open('pwds_dictionary.txt', 'r').readlines()
    common_names_dictionary = open('names_dictionary.txt', 'r').readlines()
    cp = [c for c in common_pwds_dictionary if c == pwd]
    cn = [c for c in common_names_dictionary if c == pwd]
    cnl = [c.lower() for c in common_names_dictionary if c.lower() == pwd]
    if len(cp) == 1:
        print('\nPassword:', cp)
        return cp
    if len(cn) == 1:
        print('\nPassword:', cn)
        return cn
    if len(cnl) == 1:
        print('\nPassword:', cnl)


if __name__ == '__main__':
    brute_force("Nickey")
