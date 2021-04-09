def rev_comp(s):
    return s[::-1].translate(str.maketrans('ACGT', 'TGCA'))