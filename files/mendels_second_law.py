"""
Mendel's second law is that alleles for different factors are
inherited with no dependence on each other. This statement has
become his second law, also known as the law of independent
assortment.
"""

"""
Given: Two positive integers k (k≤7) and N (N≤2k). In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. Tom has two children in the 1st generation, each of whom has two children, and so on. Each organism always mates with an organism having genotype Aa Bb.

Return: The probability that at least N
Aa Bb organisms will belong to the k-th generation of Tom's family tree (don't count the Aa Bb mates at each level). Assume that Mendel's second law holds for the factors.

probability of Aa Bb from any parent with an Aa Bb parent is 
P(Aa) from any parent with an Aa parent times P(Bb) in the same
situation

P(Aa) = .5
P(Bb) = .5

P(Aa)*P(Bb) = .5 * .5 = (1/2) * (1/2) = (1/4) = .25

From further observation, this is a binomial random variable

"""

from scipy.special import comb as nCr

k,n = [int(x) for x in input().strip().split()]
K = 2**k

prob = 0

for n_i in range(n,K+1):

    prob += nCr(K,n_i) * (.25**n_i) * (.75**(K-n_i))
    
"""
ALSO could use the built in scipy binomial distribution
funcion

from scipy.stats import binom
1 - binom.cdf(n - 1, 2 ** k, 0.25)
"""
    
    
print(prob)         
