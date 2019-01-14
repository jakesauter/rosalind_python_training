# rosalind_python_training

Using the rosalind.info site for bioinformatic programming to sharpen my python and mathematical skills. The link for each problem will bring you to the problem prompt on the rosalind.info site, and the link for each solution will bring you to my solution in this repository.

[**Counting DNA Nucleotides**](http://rosalind.info/problems/dna/) -- [counting_dna_2.py](files/counting_dna_2.py)

[**Transcribing DNA into RNA**](http://rosalind.info/problems/rna/) -- [transcribing.py](files/transcribing.py)

[**Completing a Strand of DNA**](http://rosalind.info/problems/revc/) -- [complimentary_dna.py](files/complimentary_dna.py)

[**Rabbits and Reccurrence Relations**](http://rosalind.info/problems/fib/) -- [reccurrence_relations.py](files/reccurrence_relations.py)

[**Computing GC Content**](http://rosalind.info/problems/gc/) -- [gc_content_2.py](files/gc_content_2.py) -- features use of the **split** and **join** commands

[**Counting Point Mutations**](http://rosalind.info/problems/hamm/) -- [hamming_distance_2.py](files/hamming_distance_2.py) -- makes use of the **zip** and **count** commands

[**Mendel's First Law**](http://rosalind.info/problems/iprb/) -- [mendels_first_law_2.py](files/mendels_first_law_2.py) -- allowed me to get reaquanited with combinatorics

[**Translating RNA into Protein**](http://rosalind.info/problems/prot/) -- [rna_to_protein_2.py](files/rna_to_protein_2.py) -- features use of the zip command as well as using it to form key-value pairs to intialize a dictionary

[**Finding a Motif in DNA**](http://rosalind.info/problems/subs/) -- 
                          [dna_motifs.py](files/dna_motifs.py) -- features the use of regular expressions including 
                                                                  lookahead assertionss
                          [dna_motifs_2.py](files/dna_motifs_2.py) -- features the use of the **str.find()** function with the
                                                                  optional offset argument **str.find(string,offset)**
                          [dna_motifs_3.py](files/dna_motifs_3.py) -- very simple, pythonic and readble, makes use of the 
                                                                      **str.startswith(string)** function
                                                                      
[**Consensus and Profile**](http://rosalind.info/problems/cons/) -- [consensus_and_profile.py](files/consensus_and_profile.py) -- Was reminded that strings can be accessed as arrays in this one, as well as encountering accidental overwriting of duplicated arrays. CANNOT use \[\[0]\*ncol]\*nrow to make a 2d array, must use \[\[0]\*ncol for i in range(nrow)]            

[**Mortal Fibbonacci Rabbits**](http://rosalind.info/problems/fibd/) -- 
                            [mortal_fib_rabbits.py](files/mortal_fib_rabbits.py) -- A simple solution independently tracking the amount of baby rabbit pairs or "little" rabbits and mature rabbits pairs or "big" rabbits
                            [mortal_fib_rabbits_2.py](files/mortal_fib_rabbits_2.py) -- A less straightforward but more efficient solution in which an array tracks the ages of each pair of rabbits, with the total number of living rabbits being the sum of the array elements.
