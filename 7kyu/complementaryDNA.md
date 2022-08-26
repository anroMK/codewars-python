# Complementary DNA
## Problem

Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

If you want to know more: http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

[codewars](https://www.codewars.com/kata/554e4a2f232cdd87d9000038)
### Example: (input --> output)
```
"ATTGC" --> "TAACG"
"GTAT" --> "CATA"
```

### Solution
```python
def DNA_strand(dna):
    mytable = dna.maketrans('ATCG','TAGC')
    return dna.translate(mytable)
```

### Test
```python
print(DNA_strand("ATTGC"))
print(DNA_strand("GTAT"))
```
