from standard import *
vout("------v py compiler ------")
cp=vin("> ")
with open(cp+'.vy','r') as f:
    temp=f.read()
write_file('temp.py','w','from standard import *\n'+temp)
run('temp.py')