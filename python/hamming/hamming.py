
def distance(strand_a, strand_b):
    hamming = 0
    i = 0
    if len(strand_a) != len(strand_b):
        raise ValueError('The DNA strands must be the same length')
    for char in strand_a:
        if strand_b[i] != strand_a[i]:
            hemming += 1
        i+=1
    return hamming
