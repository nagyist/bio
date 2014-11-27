import math
from .hamming import hamming_distance
from .numberpattern import all_nucleotides

def min_distance(pattern, text):
    """
    Given a k-mer Pattern and a longer string Text, we use d(Pattern, Text) to
    denote the minimum Hamming distance between Pattern and any k-mer in Text,
    """
    k = len(pattern)
    result = float("inf")
    for i in range(len(text) - k):
        splice = text[i:i + k]
        distance = hamming_distance(pattern, splice)
        if distance < result:
            result = distance
    return result


def min_dna_distance(pattern, dna):
    """
    Given a k-mer Pattern and a set of strings Dna = {Dna1, … , Dnat}, we define
    d(Pattern, Dna) as the sum of distances between Pattern and all strings 
    in Dna.
    """
    return sum(min_distance(pattern, text) for text in dna)


def median_string(dna, k):
    distance = float("inf")
    medians = []
    for pattern in all_nucleotides(k, stringify=True):
        d = min_dna_distance(pattern, dna)
        if d < distance:
            distance = d
            median = [pattern]
        elif d == distance:
            median.append(pattern)
    return median


def main():
    assert(min_distance("GATTCTCA", "GCAAAGACGCTGACCAA") == 3)
    assert(min_dna_distance("AAA", "TTACCTTAAC GATATCTGTC ACGGCGTTCG CCCTAAAGAG CGTCAGAGGT".split()) == 5)
    print(median_string("AAATTGACGCAT GACGACCACGTT CGTCAGCGCCTG GCTGAGCACCGG AGTACGGGACAG".split(), 3))

if __name__ == '__main__':
    main()
