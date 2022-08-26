def DNA_strand(dna):
    mytable = dna.maketrans('ATCG','TAGC')
    return dna.translate(mytable)

print(DNA_strand("ATTGC"))
print(DNA_strand("GTAT"))
