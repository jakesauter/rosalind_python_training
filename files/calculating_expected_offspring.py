"""
Script to calculate the total number of offspring
that display the dominant phenotype given the amount
of each parent having the genotypes

1. AA-AA
2. AA-Aa
3. AA-aa
4. Aa-Aa
5. Aa-aa
6. aa-aa

"""

display_prob = [1.0, 1.0, 1.0, 0.75, 0.5, 0.0]
offspring = 2

genotypes = [int(x) for x in input().split()]

expected = sum([offspring * x[0] * x[1] for x in zip(display_prob, genotypes)])

print(expected)
