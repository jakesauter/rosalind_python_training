""" We will be keeping a running maximum 
    GC content encountered variable """

max_gc_name = ''
max_gc = 0
cur_name = ''
cur_gc = 0

gc_string = ''


""" This method of opening a file automatically closes
    it at the end of the loop """
    
with open('rosalind_gc.py') as f:
   
    cur_name = f.read()
    
    gc_string = f.read()
    
    cur_gc = gc_string.count('G') + gc_string.count('C')
    
    cur_gc = cur_gc / len(gc_string)
    
    if(cur_gc > max_gc): 
    
        max_gc_name = cur_name
        max_gc = cur_gc
        
print(max_gc_name[1:])               
