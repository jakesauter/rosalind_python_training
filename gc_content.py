""" We will be keeping a running maximum 
    GC content encountered variable """

max_gc_name = ''
max_gc = 0
cur_name = ''
cur_gc = 0

gc_string = ''


""" This method of opening a file automatically closes
    it at the end of the loop """
    
with open('rosalind_gc.txt') as f:
    
    for line in f:
    
        if(line[0] == ">"):
        
            cur_name = line[1:]
            
            if(len(gc_string) == 0):
                continue
                    
            cur_gc = gc_string.count('G') + gc_string.count('C')
                
            cur_gc = cur_gc / len(gc_string)
            
            if(cur_gc > max_gc): 
    
                max_gc_name = cur_name
                max_gc = cur_gc
                
            gc_string = ''
            
        else:
        
            gc_string = gc_string + line.strip() 
    
cur_gc = gc_string.count('G') + gc_string.count('C')
                
cur_gc = cur_gc / len(gc_string)
                      
if(cur_gc > max_gc): 
    
    max_gc_name = cur_name
    max_gc = cur_gc
        
print(max_gc_name,round(max_gc*100, 7))               
