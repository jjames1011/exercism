def to_rna(dna_strand):
    dna_rna_dict = {'G':'C','C':'G','T':'A','A':'U'}
    dna_strand = dna_strand.upper()
    dna_strand = dna_strand.replace(' ','')
    rna_Complement = ''
    for char in dna_strand:
        if char in dna_rna_dict:
            rna_Complement = rna_Complement + dna_rna_dict[char]
        else:
            raise ValueError('Your input was invalid')
    return rna_Complement
