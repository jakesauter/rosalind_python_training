string  = raw_input("")

a_s = len([x for x in string if x=="A"])

c_s = len([x for x in string if x=="C"])

g_s = len([x for x in string if x=="G"])

t_s = len([x for x in string if x=="T"])

print a_s, c_s,  g_s, t_s 
