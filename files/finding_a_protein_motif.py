"""
This program uses the weburl library to access the 
FASTA data for a protein using the online database
of UniProt
"""

import urllib.request
import re

web_string = 'https://www.uniprot.org/uniprot/'


f = open("rosalind_mprt.txt")
protein_list = f.read().strip().split("\n")
f.close()

for prot_name in protein_list:

    """
    If we get redirected we now have to access the 
    redirected link and read the info from that page
    """

    try: 
        weburl = urllib.request.urlopen(web_string + prot_name + '.fasta')
    except: 
        weburl = urllib.requrest.urlopen(weburl.url)
    
    
    data = ''.join(str(weburl.read())[2:].split("\\n")[1:-1])
    
    indices = [m.start()+1 for m in re.finditer('(?=N[^P][S|T][^P])', data)]
    
        if indices != []: 
    
        print(prot_name + "\n" + ' '.join([str(x) for x in indices]))


